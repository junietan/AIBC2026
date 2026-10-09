import streamlit as st
from utility import check_password

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()
    
st.write("let me tell you a secret... ", st.secrets["secret"])