

import streamlit as st
import hashlib

message=st.text_input("Enter Message")
result=None
result=hashlib.sha384(message.encode())
st.caption("Hashed Message is:")
st.caption(result.hexdigest())
    



