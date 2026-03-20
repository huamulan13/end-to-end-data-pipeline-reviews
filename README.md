![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

# 📌 End-to-End Data Pipeline for Customer Review Processing

---

## 🚀 Overview
This project demonstrates a lightweight **end-to-end data pipeline** for processing customer reviews, from raw data ingestion to structured storage and visualization.

💡 This project highlights how raw data can be transformed into actionable insights using a structured pipeline.

---

## ⚙️ Features
- 📥 Data extraction from raw CSV files  
- 🔄 Data transformation (cleaning, sentiment analysis, feature engineering)  
- 💾 Data storage using SQLite  
- 🔍 SQL-based querying for analysis  
- 📊 Interactive dashboard visualization  
- 📝 Logging system for pipeline monitoring  

---

## 🏗️ Architecture
Raw Data → Extract → Transform → Load → SQLite → Dashboard

---

## 🧠 Key Insights
- ❌ Negative sentiment often linked to performance issues (error, lambat)  
- 🔁 Pipeline ensures repeatable & structured processing  

---

## 🛠️ Tech Stack
- 🐍 Python  
- 🐼 Pandas  
- 🗄️ SQLite  
- 📊 Streamlit  

---

## 📂 Project Structure

```bash
data/                # mentah & processed data
  mentah/
  processed/
src/                 # pipeline modules
  extract.py
  transform.py
  load.py
pipeline.py          # main pipeline runner
app.py               # Streamlit dashboard
```

---

## 📸 Demo
## 📊 Dashboard View
<img width="1915" height="916" alt="image" src="https://github.com/user-attachments/assets/7252bc13-8039-4186-abb5-3830ad940bd7" />

## 📈 Visualization
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/75fcf56b-48d4-4dcd-b3f3-1bfdedb75da5" />

---

## ▶️ How to Run

```bash
python pipeline.py
streamlit run app.py
```