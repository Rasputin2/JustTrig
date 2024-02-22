import streamlit as st
import quiz_dictionaries.right_triangles
import quiz_dictionaries.the_unit_circle

# Set Page Specific Variables
content_dictionary = {}
if st.session_state.quiz_state == "right_triangles":
    content_dictionary = quiz_dictionaries.right_triangles.content_dictionary
if st.session_state.quiz_state == "the_unit_circle":
    content_dictionary = quiz_dictionaries.the_unit_circle.content_dictionary

# Clear the Session State
st.session_state.quiz_state = "false"

# Render Questions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7", "Question 8", "Question 9", "Question 10"])

with tab1:
    st.header("Question 1")
    answer_1 = st.radio("Choose One:", content_dictionary["1"]["options"])

    if answer_1 == content_dictionary["1"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["1"]["explanation"])

with tab2:
    st.header("Question 2")
    answer_2 = st.radio("Choose One:", content_dictionary["2"]["options"])
    if answer_2 == content_dictionary["2"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :poop:")
        st.write(content_dictionary["2"]["explanation"])

with tab3:
    st.header("Question 3")
    answer_3 = st.radio("Choose One:", content_dictionary["3"]["options"])
    if answer_3 == content_dictionary["3"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :thumbsdown:")
        st.write(content_dictionary["3"]["explanations"])

with tab4:
    st.header("Question 4")
    answer_4 = st.radio("Choose One:", content_dictionary["4"]["options"])
    if answer_4 == content_dictionary["4"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["3"]["explanations"])

with tab5:
    st.header("Question 5")
    answer_5 = st.radio("Choose One:", content_dictionary["5"]["options"])
    if answer_5 == content_dictionary["5"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["5"]["explanations"])

with tab6:
    st.header("Question 6")
    answer_6 = st.radio("Choose One:", content_dictionary["6"]["options"])
    if answer_6 == content_dictionary["6"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["6"]["explanations"])

with tab7:
    st.header("Question 7")
    answer_7 = st.radio("Choose One:", content_dictionary["7"]["options"])
    if answer_7 == content_dictionary["7"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["7"]["explanations"])

with tab8:
    st.header("Question 8")
    answer_8 = st.radio("Choose One:", content_dictionary["8"]["options"])
    if answer_8 == content_dictionary["8"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["8"]["explanations"])

with tab9:
    st.header("Question 9")
    answer_9 = st.radio("Choose One:", content_dictionary["9"]["options"])
    if answer_9 == content_dictionary["9"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["9"]["explanations"])

with tab10:
    st.header("Question 10")
    answer_10 = st.radio("Choose One:", content_dictionary["10"]["options"])
    if answer_10 == content_dictionary["10"]["answer"]:
        st.write("Correct!:popcorn:")
    else:
        st.write("Sorry. Incorrect. :pirate_flag:")
        st.write(content_dictionary["10"]["explanations"])