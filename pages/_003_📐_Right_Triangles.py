import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "right_triangles":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "right_triangle_page" not in st.session_state:
    st.session_state.right_triangle_page = 0

# Set Page Specific Variables
max_page_num = 10
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
        "text_1": "The most important type of triangle, however, is the so-called 'right' triangle, shown here.  The side colored RED is what we refer to as the Hypotenuse.  Only right triangles have a side called Hypotenuse.  In this case, two sides happen to be equal, so this triangle is ALSO considered an isoceles triangle.  But that need not be the case.  A right triangle may be an isoceles triangle if two of its angles are equal and two of its sides are equal.  If it is not an isoceles, we call it a 'scalene' triangle (i.e., a triangle where no angles are the same and no sides are the same length).",
        "text_2": "What makes a triangle a 'right' triangle?  The existence of a 'right' angle - meaning an angle with 90 degrees.  Whenever you see a square :square: superimposed on a vertex like the red square shown here, you know you have a 'right' angle - an angle at 90 degrees :angle:.  It's opposite side is always the hypotenuse.",
        "media": "./static/RightTriangle.jpg",
        "media_text": "Right Triangle"},
    3: {
        "text_1": f"But why is a right triangle so special?  One reason 'right' triangles are so important is that they are the only triangles that the Pythagorean Theorem applies to. You have likely seen this theorem before: ${lx.pythagorean_theorem}$. We'll discuss this more in the next slide.",
        "text_2": "What makes a triangle a 'right' triangle?  The existence of a 'right' angle - meaning an angle with 90 degrees.  Whenever you see a square :square: superimposed on a vertex like the red square shown here, you know you have a 'right' angle - an angle at 90 degrees :angle:.  It's opposite side is always the hypotenuse.",
        "media": "./static/PythagoreanTheorem.png",
        "media_text": "Right Triangle"},
    4: {
        "text_1": f"The pythagorean theorem is given by the expression ${lx.pythagorean_theorem}$. The letter 'c' always refers to the hypotenuse - the side opposite the right angle.  You can choose which sides represent 'a' or 'b'.  So, in this case, it doesn't matter whether a=4 and b=3 or a=3 and b=4.  Either way, the theorem holds and 'c', the hypotenuse, equals ${lx.square_root_25}$ which is 5.",
        "text_2": "What makes a triangle a 'right' triangle?  The existence of a 'right' angle - meaning an angle with 90 degrees.  Whenever you see a square :square: superimposed on a vertex like the red square shown here, you know you have a 'right' angle - an angle at 90 degrees :angle:.  It's opposite side is always the hypotenuse.",
        "media": "./static/PythagoreanTheorem.png",
        "media_text": "Right Triangle"},
    5: {
        "text_1": "Another reason 'right' triangles are so important is that the ratios of their sides represented by the trigonometric functions sine (sin), cosine (cos), and tangent (tan) will come in very handy. Look to the right triangle in the diagram.  Each vertex is associated with an angle.  A is blue.  B is green.  C is red.  We don't know what angles A and B are, but we know angle C is 90 degrees because of the red square, right?",
        "text_2": "What is sine?  Sine is a mathematical 'function'.  Like any function, you feed it an input - what mathematicians refer to as an 'argument'.  In this case, the argument is an angle.  What do we get back?  We get back a ratio.  You remember ratios from artithmetics class.  A ratio is a numerator divided by a denominator.  In this case, the numerator is the length of the side opposite the angle.  The denominator is the length of the hypotenuse.  So, in this case, the sine of angle A is the length of the blue side divided by the length of the red side.  The sine of angle B is the length of the green side divided by the length of the red side.  What about angle C?  The sine of angle C is the opposite side divided by the hypotenuse.  It just so happens that the side opposite angle C (the right angle) is always the hypotenuse.  Thus, the sine of angle C will ALWAYS be 1.  This is important.  In this fact pattern, you don't know the length of any of the sides, so you can't compute sin(A) or sin(B), but you can still conclude that sin(C) = 1.",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Sine"},
    6: {
        "text_1": "Let's stick with the same picture we have been using for the moment... :point_right:",
        "text_2": "What is cosine?  Cosine is also a mathematical 'function', just like sine.  But this time, when we feed in an angle, the numerator of the ratio is the length of the side adjacent to the angle.  The denominator is still the length of the hypotenuse.  So, in this case, the cosine of angle A is the length of the green side divided by the length of the red side.  The cosine of angle B is the length of the blue side divided by the length of the red side.  What about angle C?  We know angle C has an opposite side, but does it have an adjacent side?  No.  It doesn't.  So the length of it's adjacent side is '0'.  Thus, the cosine of angle C will ALWAYS be 0.  Again, you don't know the length of any of the sides in this example, but you can still conclude that cos(C) = 0.",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Sine"},
    7: {"text_1": "Let's keep using this picture. :point_right: I know . . . it's getting old. :clock3:",
        "text_2": "What is cosine?  Cosine is also a mathematical 'function', just like sine.  But this time, when we feed in an angle, the numerator of the ratio is the length of the side adjacent to the angle.  The denominator is still the length of the hypotenuse.  So, in this case, the cosine of angle A is the length of the green side divided by the length of the red side.  The cosine of angle B is the length of the blue side divided by the length of the red side.  What about angle C?  We know angle C has an opposite side, but does it have an adjacent side?  No.  It doesn't.  So the length of it's adjacent side is '0'.  Thus, the cosine of angle C will ALWAYS be 0.  Again, you don't know the length of any of the sides in this example, but you can still conclude that cos(C) = 0.",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Cosine"},
    8:{ "text_1": "Last time we use this picture ... I promise. :point_right:",
        "text_2": "What is tangent?  Tangent is also a mathematical 'function', just like sine and cosine.  But this time, when we feed in an angle, the numerator of the ratio is the length of the side opposite to the angle.  The denominator is still the length of the hypotenuse.  So, in this case, the cosine of angle A is the length of the green side divided by the length of the red side.  The cosine of angle B is the length of the blue side divided by the length of the red side.  What about angle C?  We know angle C has an opposite side, but does it have an adjacent side?  No.  It doesn't.  So the length of it's adjacent side is '0'.  Thus, the cosine of angle C will ALWAYS be 0.  Again, you don't know the length of any of the sides in this example, but you can still conclude that cos(C) = 0.",
        "media": "./static/RightTriangleWithDots.png",
        "media_text": "Tan"},
    9: {
        "text_1": "But what about other triangles?  Not every triangle is a right triangle.  So is any of this relevant to other triangles?  The answer is YES.  But you have to be a little creative and try and 'find' the right triangle in whatever shape you are dealing with. Imagine you have an equilateral triangle :triangle: like the one shown to the right :point_right:.",
        "text_2": "Each side is of length 6.  By definition, each angle at each vertex must be 60 degrees.  However, if we imagine a line were dropped (sometimes referred to as dropping a perpendicular) from the top vertex down to the base, like the red dashed line shown here, we bisect the equilateral triangle into 2 right-triangles.  What can we infer from this?  Well, we know that since the red line bisects the base in two, the length of each side to the left and right of the red dashed line is of length 3.  What else do we know?  We know that the angle between the red line and the base is 90 degrees (illustrated by the square).  We also know that the uppermost angle must be half of 60 degrees or 30 degrees.  So, we have two right triangles now and with angles 30-60-90 where one side has a length of 3 and the hypotenuse has a length of 6.  Pretty cool heh?",
        "media": "./static/FindTheRightTriangle.png",
        "media_text": "Finding the Right Triangle"},
    10: {
        "text_1": "The last thing we need to cover in this section is that there are a couple of right triangles that will show up again and again and again on your tests.  The reason is that they happen to have sides which are relatively easy to calculate and manipulate without calculators.  So teachers often like to use them on exams.",
        "text_2": "The three triangles you are most likely to see are the 30, 60, 90 right triangle, the 45, 45, 90 isoceles right triangle, and the 3, 4, 5 right triangle shown above :point_up:.  These are so common that you may want to commit their angles and sides to memory.",
        "media": "./static/CommonTriangles.png",
        "media_text": "Finding the Right Triangle"},
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
text_2 = content_dictionary[st.session_state.right_triangle_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.right_triangle_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)
