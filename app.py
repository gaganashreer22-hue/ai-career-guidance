import streamlit as st

st.set_page_config(page_title="Login Page", page_icon="🔐")

# Create login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🔐 Login Page")

if st.session_state.logged_in == False:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "student" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Wrong username or password")

else:
    st.title("🎓 Welcome")
    st.write("Login successful. You are inside the website.")
