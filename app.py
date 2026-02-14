import streamlit as st
import joblib
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sklearn
import os

# nltk files are stored in the nltk_data folder in the current working directory
# Create nltk_data folder
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_path, exist_ok=True)

# Tell nltk to use this folder
nltk.data.path.append(nltk_data_path)

# Download required resources
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

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