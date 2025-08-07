from transformers import pipeline
import math

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
FEATURES = ["battery", "camera", "display", "performance", "storage", "charging", "design"]

def sigmoid_scale(score: float) -> float:
    """Apply sigmoid scaling to convert 0–1 score into 0–5 rating."""
    return 5 / (1 + math.exp(-10 * (score - 0.5)))

def classify_features(review: str):
    results = {}

    for feature in FEATURES:
        classification = classifier(
            review,
            [f"positive {feature}", f"negative {feature}", f"neutral {feature}"]
        )
        label = classification['labels'][0].split()[0]  # 'positive', 'negative', etc.
        score = classification['scores'][0]             # 0–1

        # Use sigmoid scaling
        if label == 'positive':
            rating = round(sigmoid_scale(score), 2)
        elif label == 'negative':
            rating = round(5 - sigmoid_scale(score), 2)
        else:  # neutral
            rating = 2.5  # or optionally: round(sigmoid_scale(0.5), 2)

        results[feature] = {
            "sentiment": label,
            "rating": rating
        }

    return results
