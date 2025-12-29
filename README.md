import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

# Create login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "student" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Wrong username or password")

# AFTER LOGIN PAGE
else:
    st.title("🎓 Welcome")
    st.write("You have logged in successfully.")
