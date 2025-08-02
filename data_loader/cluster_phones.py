import pandas as pd
import re
from fuzzywuzzy import fuzz

# 1. Normalize phone names
def normalize_name(name):
    if not isinstance(name, str):
        return ''
    name = re.sub(r'[^A-Za-z0-9 ]+', ' ', name)  # Remove special chars
    name = re.sub(r'\s+', ' ', name).strip()     # Collapse whitespace
    name = name.lower()

    # Remove GB, colors, and storage sizes
    name = re.sub(r'\b\d+\s?gb\b', '', name)
    name = re.sub(r'\b(black|white|silver|gold|rose|gray|grey|space|guld|rosa|prateado|cinza|rymdgrå|stellar|rosegold|dourado|sølv|vit|gris|grå|matt|sort|azul|blue|pink|red)\b', '', name)
    name = re.sub(r'\bapple\b', '', name)
    name = re.sub(r'\bsmartphone\b', '', name)
    name = re.sub(r'\s+', ' ', name).strip()

    return name

# 2. Group similar names using fuzzy match
def group_similar_names(normalized_names, threshold=90):
    groups = {}
    seen = set()

    for name in normalized_names:
        if name in seen:
            continue
        group_key = name
        groups[group_key] = [name]
        seen.add(name)

        for other in normalized_names:
            if other in seen:
                continue
            if fuzz.partial_ratio(name, other) >= threshold:
                groups[group_key].append(other)
                seen.add(other)

    return groups

# 3. Run pipeline
def cluster_products(df, column='product'):
    df['normalized'] = df[column].apply(normalize_name)
    unique_names = df['normalized'].dropna().unique()
    groups = group_similar_names(unique_names)

    # Build reverse mapping: normalized -> cluster group
    name_to_group = {}
    for group, members in groups.items():
        for member in members:
            name_to_group[member] = group

    df['cluster'] = df['normalized'].map(name_to_group)
    return df, groups

# Example usage
if __name__ == "__main__":
    from data_loader.kaggle_review_loader import load_all_reviews
    df = load_all_reviews()

    print("🔍 Clustering phones...")
    clustered_df, groups = cluster_products(df)

    print(f"\n📊 Found {len(groups)} groups:")
    for i, (group, members) in enumerate(groups.items(), 1):
        print(f"{i}. 📱 {group} ({len(members)} variants)")
        if i >= 20:
            break  # only show top 20

    # Save to CSV if needed
    # clustered_df.to_csv("cleaned_clustered_reviews.csv", index=False)
