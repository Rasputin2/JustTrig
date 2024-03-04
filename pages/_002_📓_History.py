import streamlit as st
import latex.latex as lx

# Create the Grid
first_row_col1, first_row_col2 = st.columns([7, 3], gap="small")
second_row_col1, second_row_col2 = st.columns([7, 3], gap="small")
third_row = st.columns(1)

import base64
import streamlit as st

# Set Session Variables
# Entire Script Runs Upon Page Refresh
if "history_page" not in st.session_state:
    st.session_state.history_page = 0

# Set Page Specific Variables
max_page_num = 1
content_dictionary = {
    0: {
        "text_1": "Many concepts underlying the study of trigonometry are so old we don't even know who first used or invented them.  For example, the concept of pi (pronounced like :pie:) - the constant that relates the circumference of a circle to it's diameter - has been around for over 4000 years.  In fact, it may be even older than that!  We just don't know.",
        "text_2": f"So, it may be easiest to start with one of the most important formulas in mathematics and work backwards from there.  In 1740 (almost 300 years ago) this guy shown here, Leonard Euler, discovered this formula: ${lx.eulers_formula}$ which we know today as Euler's formula.  Don't worry if you don't recognize or understand this.  We'll cover it all later.  One of the many cool things about this formula is that if you substitute ${lx.pi}$ for theta, the foregoing simplifies to: ${lx.eulers_identity}$, which we know as Euler's identity.  There is a lot going on here for such a short formula.  We'll start with ${lx.pi}$, which is the oldest concept in the above formula.  We'll then look at the history of sin and cos.  Then we'll see where the 'i' comes from and then the 'e', which arrived on the scene last.",
        "media": "./static/euler.jpg",
        "media_text": "Courtesy of Wikimedia Commons"},
    1: {
        "text_1": f"The oldest concept in Euler's identity is ${lx.pi}$.  As we'll discuss in more detail later, Pi represents the ratio of the circumference of a circle over its diameter.  So, in the picture to the right, if you measured the length of the blue circle and divided it by the length of the red diameter - you should always get the same number - no matter how big or small the circle is - approximately 3.14.  ",
        "text_2": f"For a thorough history of ${lx.pi}, we'd encourage you to read *A History of Pi*, by Petr Beckman.  In sum, the oldest records we have suggest that the Babylonians first discovered the relationship between a circumference of a circle to it's diameter.  The primary difficulty the ancients had was in accurately measuring ${lx.pi}$ because it is an irrational number - i.e., it has an infinite number of decimal places.  Interestingly, the Babylonians had a base60 numbering system - whereas today we have a base10 numbering system adopted from the Arabic mathematicians in the middle ages.  Because the Bablyonians had a base60 numbering system, they divided circles into 6 arcs, each containing 60 degrees - which is why we continue to refer to a circle as having 360 degrees today.  Nevertheless, the Babylonians, Egyptians and then the Greeks and Persians all tried to come up with more and more accurate measures of ${lx.pi}$. We didn't start actually using the term (pi) and symbol ${lx.pi}$ until 1706, however, when the British mathematician, William Jones, coined it and Leonard Euler (seen before) popularized it.",
        "media": "./gifs/Pi.gif",
        "media_text": "Pi = Circumference / Diameter"
    },
    2: {
        "text_1": "The guy shown here is Pythagoras.  Pythagoras was born on the Greek Island of Samos in 570 BCE.... ",
        "text_2": "MORE TO COME... The Babylonians, the history of i, why we i, e and pi the 'transcendental' numbers and why e shows up all the time in nature ...",
        "media": "./static/pythagoras.jpg",
        "media_text": "Courtesy of: Jacopo Bertolotti, CC0, via Wikimedia Commons"}
}
# Create the Grid
first_row_col1, first_row_col2, first_row_col3 = st.columns([1, 8, 1], gap="small")  # Button - Header - Button
second_row_col1, second_row_col2 = st.columns([6, 4], gap="small")  # Text -- Media
third_row = st.columns(1)  # Text
fourth_row = st.columns(1)  # Conditional Buttons


# The Streamlit Session State Persists
# Across Pages
def set_stage(increment):
    st.session_state.history_page = st.session_state.history_page + increment
    if st.session_state.history_page < 0:
        st.session_state.history_page = 0
    if st.session_state.history_page > max_page_num:
        st.session_state.history_page = 0


# Render the Pages
# The Content Changes Based on the Session_State Which
# Acts as the Key for the Content Dictionary

# Fill in First Row Content
button1 = first_row_col1.button('Prev', on_click=set_stage, args=[-1], type="primary")

r1c2_container = first_row_col2.container()
with r1c2_container:
    st.write("Page " + str(st.session_state.history_page) + " of " + str(max_page_num) + " pages.")

button2 = first_row_col3.button('Next', on_click=set_stage, args=[1], type="primary")

# Fill in Second Row Content
text_1 = content_dictionary[st.session_state.history_page]['text_1']
media = content_dictionary[st.session_state.history_page]['media']
media_text = content_dictionary[st.session_state.history_page]['media_text']

r2c1_container = second_row_col1.container(height=350, border=True)
r2c1_container.write(text_1)

r2c2_container = second_row_col2.container(height=350, border=True)

file_ = open(media, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
r2c2_container.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="em_wave">',
    unsafe_allow_html=True,
)
with r2c2_container:
    st.write(media_text)

# Fill in Third Row Content
text_2 = content_dictionary[st.session_state.history_page]['text_2']
with third_row[0].container(border=True):
    st.write(text_2)
