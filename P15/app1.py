import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Web Scraping Outputs", layout="wide")

st.title("📊 Web Scraping Project Outputs")

# Sidebar navigation
tab = st.sidebar.radio("Choose a section:", [
    "📚 Coursera Python Courses",
    "💬 Tweet Sentiment Analysis",
    "🎬 Netflix Movie Duration Analysis"
])

# 1️⃣ Coursera
if tab == "📚 Coursera Python Courses":
    st.header("📚 Coursera Python Courses")
    try:
        df = pd.read_csv("coursera_courses.csv")
        st.success(f"Loaded {len(df)} courses.")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "coursera_courses.csv", "text/csv")
    except FileNotFoundError:
        st.error("❌ 'coursera_courses.csv' not found. Please make sure the file exists.")

# 2️⃣ Tweet Sentiment
elif tab == "💬 Tweet Sentiment Analysis":
    st.header("💬 COVID-19 Tweet Sentiment Analysis")
    try:
        df = pd.read_csv("tweets_with_sentiment.csv")
        st.success(f"Loaded {len(df)} tweets.")
        st.dataframe(df.head(100))  # Limit display

        sentiment_counts = df['Sentiment'].value_counts()
        fig, ax = plt.subplots()
        sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'], ax=ax)
        ax.set_title('Tweet Sentiment Distribution')
        ax.set_xlabel('Sentiment')
        ax.set_ylabel('Tweet Count')
        st.pyplot(fig)

        csv = df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "tweets_with_sentiment.csv", "text/csv")
    except FileNotFoundError:
        st.error("❌ 'tweets_with_sentiment.csv' not found.")

# 3️⃣ Netflix Analysis
elif tab == "🎬 Netflix Movie Duration Analysis":
    st.header("🎬 Netflix Movie Duration Analysis")
    try:
        df = pd.read_csv("netflix_avg_duration_by_country.csv")
        st.success("Data loaded successfully.")
        st.dataframe(df.head(10))

        top10 = df.head(10).set_index("country")
        fig, ax = plt.subplots(figsize=(10, 6))
        top10["duration_minutes"].plot(kind='bar', color='teal', edgecolor='black', ax=ax)
        ax.set_title('Top 10 Countries by Average Movie Duration')
        ax.set_ylabel('Average Duration (minutes)')
        ax.set_xlabel('Country')
        st.pyplot(fig)

        csv = df.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "netflix_avg_duration_by_country.csv", "text/csv")
    except FileNotFoundError:
        st.error("❌ 'netflix_avg_duration_by_country.csv' not found.")
