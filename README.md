# 📰 News_Pulse_Analyzer

**News_Pulse_Analyzer** is an advanced news analytics platform built with Python and Streamlit. It fetches news from multiple APIs, performs sentiment analysis, named entity recognition, topic modeling, trend detection, and provides an interactive AI chatbot for querying insights.  

---

## 🚀 Features

- Fetches news from **NewsAPI** (global) and **NewsData.io** (India-focused) based on language.
- **Language-aware fetching**:
  - Indian languages → NewsData.io  
  - Foreign languages → NewsAPI  
  - English/Hindi → Both APIs combined  
- **Text Preprocessing**: Clean, tokenize, and lemmatize news articles.
- **Sentiment Analysis** using **Hugging Face transformers**.
- **Named Entity Recognition (NER)** with **spaCy**.
- **Topic Modeling** using **BERTopic**.
- **Trend Analysis**: Detect spikes, dips, and trending topics.
- **Cross-Sector Correlation** between news categories.
- **Interactive Visualizations**: Pie charts, bar charts, word clouds, and timelines.
- **AI Chatbot Assistant** with **Google Gemini AI**.
- **Streamlit Dashboard** for user-friendly interaction.

---

## 📂 Project Structure

```bash
News_Pulse_Analyzer/
│
├─ modules/
│ ├─ login.py
│ ├─ news_fetcher.py
│ ├─ preprocessing.py
│ ├─ sentiment_analysis.py
│ ├─ ner_analysis.py
│ ├─ topic_modeling.py
│ ├─ trend_analysis.py
│ ├─ cross_sector.py
│ └─ chatbot_integration.py
│
├─ utils/
│ └─ visualization.py
│
├─ data/
│ └─ news_cache.json
│
├─ config.py
├─ app.py
├─ requirements.txt
└─ .gitignore
```

---

## 💻 Technologies Used

- **Python 3.9+**  
- **Streamlit** – Web app and dashboard  
- **Pandas & Numpy** – Data processing  
- **Requests** – API calls  
- **NLTK & spaCy** – Text preprocessing and NER  
- **Transformers (Hugging Face)** – Sentiment analysis  
- **BERTopic** – Topic modeling  
- **Matplotlib & Plotly** – Visualizations  
- **WordCloud** – Text visualization  
- **Google Generative AI (Gemini)** – Chatbot  

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pratham-Modi/News_Pulse_Analyzer.git
cd News_Pulse_Analyzer
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file in the root directory with your API keys

```bash
NEWS_API_KEY=<your-newsapi-key>
NEWSDATAIO_API_KEY=<your-newsdataio-key>
GOOGLE_API_KEY=<your-google-gemini-key>
```

### 5. Running the App

```bash
streamlit run app.py
```

---

## 📝 Usage

- **Login Page** – Enter username, email, and password.
- **Sidebar Options** – Select news language and category.
- **Fetch News** – Retrieve articles from selected sources.
- **News Display** – View latest articles with sentiment, entities, and topics.
- **Visualizations** – Interactive charts, word clouds, and timeline.
- **Chatbot** – Ask questions or summarize news in natural language.

---**

## 🌐 Supported Languages

**NewsAPI**: en, hi, ar, de, es, fr, he, it, nl, no, pt, ru, sv, ud, zh
**NewsData.io**: en, hi, bn, gu, kn, ml, mr, or, pa, ta, te, ur

---

## 📊 Visualizations

- Sentiment Distribution Pie Chart
- Article Counts per Category
- Word Cloud of Headlines & Content
- Timeline of News Activity

---

## 📈 Future Improvements

- Add support for additional languages and news APIs
- Real-time notifications for trending topics
- Advanced AI summarization of topics
- Personalized news recommendations

---

## ⚠️ Notes

- Ensure .env contains valid API keys.
- Cached news (data/news_cache.json) reduces API calls.
- Streamlit may require extra setup for some visualization libraries.

---

## 👤 Author

**Pratham Modi**  

- GitHub: [https://github.com/Pratham-Modi](https://github.com/Pratham-Modi)  
- LinkedIn: [https://www.linkedin.com/pratham-modi](https://www.linkedin.com/in/pratham-modi-94a965253/)

---
