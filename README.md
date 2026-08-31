# 🚀 QualiAI - AI Powered Data Quality Assessment System

## 📌 Overview

QualiAI is an AI-powered web application built using Python and Streamlit that analyzes dataset quality through data profiling, validation, anomaly detection, and AI-driven recommendations.

The application helps users identify missing values, duplicate records, anomalies, and overall dataset quality while providing downloadable reports and cleaned datasets.

---

## ✨ Features

- 📂 Upload CSV Dataset
- 📊 Data Profiling
- ✅ Data Validation
- ⭐ Data Quality Score
- 🤖 Dataset Quality Prediction
- 🧹 Smart Data Cleaning
- 🔍 Isolation Forest Anomaly Detection
- 📈 Interactive Plotly Visualizations
- 📄 PDF Report Generation
- 💾 Download Cleaned Dataset

---

## 🧠 Machine Learning Algorithm

**Isolation Forest**

Isolation Forest is used to detect anomalous records in the uploaded dataset.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- ReportLab

---

## 📁 Project Structure

```
AI_Data_Quality_System/
│
├── app.py
├── README.md
├── requirements.txt
├── pages/
├── utils/
├── datasets/
├── assets/
└── screenshots/
```

---

## ⚙ Installation

```bash
git clone https://github.com/yourusername/AI_Data_Quality_System.git

cd AI_Data_Quality_System

pip install -r requirements.txt

streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots of:

- Dashboard
- Data Profiling
- Validation
- Anomaly Detection
- PDF Report

inside the `screenshots` folder.

---

## 👨‍💻 Author

**Shubham Warhade**


flowchart TD

    A[Raw Dataset] --> B[Profiling]
    B --> C[Validation]
    C --> D[Anomaly Detection]
    D --> E[Quality Metrics]
    E --> F[Overall Quality Score]

    E --> G[Recommendations]
    E --> H[Visualizations]
    E --> I[RAG Context]

    I --> J[Retriever]
    J --> K[Knowledge Base]
    K --> L[LLM]
    L --> M[AI Assistant Response]
