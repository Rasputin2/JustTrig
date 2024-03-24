import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "trig_identities_pt1":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "trig_identities_pt1_page" not in st.session_state:
    st.session_state.trig_identities_pt1_page = 0

# Set Page Specific Variables
max_page_num = 1
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": "Now we move to one of the more difficult aspects of trigonometry, because it tends to require a lot of memorization.  We're talking specifically about so-called trig identities.  First, let's consider what is a mathematical 'identity'?  A mathematical identity is an equation (i.e., two mathematical expressions that are equal to one another) that has a unique property in that it is true for ALL values of a variable.  Trig identities are mathematical identities that involve trigonometric functions. The most important identities are called the 'fundamental' identities, and it is those that we cover here in this section.  There are more fundamental identities than shown above, but the reason we only show these ones is that the other Fundamental Identities can all be derived from these.  That is why it is really important to memorize these and understand where they come from.",
        "media": "./static/FundamentalIdentities.png",
        "media_text": "Fundamental Identities"},
    1: {
        "text_1": "",
        "text_2": f"The first even-odd identity we'll look at is ${lx.sin_neg_angle_id}$. To figure out why this is true, just look at the Unit Circle :point_up:.  For example, if theta is positive, as it is in the red triangle, the opposite side is going to be positive, because it is in Quadrant I.  If, instead, theta is negative, as it is in the green triangle, then the opposite side is going to be negative (i.e., the y-coordinate of the terminus of the opposite side, will be a negative number) because it is in Quadrant IV. If you need a refresher on the quadrants, go back to the introduction section.  The same holds true in Quadrants II and III.  If the opposite side terminates in Quadrant II, it's positive whereas if it terminates in Quadrant III, it's negative.  This brings us to an important point.  Remember the trig functions are 'functions' and 'functions' can be 'odd' or 'even'.  A function is 'odd' if it is like sine, the sign of your output changes when the sign of your input changes.  Otherwise, it is considered 'even'.",
        "media": "./static/SinNegativeAngle.png",
        "media_text": "Sine is an Odd Function"},
    2: {
        "text_1": "",
        "text_2": "There are a couple of key points to note about the sine wave.  Notice how the x-axis may be phrased in terms of radians or other units.  But in all events, unless the plot is shifted (which we'll talk about in the section More_Waves) the peak of the sine wave should appear at pi/2.  The trough of the sine wave should appear at 3/2pi and the zeroes (the places where the function intersects with the x axis should be at 0 and 2pi).  This cycle repeats indefinitely in either direction.  So, for example, zeroes will occur at 4pi, and 6pi and 8pi, etc.  ",
        "media": "./static/SinFunctionPlot.png",
        "media_text": "Sine Function Plot"},
    3: {
        "text_1": "",
        "text_2": "The other thing to bear in mind is that sine is a 'function'.  A 'function' has a very specific meaning in mathematics.  A function takes an input - in this case the numbers on the x axis - and produces an output - i.e., the numbers on the y-axis.  Importantly, the same input cannot generate two different output values.  If that did happen, then sine wouldn't be a 'function' by definition.  Compare and contrast the graph of the circle on the left and the sine wave on the right.  On the left, a single point on the x-axis can (and does) correspond to more than one location on the y-axis.  So the formula that generates a circle (be it a Unit Circle or not) cannot be a 'function'.  In contrast, every x coordinate on the sine wave on the right correlates to a single y-value.",
        "media": "./gifs/SinIsAFunction.gif",
        "media_text": "Sine Is a Function"},
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
    st.session_state.trig_identities_pt1_page = st.session_state.trig_identities_pt1_page + increment
    if st.session_state.trig_identities_pt1_page < 0:
        st.session_state.trig_identities_pt1_page = 0
    if st.session_state.trig_identities_pt1_page > max_page_num:
        st.session_state.trig_identities_pt1_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "trig_identities_pt1"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.trig_identities_pt1_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.trig_identities_pt1_page]['text_1']
media = content_dictionary[st.session_state.trig_identities_pt1_page]['media']
media_text = content_dictionary[st.session_state.trig_identities_pt1_page]['media_text']

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
text_2 = content_dictionary[st.session_state.trig_identities_pt1_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.trig_identities_pt1_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)