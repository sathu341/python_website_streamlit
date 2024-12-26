import streamlit as st

st.title("welcome to camerinfolks")

name=st.text_input("Enter your name") 
course=st.selectbox("select your course",("","python","java","mern"))
button=st.button("Done")
if button:
  st.markdown(f""" Name:{name},Selected Course{course}""")

