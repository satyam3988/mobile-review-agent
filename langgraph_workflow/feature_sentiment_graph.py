# langgraph_workflow/feature_sentiment_graph.py

from langgraph.graph import StateGraph
from agents.feature_sentiment_agent import classify_features

# Define the state object that will carry data through the graph
class ReviewState(dict):
    pass

# Agent node: Classifies the feature-wise sentiment
def feature_sentiment_node(state: ReviewState):
    review = state["review"]
    features_result = classify_features(review)
    return ReviewState({
        "review": review,
        "feature_sentiment": features_result
    })

# Build and compile the graph
def build_feature_sentiment_graph():
    builder = StateGraph(ReviewState)

    builder.add_node("feature_sentiment", feature_sentiment_node)

    builder.set_entry_point("feature_sentiment")
    builder.set_finish_point("feature_sentiment")  # ✅ FIXED: only one argument

    return builder.compile()
