import streamlit as st
import openai

openai.api_key = "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"




st.title("Picture Thing")
model_engine = "text-davinci-002"
prompt=st.text_area("Generate the Image")
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

st.image(image_url)




