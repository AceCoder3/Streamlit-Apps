import streamlit as st
import openai

openai.api_key = "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"


st.title("Smart")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=st.text_input("Enter Your Question"),
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

st.caption(response["choices"][0].text)
