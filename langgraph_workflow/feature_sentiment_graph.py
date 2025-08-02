from langgraph.graph import StateGraph
from agents.feature_sentiment_agent import classify_features
from agents.summarization_agent import summarize_review

class ReviewState(dict):
    pass

def feature_sentiment_node(state: ReviewState):
    review = state["review"]
    features_result = classify_features(review)
    return ReviewState({**state, "feature_sentiment": features_result})

def summarization_node(state: ReviewState):
    summary = summarize_review(state["review"])
    return ReviewState({**state, "summary": summary})

def build_feature_sentiment_graph():
    builder = StateGraph(ReviewState)

    builder.add_node("feature_sentiment", feature_sentiment_node)
    builder.add_node("summarize", summarization_node)

    builder.set_entry_point("feature_sentiment")
    builder.add_edge("feature_sentiment", "summarize")  # ✅ required
    builder.set_finish_point("summarize")                # ✅ must finish here

    return builder.compile()