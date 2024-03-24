import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "eulers_number":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "eulers_number" not in st.session_state:
    st.session_state.eulers_number = 0

# Set Page Specific Variables
max_page_num = 1
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": "A more comprehensive history of Euler's number or 'e' can be found in the book *e:The Story of a Number* by Eli Maor. For our purposes, I want to go back to 1683, and a guy named Jacob Bernoulli, who was tasked with coming up with a formula for infinite compounding of bank interest. As you probably know, when you buy a car or a house on credit, you pay interest. While the interest *rate* is very important, the manner in which the interest *compounds* is just as important. For example, if I agreed on January 1st to pay you cash at the end of year, would you rather have me pay you $100 plus: (A) 3% compounded quarterly; (B) 6% compounded semi-annually; or (C) 9% compounded annually.  The answer is (A), which yields $112.56. The question the Italian banking houses posed to Bernoulli back in the Renaissance was how to determine what the amount would be if interest literally compounded constantly - similar to interest compounding every nanosecond of every day from January 1st to December 31st. That number can be derived by taking the limit of the expression in (i) as n approaches infinity, or by recognizing, as Euler did, that e can also be represented as a series shown in (ii). Either way, you get a number approximating (but not equaling) 2.718. Like pi, Euler's number is irrational, so it can only be approximated to a chosen number of decimal places.",
        "media": "./static/EulersNumber.png",
        "media_text": "Euler's Number"
    },
    1: {
        "text_1": "",
        "text_2": "The reason Euler's number is so important is that most natural phenomena occur constantly, not at discrete units of time. For example, ",
        "media": "./gifs/CosOmegaT.gif",
        "media_text": "Using e to Find Cosine"
    },
    2: {
        "text_1": "",
        "text_2": " ",
        "media": "./static/SinFunctionPlot.png",
        "media_text": "Sine Function Plot"
    },
    3: {
        "text_1": "",
        "text_2": "",
        "media": "./gifs/SinIsAFunction.gif",
        "media_text": "Sine Is a Function"
    },
    4: {
        "text_1": "",
        "text_2": f"",
        "media": "./gifs/UnitCircleWithPi.gif",
        "media_text": "Unit Circle With Pi"},
    5:  {
        "text_1": "",
        "text_2": f"",
        "media": "./static/UnitCircleRadians.png",
        "media_text": "Unit Circle with Radians"},
    6: {
        "text_1": "",
        "text_2": f"",
        "media": "./gifs/UnitCircleWithinLargerCircle.gif",
        "media_text": "Unit Circle within Larger Circle"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row = st.columns(1)  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.eulers_number = st.session_state.eulers_number + increment
    if st.session_state.eulers_number < 0:
        st.session_state.eulers_number = 0
    if st.session_state.eulers_number > max_page_num:
        st.session_state.eulers_number = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "eulers_number"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.eulers_number) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.eulers_number]['text_1']
media = content_dictionary[st.session_state.eulers_number]['media']
media_text = content_dictionary[st.session_state.eulers_number]['media_text']

r2c2_container = second_row[0].container()
if any(media[-4] in x for x in [".pmg", ".jpg", "jpeg", ".gif"]):
    file_ = open(media, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    r2c2_container.markdown(
        f'<img src="data:image/gif;base64,{data_url}">',
        unsafe_allow_html=True,
    )
elif media[-4] == ".mp4":
    video_file = open(media, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    r2c2_container.write("Invalid Media Type")

with r2c2_container:
    st.write(media_text)

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.eulers_number]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.eulers_number == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)