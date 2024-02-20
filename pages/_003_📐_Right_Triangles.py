import base64
import streamlit as st

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "right_triangles":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "right_triangle_page" not in st.session_state:
    st.session_state.right_triangle_page = 0

# Set Page Specific Variables
max_page_num = 3
content_dictionary = {
    0: {
        "text_1": "The term Trigonometry comes from the combination of two Greek words.  The first is trigonon, meaning three (3) angles.  This is how we get the word 'tri-angle'.  The second word is metron, meaning 'to measure'.  So, Trigonometry is all about measuring triangles.",
        "text_2": "We know that every triangle has to have three sides and three angles - right?  We also know those angles have to add up to 180 degrees.  But triangles come in lots of different shapes and sizes.  Some triangles with specific angles or combinations of angles have unique properties, and so we give them special names. Above you see an 'equilateral' triangle. All three of it's sides have the exact same length and each of it's angles is precisely 60 degrees.  Each of the dots you see are referred to (for every triangle, not just equilateral triangles) as a 'vertex', the plural of which is 'vertices'. Although the length of each side may change, an equilateral triangle's sides will all be of equal length and each angle must be 60 degrees.",
        "media": "./static/EquilateralTriangle.png",
        "media_text": "Equilateral Triangle"},
    1: {
        "text_1": "Another type of triangle is the 'isoceles' triangle.  One permutation of an isocoles triangle is shown on the right.",
        "text_2": "What makes this triangle 'isoceles'?  Unlike the equilateral triangle, it only has two equal sides (the side between the red and green vertices and the side between the blue and green vertices).  We know, then, that the two angles opposite those sides are identical.  In this case, the two identical angles (the one at the red dot and the blue vertices) are 75 degrees.  That is not always the case.  The two angles could each have been 20 degrees or 30 degrees.  All we know is that if it is an isoceles, then two of the three angles must be equal.  But this is still a lot of information.  For example, given that the angles have to sum to 180 degrees (because the three angles of a triangle always sum to 180 degrees), and we know the angle at the red vertex equals 75 degrees, you can immediately figure out the other angles.  You know the angle at the blue vertex is also 75 degrees and the angle at the green vertex must be 180 - 75 - 75 = 30 degrees.",
        "media": "./static/IsocelesTriangle.png",
        "media_text": "Isoceles Triangle"},
    2: {
        "text_1": "Perhaps the most important triangle, however, is the so-called 'right' triangle, shown here.  The side colored RED is what we refer to as the Hypotenuse.  Only right triangles have a side called Hypotenuse.  In this case, two sides happen to be equal, so this triangle is ALSO considered an isoceles triangle.  But that need not be the case.",
        "text_2": "What makes a triangle a 'right' triangle?  The existence of a 'right' angle - meaning an angle with 90 degrees.  Whenever you see a square :square: superimposed on a vertex like the red square shown here, you know you have a 'right' angle - an angle at 90 degrees :angle:.  It's opposite side is always the hypotenuse.",
        "media": "./static/RightTriangle.jpg",
        "media_text": "Right Triangle"},
    3: {
        "text_1": "The reason 'right' triangles are so important is that they are the only triangles that the Pythagorean Theorem applies to. You have likely seen this theorem before ",
        "text_2": "What makes a triangle a 'right' triangle?  The existence of a 'right' angle - meaning an angle with 90 degrees.  Whenever you see a square :square: superimposed on a vertex like the red square shown here, you know you have a 'right' angle - an angle at 90 degrees :angle:.  It's opposite side is always the hypotenuse.",
        "media": "./static/PythagoreanTheorem.jpg",
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
    st.session_state.right_triangle_page = st.session_state.right_triangle_page + increment
    if st.session_state.right_triangle_page < 0:
        st.session_state.right_triangle_page = 0
    if st.session_state.right_triangle_page > max_page_num:
        st.session_state.right_triangle_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "right_triangles"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.right_triangle_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.right_triangle_page]['text_1']
media = content_dictionary[st.session_state.right_triangle_page]['media']
media_text = content_dictionary[st.session_state.right_triangle_page]['media_text']

r2c1_container = second_row_col1.container(height=350, border=True)
r2c1_container.write(text_1)

r2c2_container = second_row_col2.container()

file_ = open(media, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
r2c2_container.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="equilateral_triangle">',
    unsafe_allow_html=True,
)
with r2c2_container:
    st.write(media_text)

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.right_triangle_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.right_triangle_page == 2:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)