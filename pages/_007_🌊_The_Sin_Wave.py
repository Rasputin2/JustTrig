import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "the_sin_wave":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "the_sin_wave_page" not in st.session_state:
    st.session_state.the_sin_wave_page = 0

# Set Page Specific Variables
max_page_num = 3
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": "Now things can get a little more interesting.  If you look above, you see how if you simply cut the unit circle in half and shift one of the halves, it now looks like a wave, right?  If you read the introductory materials you'll know that one of (although not the only) the reasons trigonometry is so important today is that it facilitates the study of waves and physical phenomenon that have wave-like behavior.",
        "media": "./gifs/UnitCircleToWave.gif",
        "media_text": "The Unit Circle to Wave"},
    1: {
        "text_1": "",
        "text_2": f"We saw in the Unit Circle section how every point on the Unit Circle was uniquely defined by a pair of x and y coordinates where cos(${lx.theta}$) established the x coordinate and sin(${lx.theta}$) established the y coordinate.  What the above illustration :point_up: shows is what just those those y-coordinates look like if they were unrolled and plotted against the x-axis.  We call this plot the sine wave.",
        "media": "./gifs/SineCurveUnitCircle.gif",
        "media_text": "Modified From heejin_park, https://infograph.tistory.com/230"},
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
    st.session_state.the_sin_wave_page = st.session_state.the_sin_wave_page + increment
    if st.session_state.the_sin_wave_page < 0:
        st.session_state.the_sin_wave_page = 0
    if st.session_state.the_sin_wave_page > max_page_num:
        st.session_state.the_sin_wave_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "the_sin_wave"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.the_sin_wave_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.the_sin_wave_page]['text_1']
media = content_dictionary[st.session_state.the_sin_wave_page]['media']
media_text = content_dictionary[st.session_state.the_sin_wave_page]['media_text']

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
text_2 = content_dictionary[st.session_state.the_sin_wave_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.the_sin_wave_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)