import pandas as pd
import datetime

positive_words = ["bagus", "membantu", "cepat"]
negative_words = ["error", "lambat", "crash"]

def clean_text(text):
    return text.lower()

def sentiment_label(text):
    score = 0
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

def transform_data(df):
    print("Sebelum transform:", len(df))

    df["text"] = df["text"].astype(str)

    df["clean_text"] = df["text"].apply(clean_text)
    df["sentiment"] = df["clean_text"].apply(sentiment_label)
    df["text_length"] = df["text"].apply(len)
    df["processed_at"] = datetime.datetime.now()

    df = df[df["text"].str.strip() != ""]

    print("Setelah cleaning:", len(df))

    df.to_csv("data/processed/cleaned_reviews.csv", index=False)

    print("✅ Data berhasil di-transform & disimpan")
    return df