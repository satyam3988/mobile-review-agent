from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
FEATURES = ["battery", "camera", "display", "performance", "storage", "charging", "design"]

def classify_features(review: str):
    results = {}

    for feature in FEATURES:
        classification = classifier(
            review,
            [f"positive {feature}", f"negative {feature}", f"neutral {feature}"]
        )
        label = classification['labels'][0]
        score = classification['scores'][0]

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
