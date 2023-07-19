import streamlit as st

def good():
    if "data" not in st.session_state: 
        st.session_state.data = []

    with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area(label='Message: ', key='input', height=100)
            submit_button = st.form_submit_button(label='Send')

def bad():
    if "input" not in st.session_state: 
        st.session_state.input = []

    with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area(label='Message: ', key='input', height=100)
            submit_button = st.form_submit_button(label='Send')

if __name__ == "__main__":
    # good()
    bad()
