import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "more_waves":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "more_waves_page" not in st.session_state:
    st.session_state.more_waves_page = 0

# Set Page Specific Variables
max_page_num = 0
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": f"The above :point_up: may be scary at first, but we'll go through it step-by-step. :smiley:.  Why are we going over this?  Well ... life would be really simple if every real-world phenomenon followed a basic sine wave or cosine wave pattern.  That is, unfortunately, not the case.  Quite often, trig functions are only useful if we manipulate them to respond in more complex ways to different inputs.  There are so many variants of wave functions that we cannot possibly cover them all here, but we will focus on a specific type of wave function where the angle on which the function is operating is expressed in terms of distance (x) and time (t).",
        "media": "./static/WaveFunction.png",
        "media_text": "The Wave Function"},
    1: {
        "text_1": "",
        "text_2": f"It may strike you as odd that tangent can be so high or so low, but think about it this way.  The above diagram :point_up: shows three triangles.  The one on the left is an isoceles right triangle, which means that the tangent of either non-right angle has to be 1. In the middle triangle, we shrink the base, and increase the height.  The tangent of the larger non-right angle ${lx.theta}$ increases, because the ratio of height/base increases.  The right-most triangle shows an even more extreme example.  This can, in theory, go on infinitely, as the base shrinks a little more and the height increases just a little more.  So long as the base has some length (no matter how small), ${lx.theta}$ will have a larger and larger tangent.",
        "media": "./static/TanToInfinity.png",
        "media_text": "Why Tan Increases to Infinity"},
    2: {
        "text_1": "",
        "text_2": f"One important point to realize here is that tangent(${lx.theta}$) equals sine divided by cosine.  The proof of this is shown above.  We'll see this throughout the study of trigonometry where our definition of some fundamental function (sin or cos) can then be manipulated to arrive at a different function (tan).",
        "media": "./gifs/TanIsSinOverCos.gif",
        "media_text": "Tangent = Sine / Cosine"},
    3: {
        "text_1": "",
        "text_2": f"",
        "media": "./gifs/UnitCircleWithPi.gif",
        "media_text": "Unit Circle With Pi"},
    4:  {
        "text_1": "",
        "text_2": f"",
        "media": "./static/UnitCircleRadians.png",
        "media_text": "Unit Circle with Radians"},
    5: {
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
    st.session_state.more_waves_page = st.session_state.more_waves_page + increment
    if st.session_state.more_waves_page < 0:
        st.session_state.more_waves_page = 0
    if st.session_state.more_waves_page > max_page_num:
        st.session_state.more_waves_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "more_waves"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.more_waves_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.more_waves_page]['text_1']
media = content_dictionary[st.session_state.more_waves_page]['media']
media_text = content_dictionary[st.session_state.more_waves_page]['media_text']

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
text_2 = content_dictionary[st.session_state.more_waves_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.more_waves_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)