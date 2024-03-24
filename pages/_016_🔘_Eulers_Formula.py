import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "eulers_formula":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "eulers_formula" not in st.session_state:
    st.session_state.eulers_formula = 0

# Set Page Specific Variables
max_page_num = 2
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": "As we've alluded to many times before now, the above formula, known as Euler's formula, is one of the most important formulas in mathematics. But how did Leonard Euler discover it? First, we have to remember that sine and cosine are mathematical 'functions', which means that for any input (x), there is a unique value f(x). Second, every new concept in math builds on previously proven concepts (often referred to as axioms). Here the previous concept is that every 'function' that is defined at a given point may be represented by something called a Taylor Series Expansion at that point.",
        "media": "./gifs/TaylorSeries.gif",
        "media_text": "Taylor Series"},
    1: {
        "text_1": "",
        "text_2": "The above animation illustrates how sine relates to Euler's number.",
        "media": "./gifs/SinOmegaT.gif",
        "media_text": "Using e To Find Sine"
        },
    2: {
        "text_1": "",
        "text_2": "The above animation illustrates how cosine relates to Euler's number.",
        "media": "./gifs/CosOmegaT.gif",
        "media_text": "Using e To Find Cosine"
        },
    3: {
        "text_1": "",
        "text_2": "",
        "media": "./gifs/CosOmegaT.gif",
        "media_text": "Using e to Find Cosine"},
    4: {
        "text_1": "",
        "text_2": " ",
        "media": "./static/SinFunctionPlot.png",
        "media_text": "Sine Function Plot"},
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
    st.session_state.eulers_formula = st.session_state.eulers_formula + increment
    if st.session_state.eulers_formula < 0:
        st.session_state.eulers_formula = 0
    if st.session_state.eulers_formula > max_page_num:
        st.session_state.eulers_formula = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "eulers_formula"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.eulers_formula) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.eulers_formula]['text_1']
media = content_dictionary[st.session_state.eulers_formula]['media']
media_text = content_dictionary[st.session_state.eulers_formula]['media_text']

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
text_2 = content_dictionary[st.session_state.eulers_formula]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.eulers_formula == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)