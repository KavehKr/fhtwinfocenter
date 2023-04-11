import streamlit as st
import requests

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.title('Welcome to the application for FHTW Info-Center')
    st.write('text-davinci-003 is more powerful and accurate but text-curie-001 is faster')
    model_type = st.sidebar.selectbox('Which model do you want to use?',['text-davinci-003','text-curie-001'])
    tokens = st.sidebar.selectbox('How many tokens for response?',[400,500,600,300,200,100,50])
    email = st.text_input('please type your email text to the FH Technikum Wien Info-center:')
    if len(email)>10:
        url = "https://infocenterfhtw22023.azurewebsites.net/api/HttpTrigger1?name="+email+"&type="+model_type+"&n_tokens="+str(tokens)
        result = requests.get(url=url)
        st.write(result.text)
    else:
        st.write('waiting for input!')