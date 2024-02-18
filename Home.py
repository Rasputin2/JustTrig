import time
import streamlit as st


st.title("Just Trig!")
st.subheader("Where Everyone Learns to :heart: Trigonometry.")

intro_p1 = "If you are sitting in your trigonometry class cursing the Pythagoras's name, then this is the website for you.  As the name suggests, Just Trig focuses solely on trigonometry - from basic - to intermediate - to advanced."

intro_p2 = "We start with the most important question of all - why should I learn this stuff?  We move on from there in easily digestible increments.  Each page shown on the left sidebar reflects a discrete topic.  You can just click on the link on the left sidebar and take it from there.  Each topic is followed by a quiz.  We recommend that you do not move ahead to a subsequent topic before getting ALL (100%) of the questions right on each quiz.  We also recommend that if you get something wrong on a quiz, you step away for a while, think about something else, and then retake the quiz.  This advice is based on the neuroscience of 'chunking' - the idea that the operating system of your brain keeps processing and memorizing information even after you are consciously focused on that task."

intro_p3 = ("Now . . . strap in and click on -- Importance -- in the left side bar to learn why you should learn trigonometry.")

def write(text):
    for word in text.split():
        yield(word + " ")
        time.sleep(0.20)


st.write_stream(write(intro_p1))
st.write_stream(write(intro_p2))
