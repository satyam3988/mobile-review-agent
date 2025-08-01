from transformers import pipeline

# Load a zero-shot classification pipeline for now
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Candidate product features
FEATURES = ["battery", "camera", "display", "performance", "storage", "charging", "design"]

def classify_review_by_feature(review):
    results = {}

    for feature in FEATURES:
        classification = classifier(review, [f"positive {feature}", f"negative {feature}", f"neutral {feature}"])
        label = classification['labels'][0]  # Top prediction
        score = classification['scores'][0]

        # Simplified score mapping to 0–5 scale
        if 'positive' in label:
            rating = round(3 + 2 * score, 1)
        elif 'neutral' in label:
            rating = round(2.5 + 0.5 * score, 1)
        else:
            rating = round(2 - 2 * score, 1)

        results[feature] = {
            "sentiment": label.split()[0],
            "rating": rating
        }

    return results


# --- Test the agent ---
if __name__ == "__main__":
    review = "The battery life is excellent, but the camera struggles is not at all good i think one of the worst camera i have ever seen. Display is crisp and bright."
    output = classify_review_by_feature(review)
    from pprint import pprint
    pprint(output)
