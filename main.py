import streamlit as st
import requests
from click import style
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon = "", layout = "wide")


def load_lottie_ani(url):
    r = requests.get(url)
    if r != 200:
        print(None)

    return r.json()

# Load CSS
def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

load_css("style/style.css")

l_ani = load_lottie_ani("https://lottie.host/0680ed40-d9df-4ed9-b27f-af607e7563ec/MVRtC5Ktiz.json")
img_pc = Image.open("Images/PC1.jpg")
img_repair = Image.open("Images/repair.jpg")

#---Header
with st.container():
    st.subheader("your friend in tech services")
    st.title("S3P Tech Services")
    st.write("Hello, you should try our comprehensive services.")
    st.write("learn more")

# --- Body ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(" Our Services")
        st.write("Laptop and Computer Services: Whether it’s a faulty keyboard, a broken hinge, or a malfunctioning hard drive, our team can handle it all.")
        st.write("Virus Removal and Security: Worried about malware? We’ll clean up your system and enhance its security.")
        st.write("Data Recovery: Accidentally deleted important files? We’ll recover them for you.")
        st.write("Gaming PC cleaning: It feels like brand new with our expert touch up.")
        st.subheader("Checkout our Social Sites")

    with right_column:
        st_lottie(l_ani, height = 300, key = "code")

with st.container():
    image_column , text_column = st.columns((1, 2))
    with image_column:
        st.image(img_pc)


    with text_column:
        st.subheader("Why S3P Tech Services?")
        st.write("Expertise: Our technicians are certified and experienced, ensuring top-notch repairs.")
        st.write("Quick Turnaround: We know you can’t be without your devices for long. Our efficient service gets you back up and running swiftly.")

with st.container():
    st.write("___")
    st.header("Send a Message")
    st.write("###")

#---formsubmit.co..
    contactform = """ <form action="https://formsubmit.co/4908796f0eb32c16f35922edf130b72c" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="Message" placeholder="Write your message here!" required></textarea>
     <button type="submit">Send</button>
     </form> """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contactform, unsafe_allow_html= True )

    with right_column:
        st.empty()


