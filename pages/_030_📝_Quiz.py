import streamlit as st
import quiz_dictionaries.right_triangles


# Set Page Specific Variables
content_dictionary = {}
if st.session_state.quiz_state == "importance":
    content_dictionary = quiz_dictionaries.right_triangles.content_dictionary
if st.session_state.quiz_state == "history":
    content_dictionary = "TBD"

# Clear the Session State
st.session_state.quiz_state = "false"

# Render Questions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7", "Question 8", "Question 9", "Question 10"])

with tab1:
    st.header("Question 1")
    answer_1 = st.radio("Choose One:", content_dictionary["1"]["options"])

    # if answer == inner_dict["answer"]:
    #     st.write("Correct!:popcorn:")

with tab2:
    st.header("Question 2")
    answer_2 = st.radio("Choose One:", content_dictionary["2"]["options"])
    if answer_2 == content_dictionary["2"]["answer"]:
        st.write("Correct!:popcorn:")
