from data_loader.phone_review_selector import load_top_reviews, get_all_phones, get_reviews_and_scores
from langgraph_workflow import build_feature_sentiment_graph, ReviewState

def main():
    # Step 1: Load the data
    df = load_top_reviews()

    # Step 2: Display available phones
    phones = get_all_phones(df)
    print("\n📱 Available Phones:")
    for idx, phone in enumerate(phones[:100]):
        print(f"{idx+1}. {phone}")

    # Step 3: User selects a phone
    choice = int(input("\n🔢 Enter the number of the phone to summarize: ")) - 1
    selected_phone = phones[choice]

    # Step 4: Get reviews and ratings
    phone_data = get_reviews_and_scores(df, selected_phone)
    reviews = phone_data["reviews"]

    if not reviews:
        print(f"❌ No reviews found for {selected_phone}.")
        return

    # Step 5: Run LangGraph workflow
    graph = build_feature_sentiment_graph()
    initial_state = ReviewState({"review": " ".join(reviews)})

    final_state = graph.invoke(initial_state)

    # Step 6: Display output
    feature_sentiment = final_state.get("feature_sentiment")
    summary = final_state.get("summary")

    print(f"\n📊 Feature-wise Ratings for {selected_phone}:")
    for feature, data in feature_sentiment.items():
        print(f"  - {feature.capitalize()}: {data['sentiment']} ({data['rating']}/5)")

    print("\n📝 Summary:")
    print(summary)

if __name__ == "__main__":
    main()
