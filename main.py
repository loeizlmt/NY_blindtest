import streamlit as st

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.write("Ceci est un buzzer : ")

st.markdown(""" <center><div onclick="buzzed()" id='balloon' class="balloon"></div></center>""", unsafe_allow_html=True)


