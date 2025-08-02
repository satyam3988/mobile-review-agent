# agents/summarization_agent.py

from statistics import mean
from transformers import pipeline



# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_review(reviews: str) -> str:
    """
    Summarizes a group of reviews into a concise summary based on features.
    :param reviews: A string containing all reviews concatenated.
    :param features: A list of features to focus on in the summary.
    :return: A summary string.
    """
    FEATURES = ["battery", "camera", "display", "performance", "storage", "charging", "design"]
    if not reviews:
        return "No reviews provided."

    # Generate a prompt to guide the summarization model
    prompt = f"Summarize the following reviews focusing on these features: {', '.join(FEATURES)}.\n\n{reviews}"

    # Use the summarization model
    summary = summarizer(prompt, max_length=150, min_length=50, do_sample=False)

    # Return the generated summary
    return summary[0]["summary_text"]