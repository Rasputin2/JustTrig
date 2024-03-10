import streamlit as st
import quiz_dictionaries.right_triangles
import quiz_dictionaries.inverse_functions
import quiz_dictionaries.six_trig_functions
import quiz_dictionaries.the_unit_circle
import quiz_dictionaries.the_sin_wave
import quiz_dictionaries.the_cos_wave
import quiz_dictionaries.the_tan_wave
import quiz_dictionaries.more_waves
import quiz_dictionaries.trig_identities_pt1

st.set_page_config("wide")

# Set Page Specific Variables
content_dictionary = {}
if "quiz_state" in st.session_state:
    if st.session_state.quiz_state == "right_triangles":
        content_dictionary = quiz_dictionaries.right_triangles.content_dictionary
    elif st.session_state.quiz_state == "six_trig_functions":
        content_dictionary = quiz_dictionaries.six_trig_functions.content_dictionary
    elif st.session_state.quiz_state == "inverse_functions":
        content_dictionary = quiz_dictionaries.inverse_functions.content_dictionary
    elif st.session_state.quiz_state == "the_unit_circle":
        content_dictionary = quiz_dictionaries.the_unit_circle.content_dictionary
    elif st.session_state.quiz_state == "the_sin_wave":
        content_dictionary = quiz_dictionaries.the_sin_wave.content_dictionary
    elif st.session_state.quiz_state == "the_cos_wave":
        content_dictionary = quiz_dictionaries.the_cos_wave.content_dictionary
    elif st.session_state.quiz_state == "the_tan_wave":
        content_dictionary = quiz_dictionaries.the_tan_wave.content_dictionary
    elif st.session_state.quiz_state == "more_waves":
        content_dictionary = quiz_dictionaries.more_waves.content_dictionary
    elif st.session_state.quiz_state == "trig_identities_pt1":
        content_dictionary = quiz_dictionaries.trig_identities_pt1.content_dictionary
    else:
        st.switch_page("Home.py")
else:
    st.switch_page("Home.py")

# Render Questions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
    ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"])
tab_dictionary = {
    1: tab1,
    2: tab2,
    3: tab3,
    4: tab4,
    5: tab5,
    6: tab6,
    7: tab7,
    8: tab8,
    9: tab9,
    10: tab10
}


# Function to Check Answers
def check_answers(question_num, feedback_container):
    session_state_key = "Q" + str(question_num)
    answer = content_dictionary[question_num]["answer"]
    explanation = content_dictionary[question_num]["explanation"]

    if session_state_key in st.session_state:
        if st.session_state[session_state_key] == answer:
            with tab_dictionary[question_num]:
                feedback_container.write("Correct!:popcorn:")
        else:
            with tab_dictionary[question_num]:
                feedback_container.write("Sorry. Incorrect. :poop:")
                feedback_container.write(explanation)


with tab1:
    st.header("Question 1")
    st.image(content_dictionary[1]["media"])
    st.write(content_dictionary[1]["question"])
    answer_1 = st.radio("Choose One:", content_dictionary[1]["options"], index=None, key="Q1")
    feedback_1 = st.container()
    submit_1 = st.button(label="Submit", key=1)
    if submit_1:
        check_answers(1, feedback_1)


with tab2:
    st.header("Question 2")
    st.image(content_dictionary[2]["media"])
    st.write(content_dictionary[2]["question"])
    answer_2 = st.radio("Choose One:", content_dictionary[2]["options"], index=None, key="Q2")
    feedback_2 = st.container()
    submit_2 = st.button(label="Submit", key=2)
    if submit_2:
        check_answers(2, feedback_2)

with tab3:
    st.header("Question 3")
    st.image(content_dictionary[3]["media"])
    st.write(content_dictionary[3]["question"])
    answer_3 = st.radio("Choose One:", content_dictionary[3]["options"], index=None, key="Q3")
    feedback_3 = st.container()
    submit_3 = st.button(label="Submit", key=3)
    if submit_3:
        check_answers(3, feedback_3)

with tab4:
    st.header("Question 4")
    st.image(content_dictionary[4]["media"])
    st.write(content_dictionary[4]["question"])
    answer_4 = st.radio("Choose One:", content_dictionary[4]["options"], index=None, key="Q4")
    feedback_4 = st.container()
    submit_4 = st.button(label="Submit", key=4)
    if submit_4:
        check_answers(4, feedback_4)

with tab5:
    st.header("Question 5")
    st.image(content_dictionary[5]["media"])
    st.write(content_dictionary[5]["question"])
    answer_5 = st.radio("Choose One:", content_dictionary[5]["options"], index=None, key="Q5")
    feedback_5 = st.container()
    submit_5 = st.button(label="Submit", key=5)
    if submit_5:
        check_answers(5, feedback_5)

with tab6:
    st.header("Question 6")
    st.image(content_dictionary[6]["media"])
    st.write(content_dictionary[6]["question"])
    answer_6 = st.radio("Choose One:", content_dictionary[6]["options"], index=None, key="Q6")
    feedback_6 = st.container()
    submit_6 = st.button(label="Submit", key=6)
    if submit_6:
        check_answers(6, feedback_6)

with tab7:
    st.header("Question 7")
    st.image(content_dictionary[7]["media"])
    st.write(content_dictionary[7]["question"])
    answer_7 = st.radio("Choose One:", content_dictionary[7]["options"], index=None, key="Q7")
    feedback_7 = st.container()
    submit_7 = st.button(label="Submit", key=7)
    if submit_7:
        check_answers(7, feedback_7)

with tab8:
    st.header("Question 8")
    st.image(content_dictionary[8]["media"])
    st.write(content_dictionary[8]["question"])
    answer_8 = st.radio("Choose One:", content_dictionary[8]["options"], index=None, key="Q8")
    feedback_8 = st.container()
    submit_8 = st.button(label="Submit", key=8)
    if submit_8:
        check_answers(8, feedback_8)


with tab9:
    st.header("Question 9")
    st.image(content_dictionary[9]["media"])
    st.write(content_dictionary[9]["question"])
    answer_9 = st.radio("Choose One:", content_dictionary[9]["options"], index=None, key="Q9")
    feedback_9 = st.container()
    submit_9 = st.button(label="Submit", key=9)
    if submit_9:
        check_answers(9, feedback_9)

with tab10:
    st.header("Question 10")
    st.image(content_dictionary[10]["media"])
    st.write(content_dictionary[10]["question"])
    answer_10 = st.radio("Choose One:", content_dictionary[10]["options"], index=None, key="Q10")
    feedback_10 = st.container()
    submit_10 = st.button(label="Submit", key=10)
    if submit_10:
        check_answers(10, feedback_10)