from langgraph_workflow import build_feature_sentiment_graph, ReviewState


def main():
    # Example input (you can make this dynamic later)
    review = "The battery lasts very long, but the camera performance is poor and the display is just okay."

    state = ReviewState({"review": review})
    graph = build_feature_sentiment_graph()

    output = graph.invoke(state)

    print("\n📊 Feature Sentiment Results:")
    for feature, data in output["feature_sentiment"].items():
        print(f"{feature.capitalize()}: {data['sentiment'].upper()} ({data['rating']}/5)")

if __name__ == "__main__":
    main()
