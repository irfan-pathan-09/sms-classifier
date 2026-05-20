# 📧 Email/SMS Spam Classifier

A Machine Learning app that detects whether a message is **Spam** or **Not Spam** using Natural Language Processing (NLP) and a trained classifier.

## 🌐 Live Demo

https://sms-classifier-irfan09.onrender.com

---

## 🚀 Features

- Classifies SMS and email-style messages
- Uses TF-IDF with a trained ML model
- Simple Streamlit web interface
- Includes sample dataset and notebook for training

---

## 🧠 Machine Learning Pipeline

1. Load and clean the `spam.csv` dataset
2. Preprocess text (lowercase, tokenize, remove stopwords, stem)
3. Extract features with `TfidfVectorizer`
4. Train a classifier and save the pipeline artifacts
5. Load saved `model.pkl` and `vectorizer.pkl` in `app.py`

---

## 🛠️ Tech Stack

- Python
- scikit-learn
- NLTK
- Streamlit
- NumPy

---

## 📂 Project Structure

sms spam classifier/
│
├── `.gitignore`
├── `.streamlit/`
├── `app.py`
├── `model.pkl`
├── `requirements.txt`
├── `README.md`
├── `sms-spam-detection.ipynb`
├── `spam.csv`
├── `vectorizer.pkl`
└── `.venv/` (local virtual environment, not tracked)

> Note: `.venv/` is included in the workspace but should typically be excluded from version control.

---

## 📥 Install and run locally

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧪 What’s included

- `app.py` — Streamlit app for prediction
- `spam.csv` — SMS spam dataset
- `sms-spam-detection.ipynb` — notebook for data exploration and training
- `model.pkl` — trained classifier model
- `vectorizer.pkl` — saved TF-IDF vectorizer

---

## 💡 Improvements you can add

- Add `train.py` to retrain the model from `spam.csv`
- Use a `sklearn.pipeline.Pipeline` for preprocessing + modeling
- Cache model loading in Streamlit with `@st.cache_resource`
- Add evaluation metrics like accuracy, precision, and recall

---

## 👨‍💻 Author

Irfan Khan Pathan

GitHub: https://github.com/irfan-pathan-09

LinkedIn: https://www.linkedin.com/in/irfan-khan-b042b7305

---

## ⭐ Support

If you like this project, please consider starring the repository!
