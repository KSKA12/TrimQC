from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser

st.set_page_config(page_title="Quality Check and Trimmer Tool", page_icon=":microscope:", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)
        
local_css("webpage1/style/style.css")

lottie_coding = load_lottieurl ("https://assets5.lottiefiles.com/packages/lf20_ymEv4F.json")
img_fac_logo = Image.open("webpage1/images/biotech.png")
img_uni_logo = Image.open("webpage1/images/Nile_University_logo.png")
img_kamal = Image.open("webpage1/images/kamal.png")
img_sisi = Image.open("webpage1/images/sisi.png")
img_andrew = Image.open("webpage1/images/andrew.png")
img_hamza = Image.open("webpage1/images/hamza.png")
img_hwary = Image.open("webpage1/images/hwary.png")
with st.container():

    st.subheader("Welcome to our Quality Check and Trimming Tool")

    st.title("The One-Stop Shop for all your sequence quality needs")

    st.write("Our Project aims to help Bioinformaticians with processing sequences in one place instead of having to use seperate tools to check, trim, format fastq files.")

with st.container():
    
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        
        st.header("How to use our tool")
        
        st.write("##")
        
        st.write(
            """
            - Input the URL to your sequence file
            - Specify The Extension of Your File (eg: .fastq, .fastq.gz, .gz)
            - Specify The Parameters You want to Work On
            - Specify The Adaptor Type You Want to Work With
            
            Make sure the access to the URL is open.
            Make sure to choose the appropriate adaptor and parameters for the best results.
            """
        )
        url = 'https://kska12-trimqc-webpage2app2-5qzleo.streamlit.app/'

        if st.button('Check Sequence Here!'):
            webbrowser.open_new_tab(url)
    with right_column:
        st_lottie(lottie_coding, height=300 , key="DNA")
        
with st.container():
    
    st.write("---")
    
    st.header("About us")
    
    st.write("##")
    
    image_column, text_column = st.columns((0.35,2))
    with image_column:
        
        st.image(img_fac_logo)
    st.write("---")
        
    with text_column:
        st.subheader("Our Vision")
        st.write(
            """
            We're a team of five bioinformatics students at nile university's faculty of biotechnology.
            
            Our aim is to aid in the processing of biological data by providing the industry with tools that cut both cost and time in order to help advance the bioinformatics research scope.
        
            """
        )
        url = 'mailto:theking200060@gmail.com'

        if st.button('Contact Us'):
            webbrowser.open_new_tab(url)

with st.container():
    st.header("Get to Know The Team")
    image_column, text_column = st.columns((0.5,2))
    with image_column:
        st.image(img_kamal)
        
        with text_column:
            st.subheader("Kamal Abdallah")
            st.write(
                """
                - Bioinformatics Student at Nile University
                - SOLE competition First Place Winner
                - ISEF competition Runner-Up
                - STEM school graduate
                """
            )
            st.write("")
            url = 'mailto:K.Salah@Nu.Edu.Eg'

            if st.button('Contact Kamal'):
                webbrowser.open_new_tab(url)
    st.write("---")

with st.container():
    image_column, text_column = st.columns((0.5,2))
    with image_column:
        st.image(img_sisi)
        
        with text_column:
            st.subheader("Mohammed ElSisi")
            st.write(
                """
                - Bioinformatics Student at Nile University
                - UGRF Competition Nominee
                - Intermediate R Programmer
                - Member of Student Union Representative Team
                """
            )
            st.write("")
            url = 'mailto:M.ElSisi@Nu.Edu.Eg'

            if st.button('Contact Mohammed'):
                webbrowser.open_new_tab(url)
    st.write("---")

with st.container():
    image_column, text_column = st.columns((0.35,2))
    with image_column:
        st.image(img_hwary)
        
        with text_column:
            st.subheader("Mohamed ElHwary")
            st.write(
                """
                - Bioinformatics Student at Nile University
                - UGRF Competition Nominee
                - Intermediate R Programmer
                - Member of Research Committee at Biotechnomatics NU
                """
            )
            st.write("")
            url = 'mailto:M.Elhwary@Nu.Edu.Eg'

            if st.button('Contact Mohamed'):
                webbrowser.open_new_tab(url)
    st.write("---")
    
with st.container():
    image_column, text_column = st.columns((0.5,2))
    with image_column:
        st.image(img_andrew)
        
        with text_column:
            st.subheader("Andrew Ghabbour")
            st.write(
                """
               - Bioinformatics Student at Nile University
               - UGRF Competition Nominee
               - Head of Media Committee at Biotechnomatics NU
               - Intermediate Python Programmer
                """
            )
            st.write("")
            url = 'mailto:A.Eshak@Nu.Edu.Eg'

            if st.button('Contact Andrew'):
                webbrowser.open_new_tab(url)
    st.write("---")
    
with st.container():
    image_column, text_column = st.columns((0.6,2))
    with image_column:
        st.image(img_hamza)
        
        with text_column:
            st.subheader("Hamza AlaaElDin")
            st.write(
                """
                - Bioinformatics Student at Nile University
                - SOLE Competition First Place Winner
                - Intro. to Python Junior Teaching Assistant
                - Head of Research Committee at Biotechnomatics NU
                """
            )
            st.write("")
            url = 'mailto:H.AlaaElDin@Nu.Edu.Eg'

            if st.button('Contact Hamza'):
                webbrowser.open_new_tab(url)
    st.write("---")
    
    
    
with st.container():

    
    left_column, right_column = st.columns(2)
    
    with left_column:
        
        st.header("Additional Info")
    
        st.subheader("Course Name:")
        st.write(
            """
            - CBIO311: Advanced Programming and Data
            """
        )
    with right_column:
        st.write("##")
        st.subheader("Course Instructors:")
        st.write(
            """
            - Mohammed Farahat (Course Instructor)
            - Omnia AbdelRaouf (Lab Instructor)
            """
        )
# with st.container():
#         st.write("---")
        #st.header("Get In Touch With Us!")
        #st.write("##")
        
        #contact_form = """
        #<form action="https://formsubmit.co/your@email.com" method="POST">
            #<input type ="hidden" name= "_captcha" value ="false">  
            #<input type="text" name="name" placeholder="Your name" required>
            #<input type="email" name="email" placeholder ="Email" required>
            #<textarea name ="message" placeholder = "Your message here" required></textarea>
            #<button type="submit">Send</button>
        #</form>
        #"""
#left_column, right_column = st.columns(2)
#with left_column:
    #st.markdown(contact_form, unsafe_allow_html=True)
#with right_column:
    #st.empty()
