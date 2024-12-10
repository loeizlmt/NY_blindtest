import streamlit as st

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with open('main.html') as f:
    html = f.read()

st.write("ceci est un buzzer : ")

st.markdown(f'<html>{html}</html>', unsafe_allow_html=True)

