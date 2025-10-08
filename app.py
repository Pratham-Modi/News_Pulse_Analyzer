import streamlit as st
from config import INTERFACE_LANGUAGES, UI_TEXT, EXTENDED_CATEGORIES, USER_SELECTABLE_NEWS_LANGUAGES
from modules.login import login_page
from modules.news_fetcher import get_all_news
from modules.preprocessing import preprocess_news
from modules.sentiment_analysis import analyze_sentiment
from modules.ner_analysis import extract_entities
from modules.topic_modeling import generate_topics
from modules.trend_analysis import detect_trends
from modules.cross_sector import compute_category_correlation, plot_correlation_heatmap
from modules.chatbot_integration import chatbot_interface
from utils.visualization import plot_sentiment_pie, plot_category_bar, generate_wordcloud, plot_timeline

# -----------------------------
# Login Page
# -----------------------------
login_page()

# Only proceed if user is logged in
if st.session_state.get("logged_in", False):

    st.sidebar.subheader("Dashboard Settings")

    # Language selection
    user_lang = st.sidebar.selectbox(
        UI_TEXT[st.session_state.language]["language"],
        USER_SELECTABLE_NEWS_LANGUAGES,
        index=USER_SELECTABLE_NEWS_LANGUAGES.index(st.session_state.language)
    )

    # Category selection
    category = st.sidebar.selectbox(
        UI_TEXT[st.session_state.language]["select_category"],
        list(EXTENDED_CATEGORIES.keys())
    )

    st.sidebar.markdown("---")
    st.sidebar.write(f"Logged in as: {st.session_state.username}")

    # Fetch News
    if st.sidebar.button(UI_TEXT[st.session_state.language]["fetch_news"]):
        with st.spinner("Fetching news..."):
            df_news = get_all_news(category=category.lower(), language=user_lang)

            if df_news.empty:
                st.warning("No news found for the selected category/language.")
            else:
                # -----------------------------
                # Preprocess Text
                # -----------------------------
                df_news["clean_text"] = df_news["title"].fillna("") + " " + df_news["content"].fillna("")
                df_news = preprocess_news(df_news, text_column="clean_text")

                # -----------------------------
                # Sentiment Analysis
                # -----------------------------
                df_news = analyze_sentiment(df_news, text_column="clean_text")

                # -----------------------------
                # Named Entity Recognition
                # -----------------------------
                df_news = extract_entities(df_news, text_column="clean_text")

                # -----------------------------
                # Topic Modeling
                # -----------------------------
                df_news, topic_model, probs = generate_topics(df_news, text_column="clean_text")

                # -----------------------------
                # Trend Analysis
                # -----------------------------
                trends_df = detect_trends(df_news)

                # -----------------------------
                # Display News
                # -----------------------------
                st.subheader("📰 Latest News")
                for idx, row in df_news.iterrows():
                    st.markdown(f"**{row.get('title', '')}**")
                    st.write(row.get('content', ''))
                    st.write(f"**Source:** {row.get('source','')}")
                    st.write(f"**Sentiment:** {row.get('sentiment', '')}")
                    st.write(f"**Entities:** {row.get('entities','')}")
                    st.write(f"**Topic:** {row.get('topic','')}")
                    st.markdown("---")

                # -----------------------------
                # Visualizations
                # -----------------------------
                fig = plot_sentiment_pie(df_news)
                if fig: st.plotly_chart(fig)

                fig = plot_category_bar(df_news)
                if fig: st.plotly_chart(fig)

                generate_wordcloud(" ".join(df_news["clean_text"].tolist()))

                fig = plot_timeline(trends_df)
                if fig: st.plotly_chart(fig)

    # Chatbot Section
    st.markdown("## Chatbot Assistant")
    chatbot_interface()
