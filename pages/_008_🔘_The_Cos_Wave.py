import base64
import streamlit as st
import latex.latex as lx

# Redirect if Required
if "quiz_state" in st.session_state and st.session_state.quiz_state == "the_cos_wave":
    st.switch_page("pages/_030_📝_Quiz.py")

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "the_cos_wave_page" not in st.session_state:
    st.session_state.the_cos_wave_page = 0

# Set Page Specific Variables
max_page_num = 2
content_dictionary = {
    0: {
        "text_1": "",
        "text_2": f"The cosine wave looks a lot like the sine wave.  Again, note the key points.  The cosine wave is 1 when x=0 and again at 2${lx.pi}$. It's -1 at ${lx.pi}$ and it's 0 at ${lx.half_pi}$ and 3${lx.half_pi}$.",
        "media": "./static/CosFunctionPlot.png",
        "media_text": "The Cosine Wave"},
    1: {
        "text_1": "",
        "text_2": f"The above diagram shows sine and cosine on the same slide.  The important thing to bear in mind is that the diagrams are identical but for the starting point.  Look at the origin.  At x=0, sine is 0, but cosine is 1.  The sine wave 'catches' up with the cosine wave at 90 degrees (or ${lx.half_pi}$).  The key point to bear in mind here is that if you simply add (or subtract) the equivalent of 90 degrees to a sine wave, you get the same result as a cosine wave.  You can do the same to the cosine wave.  This concept of adding a value to whatever the angle is is often referred to as a 'phase shift.'",
        "media": "./static/SinAndCosFunctionPlot.png",
        "media_text": "Sine and Cosine Function Plotted"},
    2: {
        "text_1": "",
        "text_2": "The above animation illustrates the shift of the sine wave into the cosine wave and vice-versa.",
        "media": "./gifs/SinAndCosFunctionPlot.gif",
        "media_text": "Sine & Cosine Function Plot"},
    3: {
        "text_1": "",
        "text_2": "",
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
    st.session_state.the_cos_wave_page = st.session_state.the_cos_wave_page + increment
    if st.session_state.the_cos_wave_page < 0:
        st.session_state.the_cos_wave_page = 0
    if st.session_state.the_cos_wave_page > max_page_num:
        st.session_state.the_cos_wave_page = 0


def redirect_to_quiz():
    st.session_state.quiz_state = "the_cos_wave"


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.the_cos_wave_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.the_cos_wave_page]['text_1']
media = content_dictionary[st.session_state.the_cos_wave_page]['media']
media_text = content_dictionary[st.session_state.the_cos_wave_page]['media_text']

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
text_2 = content_dictionary[st.session_state.the_cos_wave_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)

# Conditional Fourth Row for Optional Quiz
if st.session_state.the_cos_wave_page == max_page_num:
    fourth_row[0].button("Take Quiz", on_click=redirect_to_quiz)