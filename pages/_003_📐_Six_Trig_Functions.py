import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "six_trig_functions":
        st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "six_trig_functions_page" not in st.session_state:
    st.session_state.six_trig_functions_page = 0

# Set Page Specific Variables
max_page_num = 3
content_dictionary = {
    0: {
        "text_1": "There are six trigonometric functions: sin, cos, tan, csc, sec, cot.  We have already covered the first three.  Now in this section, we will cover the last three.  Each of the last three (csc, sec, cot) are the RECIPROCAL of the RESULT of one of the original three. :point_right:",
        "text_2": "We capitalize the words INVERSE and RESULT because mathematical notation and terminology is notoriously inconsistent from textbook to textbook and so we want to make sure that you do not confuse csc, sec, and cot with another concept we will talk about in the next section arcsine, arccosine, and arctangent.  Let's talk about each word separately.  RECIPROCAL: You probably know that the word reciprocal of 'x' in math means '1/x', right?  That is what we mean here.  RESULT: we mean that you should take 1/sin(x) or 1/cos(x) or 1/tan(x). We'll go through some examples.  For now, just know that sin is associated with cosecant (csc), cosine is associated with secant (sec), and tangent is associated with cotangent (cot) :point_up:.",
        "media": "./gifs/InverseOfResult.gif",
        "media_text": "Relationships Between Functions"},
    1: {
        "text_1": "Let's take a look at cosecant (csc).  Remember the csc = 1/sin.  Check out the picture on the right. :point_right:",
        "text_2": "We already know that the sin of the angle at vertex A (or sin(A)) is equal to the length of the blue side over the length of the red side - or hypotenuse.  Thus, the cosecant of the angle at A (or csc(A)) is simply 1 over that ratio.  Stated another way, the csc(A) equals the ratio of the red side over the blue side.  Similarly, the csc(B) is the red side over the green side.  Finally, the csc(C) is 1.  How do we know this?  Well, we already know that the sine of 90 is 1 and 1/1 is also 1. :smiley:.",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Right Triangle"},
    2: {
        "text_1": "Let's move on to the secant, or sec.  The secant is just 1/cos. :point_right:",
        "text_2": "We know that the cosine of the angle at vertex A equals the green side divided by the red side (the hypotenuse).  So the secant of the angle at A is just the red hypotenuse divided by the green side.  The cosine of the angle at B is the blue side divided by the red side, and so the secant of B is the red side over the blue side.  What about the right angle - the angle at vertex C?  The secant of 90 degress is undefined.  Why?  Because the cosine of 90 is 0 and 1/0 is undefined. :smiley:",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Isoceles Triangle"},
    3: {
        "text_1": "We're almost done with this section - but we need to talk about cotangent (cot)  :point_right:.",
        "text_2": "We know that the tangent of an angle is the ratio of the opposite side side over the adjacent side.  So cotangent must be the adjacent side over the opposite side.  So cot(A) is the green side over the blue side and cot(B) is the blue side over the green side.  What about the right angle?  The cot(C) = cot(90) = undefined.  Why?  Because we know the tangent of 90 degrees is 0 and 1/0 is undefined.",
        "media": "./static/RightTriangle.jpg",
        "media_text": "Right Triangle"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row_col1, second_row_col2 = st.columns([3, 7])  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.six_trig_functions_page = st.session_state.six_trig_functions_page + increment
    if st.session_state.six_trig_functions_page < 0:
        st.session_state.six_trig_functions_page = 0
    if st.session_state.six_trig_functions_page > max_page_num:
        st.session_state.six_trig_functions_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "six_trig_functions"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.six_trig_functions_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.six_trig_functions_page]['text_1']
media = content_dictionary[st.session_state.six_trig_functions_page]['media']
media_text = content_dictionary[st.session_state.six_trig_functions_page]['media_text']

r2c1_container = second_row_col1.container(height=350, border=True)
r2c1_container.write(text_1)

r2c2_container = second_row_col2.container(height=350)
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
    # NOTE THIS DOES NOT WORK YET . . .
    video_file = open(media, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    r2c2_container.write("Invalid Media Type")

with r2c2_container:
    st.write(media_text)

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.six_trig_functions_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.six_trig_functions_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)
