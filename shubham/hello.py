import streamlit as st

st.header('This is my first Web Application')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

code = '''def cat():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
agree = st.checkbox('I am a great programmer')

if agree:
    st.write('I am ')