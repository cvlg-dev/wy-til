import streamlit as st
import requests

st.header("문장 감성분석기")

text = st.text_input(label='input text')

input_dict = {"text": text}

if st.button(label='submit'):

    with st.spinner("Model running..."):
        headers = {
            "accept" : "application/json",
            "Content-Type": "application/json"
        }
        url = "https://kobert-senti-bentoml-jhqbnr66na-de.a.run.app/predict"
        response = requests.post(url,
                      headers=headers,
                      json=input_dict)
    st.markdown("* * *")
    st.subheader("분석 결과")
    if response.text == "negative":
        st.markdown("부정적 :rage:")
    else:
        st.markdown("긍정적 :smiley:")