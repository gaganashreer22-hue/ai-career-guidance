import streamlit as st

st.title("🔐 Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "student" and password == "1234":
        st.success("Login successful 🎉")

        st.header("🎓 Career Guidance System")
        st.write("Type ANY career you want to become.")

        career = st.text_input("Enter your career (Doctor, Pilot, Designer, etc.)")

        if career:
            st.write("You selected the career:")
            st.write(career)

    else:
        st.error("Invalid login ❌")
