# https://towardsdatascience.com/streamlit-and-spacy-create-an-app-to-predict-sentiment-and-word-similarities-with-minimal-domain-14085085a5d4

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
text = 'Today is an amazing day!'

st.title('Sentiment app')
user_input = st.text_input("Text", text)
doc = nlp(user_input)

st.write('Polarity:', round(doc._.blob.polarity, 2))
st.write('Subjectivity:', round(doc._.blob.subjectivity, 2)) 