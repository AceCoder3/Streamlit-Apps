import streamlit as st
import openai

openai.api_key = "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"




st.title("Code Translater")
model_engine = "text-davinci-002"
prompt=st.text_area("Translate Your Code From One language to another ")
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=60,
    n=1,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    
    
)

st.caption(response["choices"][0].text)

    
    


