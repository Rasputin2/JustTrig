import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "the_unit_circle":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "the_unit_circle_page" not in st.session_state:
    st.session_state.the_unit_circle_page = 0

# Set Page Specific Variables
max_page_num = 4
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": "OK... Now we're ready to start talking about something called the 'unit circle'.  The unit circle is just an ordinary circle, but it is centered at the origin (0,0) and has a radius of one.  One what?  It doesn't matter.  It could be one meter, one mile, one kilometer.  The point is that whatever units of measurement you happen to be using, the radius is one of those units.  Now, you may be wondering, what does trigonometry have to do with circles?  I thought you said trigonometry was all about triangles!  That's true.  Trigonometry is all about triangles.  But, you can reach any point on the unit circle (see the red dot) with right triangles.  Go to the next slide to see how.",
        "media": "./gifs/UnitCircleWithDot.gif",
        "media_text": "The Unit Circle"},
    1: {
        "text_1": "",
        "text_2": "What this animation shows is how you can reach any point on the unit circle with a right triangle.  In any of the four quadrants of the unit circle, by carefully drawing a right triangle, we can ensure that one of the vertices touches the circle.  Why is this important?  It is important, because it means that we can use that knowledge of trig functions to identify any given point on the circle.  Why do we care?  Remember in the Importance section we discussed the concept of waves.  We'll tie this all together in a moment, but there are a couple more things we need to cover first.  Be patient....",
        "media": "./gifs/UnitCircleWithTriangle.gif",
        "media_text": "Right Triangle in Unit Circle"},
    2: {
        "text_1": "",
        "text_2": "Things can get a little weird at the axes.... What you need to do is imagine that at (1,0) you have a right triangle with no height.  In this case, the sin will be zero and the cos will be 1, because the length of the adjacent side will be 1 and the hypotenuse will also be 1. At (0,1) you have to imagine a right triangle with no width, and so the opposite side has length 1 and the hypotenuse has length 1, and so the sin is 1 and the cosine is 0.  Take some time and think about that before you proceed :thinking_face:.  What is really important to keep in mind here is that you can use the unit circle to determine what the sine or cosine is of ANY angle.  This is because whatever angle you choose, all you need to do is find the x and y coordinates of the point where a carefully drawn right triangle intersects with the circle.  The y coordinate will give you sine and the x coordinate will give you cosine.  Let's check out an example....",
        "media": "./static/UnitCircleAtAxes.jpg",
        "media_text": "Unit Circle on Axes"},
    3: {
        "text_1": "",
        "text_2": f"Let's assume someone were to ask you for the cosine of 135 degrees.  How could you use what you have learned thus far to find that answer?  Well, theta_1, shown above, is what we are trying to find.  Obviously, since the angle is larger than 90 degrees we can't make a right triangle out of that.  But what if we were to drop a new line (the red line) down perpendicular to the x-axis as shown above.  Now, we have theta_2.  What is theta_2?  We know that an entire circle is 360 degrees right?  So, half a circle is 180 degrees.  If we subtract 135 from 180, we get 45, which is theta_2.  Now, we have a right triangle in the second quadrant defined by the white rotated line, the x-axis and the red perpendicular line.  We know the right angle is 90 degrees and theta_2 is 45 degrees.  Thus, given triangles have to have only 180 degrees, we know the other angle is also 45 degrees.  What else do we know?  Well, this is the unit circle right?  So, the hypotenuse has to be '1' units long, because the radius of the unit circle is '1' and the hypotenuse here has to equal the radius of the circle. We also know that the height and width of the triangle have to be identical because the non-right angles are identical.  We also know from the pythagorean theorem ${lx.pythagorean_theorem}$ that c in this case is 1, and a and b are identical so we can rewrite the right-side of the equation as 2a^2.  So now we just do some algebra.  This simplifies to a = the square root of 1/2 which is plus or minus ${lx.square_root_2_over_2}$.  We say plus or minues because it's possible a was negative and when we squared it, the negative sign went away (i.e., a negative times a negative yields a positive).  So, believe it or not, we now have our answer.  You see, the cosine of the angle drawn from 0 to 135 degrees is the same as the cosine of 45 degrees in the third quadrant.  We know that the cosine equals the x coordinate of a carefully drawn right triangle.  What is our x-coordinate here?  It is -${lx.square_root_2_over_2}$.  Voila! :popcorn:",
        "media": "./gifs/UnitCircle135.gif",
        "media_text": "Unit Circle on Axes"},
    4: {
        "text_1": "",
        "text_2": "More to come... radians, and waves!",
        "media": "./static/UnitCircleRadians.jpg",
        "media_text": "Unit Circle on Axes"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row = st.columns(1)  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.the_unit_circle_page = st.session_state.the_unit_circle_page + increment
    if st.session_state.the_unit_circle_page < 0:
        st.session_state.the_unit_circle_page = 0
    if st.session_state.the_unit_circle_page > max_page_num:
        st.session_state.the_unit_circle_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "the_unit_circle"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.the_unit_circle_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.the_unit_circle_page]['text_1']
media = content_dictionary[st.session_state.the_unit_circle_page]['media']
media_text = content_dictionary[st.session_state.the_unit_circle_page]['media_text']

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
text_2 = content_dictionary[st.session_state.the_unit_circle_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.the_unit_circle_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)
