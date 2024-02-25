import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "inverse_functions":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "inverse_functions_page" not in st.session_state:
    st.session_state.inverse_functions_page = 0

# Set Page Specific Variables
max_page_num = 2
content_dictionary = {
    0: {
        "text_1": "Now we're going to talk about the inverse trigonometric functions.  Remember earlier when we said that sin, cos, tan etc. are trigonometric FUNCTIONS.  Like any mathematical function, you put something into it and you get something out of it.  But this works the other way too! Check out the video on the right to how the functions relate to their inverse. :point_right:",
        "text_2": "Some functions (not all) have an 'inverse'.  With an inverse, you can reverse the process and take the output, feed it to the inverse function, and get back the input.  Each one of the six (6) trig functions happens to have an inverse.  ",
        "media": "./gifs/InverseFunctions.gif",
        "media_text": "Inverse Trig Functions"},
    1: {
        "text_1": "So, remember that with a regular trigonometric function, we feed it the measure of an angle (like the size of Angle A or Angle B) and we get back a ratio of the lengths of certain sides of the triangle.",
        "text_2": "What we do with inverse functions is we feed the ratio of the lengths of sides and we get back the measure of the angle.  It's just the reverse of the process.  So if the sine of 30 degrees equals 1/2, then the arcsine of 1/2 equals 30 degrees.  If the cosine of 60 degrees is 1/2 then the arccos of 1/2 is 60 degrees.  Easy, right?",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Right Triangle"},
    2: {
        "text_1": "Now, before we end this section, we need to focus on notation.  As noted in a previous section, math textbooks are notoriously inconsistent in their notation.  This is one place where that can cause a significant amount of confusion...",
        "text_2": f"When you see a variable raised to the power of a negative exponent like ${lx.reciprocal_x_exponent}$ that means the same thing as 1/x.  Thus, when you see ${lx.reciprocal_sin_exponent}$ it should mean the same thing as 1/sin or cosecant.  But sometimes people will use the notation ${lx.reciprocal_sin_exponent}$ when they really mean arcsin.  The same goes for arccos and arctan etc.  In all events, when you mean arcsin or arccos etc. you should say that and not use the ${lx.reciprocal_sin_exponent}$ notation.",
        "media": "./static/RightTriangle.jpg",
        "media_text": "Right Triangle"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row_col1, second_row_col2 = st.columns([4, 6])  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.inverse_functions_page = st.session_state.inverse_functions_page + increment
    if st.session_state.inverse_functions_page < 0:
        st.session_state.inverse_functions_page = 0
    if st.session_state.inverse_functions_page > max_page_num:
        st.session_state.inverse_functions_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "inverse_functions"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.inverse_functions_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.inverse_functions_page]['text_1']
media = content_dictionary[st.session_state.inverse_functions_page]['media']
media_text = content_dictionary[st.session_state.inverse_functions_page]['media_text']

r2c1_container = second_row_col1.container(height=350, border=True)
r2c1_container.write(text_1)

r2c2_container = second_row_col2.container()
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
    # To Come
    print("Hello")
else:
    r2c2_container.write("Invalid Media Type")

with r2c2_container:
    st.write(media_text)

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.inverse_functions_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.inverse_functions_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)
