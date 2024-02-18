import streamlit as st

first_row_col1, first_row_col2 = st.columns([7, 3], gap="small")
second_row_col1, second_row_col2 = st.columns([7, 3], gap="small")
third_row = st.columns(1)

# Entire Script Runs Upon Page Refresh
if "page" not in st.session_state:
    st.session_state.page = 0
    max_pages = 3

# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.page = st.session_state.page + increment
    if st.session_state.page < 0:
        st.session_state.page = 0
    if st.session_state.page > max_pages:
        st.session_state = 0

def render_col1(text):
    st.write("Hello")


def render_col2(media):
    st.write("World")


with first_row_col1.container():
    st.write(st.session_state.page)

button1 = second_row_col1.button('Prev', on_click=set_stage, args=[-1])
button2 = second_row_col2.button('Next', on_click=set_stage, args=[1])
if st.session_state.page == 5:
    st.switch_page("pages/_30_📝_Quiz.py_")
