import os
import pandas as pd

DATA_DIR = "data"

def load_all_reviews():
    print(f"📥 Loading all review CSVs from: {DATA_DIR}")
    all_files = [
        os.path.join(DATA_DIR, file)
        for file in os.listdir(DATA_DIR)
        if file.endswith(".csv")
    ]

    dfs = []
    for file in all_files:
        print(f"📄 Checking file: {file}")
        try:
            df = pd.read_csv(file, encoding="ISO-8859-1")
            print(f"✅ Loaded with columns: {list(df.columns)}")
            if 'extract' in df.columns and 'product' in df.columns:
                dfs.append(df[['product', 'extract']])
            else:
                print("❌ Missing required columns.")
        except Exception as e:
            print(f"⚠️ Error reading {file}: {e}")

    if not dfs:
        raise ValueError("No valid dataframes loaded.")

    full_df = pd.concat(dfs, ignore_index=True)
    print(f"✅ Total reviews loaded: {len(full_df)}")
    return full_df


def get_reviews_for_phone(df, phone_name):
    # Match by 'product' column
    filtered = df[df['product'].str.lower().str.contains(phone_name.lower(), na=False)]
    print(f"🔎 Found {len(filtered)} reviews for: {phone_name}")
    return filtered['extract'].dropna().tolist()
