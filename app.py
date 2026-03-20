import streamlit as st
import sqlite3
import pandas as pd
import subprocess

if st.button("Run Pipeline"):
    subprocess.run(["python", "pipeline.py"])
    st.success("Pipeline berhasil dijalankan!")

st.title("📊 Data Pipeline Dashboard")

conn = sqlite3.connect("data/mentah/reviews.db")

df = pd.read_sql("SELECT * FROM reviews", conn)

st.write("### Data Preview")
st.dataframe(df)

st.write("### Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

st.write("### Insight")

top_sentiment = df["sentiment"].value_counts().idxmax()

if top_sentiment == "Negative":
    st.error("Mayoritas user tidak puas ⚠️")
elif top_sentiment == "Positive":
    st.success("Mayoritas user puas 🎉")
else:
    st.info("Sentimen cenderung netral")

st.write("### Query Result")

query = "SELECT sentiment, COUNT(*) as total FROM reviews GROUP BY sentiment"
query_df = pd.read_sql(query, conn)

st.dataframe(query_df)

sentiment_filter = st.selectbox(
    "Filter Sentiment",
    ["All", "Positive", "Neutral", "Negative"]
)

if sentiment_filter != "All":
    df = df[df["sentiment"] == sentiment_filter]

st.metric("Total Data", len(df))
st.metric("Positive", (df["sentiment"]=="Positive").sum())
st.metric("Negative", (df["sentiment"]=="Negative").sum())
conn.close()