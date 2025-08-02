import streamlit as st
import pandas as pd
from data_loader.phone_review_selector import load_top_reviews, get_all_phones, get_reviews_and_scores
from langgraph_workflow import build_feature_sentiment_graph, ReviewState

# Page configuration
st.set_page_config(
    page_title="Mobile Review Agent",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .rating-badge {
        background-color: #28a745;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
    }
    .summary-box {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📱 Mobile Review Agent</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for phone selection
with st.sidebar:
    st.header("📱 Phone Selection")
    
    # Load data
    with st.spinner("Loading phone data..."):
        df = load_top_reviews()
        phones = get_all_phones(df)
    
    st.success(f"✅ Loaded {len(phones)} phones")
    
    # Phone selection
    selected_phone = st.selectbox(
        "Choose a phone to analyze:",
        options=phones,
        index=0,
        help="Select a phone from the dropdown to get feature-wise sentiment analysis and summary"
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This app analyzes mobile phone reviews to provide:
    - **Feature-wise sentiment analysis**
    - **Rating scores for each feature**
    - **Comprehensive summary**
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"📊 Analysis for {selected_phone}")
    
    # Get reviews and ratings
    with st.spinner("Fetching reviews and analyzing..."):
        phone_data = get_reviews_and_scores(df, selected_phone)
        reviews = phone_data["reviews"]
        
        if not reviews:
            st.error(f"❌ No reviews found for {selected_phone}.")
            st.stop()
        
        # Run LangGraph workflow
        graph = build_feature_sentiment_graph()
        initial_state = ReviewState({"review": " ".join(reviews)})
        
        final_state = graph.invoke(initial_state)
        
        # Extract results
        feature_sentiment = final_state.get("feature_sentiment")
        summary = final_state.get("summary")
    
    # Display feature-wise ratings
    st.subheader("🎯 Feature-wise Ratings")
    
    # Create columns for features
    feature_cols = st.columns(2)
    
    for idx, (feature, data) in enumerate(feature_sentiment.items()):
        col_idx = idx % 2
        with feature_cols[col_idx]:
            with st.container():
                st.markdown(f"""
                <div class="feature-card">
                    <h4>{feature.capitalize()}</h4>
                    <p><strong>Sentiment:</strong> {data['sentiment']}</p>
                    <span class="rating-badge">Rating: {data['rating']}/5</span>
                </div>
                """, unsafe_allow_html=True)
    
    # Display summary
    st.subheader("📝 Summary")
    st.markdown(f"""
    <div class="summary-box">
        {summary}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.header("📈 Quick Stats")
    
    # Display some statistics
    if feature_sentiment:
        # Calculate average rating
        ratings = [data['rating'] for data in feature_sentiment.values()]
        avg_rating = sum(ratings) / len(ratings)
        
        # Count positive/negative sentiments
        positive_features = sum(1 for data in feature_sentiment.values() 
                             if 'positive' in data['sentiment'].lower())
        negative_features = sum(1 for data in feature_sentiment.values() 
                             if 'negative' in data['sentiment'].lower())
        
        st.metric("📊 Average Rating", f"{avg_rating:.1f}/5")
        st.metric("✅ Positive Features", positive_features)
        st.metric("❌ Negative Features", negative_features)
        st.metric("📱 Total Features", len(feature_sentiment))
    
    # Display review count
    st.metric("📝 Reviews Analyzed", len(reviews))
    
    # Feature breakdown chart
    if feature_sentiment:
        st.subheader("📊 Rating Breakdown")
        ratings_df = pd.DataFrame([
            {"Feature": feature.capitalize(), "Rating": data['rating']}
            for feature, data in feature_sentiment.items()
        ])
        
        st.bar_chart(ratings_df.set_index("Feature"))

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Powered by LangGraph & Streamlit | Mobile Review Analysis Agent</p>
</div>
""", unsafe_allow_html=True) 