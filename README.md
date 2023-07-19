This repository is for bug report for https://github.com/streamlit/streamlit/issues/7037.
# streamlit-sample
### Summary

st.session_state causes an error when it has a value named "input".
```
TypeError: bad argument type for built-in operation
```
Probably it is a special value used in advance.

### Reproducible Code Example

```Python
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
```


### Steps To Reproduce

1. Execute the bad() function I get the error I want to report.
2. Execute the good() function, there is no problem.

### Expected Behavior

When st.session_state has a value named "input", it should behave the same as when it has other values (e.g., "data").

### Current Behavior

Error message:
```
TypeError: bad argument type for built-in operation
```
