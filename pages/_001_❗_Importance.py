import base64
import streamlit as st

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "importance_page" not in st.session_state:
    st.session_state.importance_page = 0

# Set Page Specific Variables
max_page_num = 1
content_dictionary = {
    0: {
        "text_1": "Trigonometry is one of the most important branches of applied mathematics.  It is unlikely anyone could list all of the ways trigonometry impacts our daily lives.  So, we will focus on one, which is probably near and dear to every teenager's heart - the cell phone. You see, electromagnetism is one of the four known forces in the universe (the others being  gravity, the strong force and the weak force).  A 2D visualization of what an electromagnetic wave looks like is to the right.",
        "text_2": "All visibile light (like the light that emanates from the sun) is made up of electromagnetic waves, like the one shown to the right.  But there are all sorts of invisible electromagnetic waves like radio waves that are bouncing around our universe.  Cell phones wouldn't work unless humans figured out how these invisible electromagnetic waves work.  And humans wouldn't have figured out how electromagnetic waves work absent - you guessed it - trigonometry!",
        "media": "./gifs/Frequency_doubling_with_perfect_pase_matching.gif",
        "media_text": "Courtesy of: Jacopo Bertolotti, CC0, via Wikimedia Commons"},
    1: {
        "text_1": "Trigonometry can be a little tricky.  For one thing, it requires you to learn a bunch of new terminology like sine, cosine, tangent, arcsine, cotangent, and radians, to name a few.  In addition, you have to learn about imaginary numbers, Euler's number, and the complex plane.  What may be most challenging is learning to visualize concepts in 2D and 3D.  We'll talk about all this in a bit.",
        "text_2": "But, as we mentioned on the previous page, trigonometry is REALLY important.  So all the hard work you put in now, learning new terms and concepts, will really pay off down the road.",
        "media": "./gifs/Sierpiński_triangle_zoom_animation.gif",
        "media_text": "Courtesy of Georg-Johann Lay, Public domain, via Wikimedia Commons"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row_col1, second_row_col2 = st.columns([6, 4], gap="small")  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.importance_page = st.session_state.importance_page + increment
    if st.session_state.importance_page < 0:
        st.session_state.importance_page = 0
    if st.session_state.importance_page > max_page_num:
        st.session_state.importance_page = 0


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.importance_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.importance_page]['text_1']
media = content_dictionary[st.session_state.importance_page]['media']
media_text = content_dictionary[st.session_state.importance_page]['media_text']

r2c1_container = second_row_col1.container(border=True)
r2c1_container.write(text_1)

r2c2_container = second_row_col2.container()

file_ = open(media, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
r2c2_container.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="em_wave">',
    unsafe_allow_html=True,
)

with r2c2_container:
    st.write("Courtesy of: Jacopo Bertolotti, CC0, via Wikimedia Commons")

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.importance_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)
