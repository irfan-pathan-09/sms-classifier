import streamlit as st
import joblib
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sklearn

# nltk fix
import nltk
import os

nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(nltk_data_path)

nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)












stemmer = PorterStemmer()

tfidf = joblib.load('vectorizer.pkl')
model = joblib.load('model.pkl')


def transform_sms(input_sms):
    input_sms = input_sms.lower()
    input_sms = nltk.word_tokenize(input_sms)
    y = []

    for i in input_sms:
        if i.isalnum() and i  not in stopwords.words('english'):
            y.append(stemmer.stem(i))

    return " ".join(y)
    
st.title("Email/SMS Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    transform_sms = transform_sms(input_sms)

    vectorized_input = tfidf.transform([transform_sms])

    result = model.predict(vectorized_input)[0]

    if(result):
        st.header("Spam")
    if(not result):
        st.header("not spam")