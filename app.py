import streamlit as st

st.title("🔐 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "student" and password == "1234":
        st.success("Login successful 🎉")
        st.write("🎓 Welcome to the Career Guidance Website")
    else:
        st.error("Invalid login ❌")
