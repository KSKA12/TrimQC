from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Tool Page", page_icon=":microscope:", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)
        
local_css("webpage2/style/style.css")

lottie_coding = load_lottieurl ("https://assets5.lottiefiles.com/packages/lf20_ymEv4F.json")
img_fac_logo = Image.open("webpage2/images/biotech.png")
img_uni_logo = Image.open("webpage2/images/Nile_University_logo.png")

with st.container():

    st.subheader("Welcome to our Quality Check and Trimming Tool")

    st.title("The One-Stop Shop for all your sequence quality needs")

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

with right_column:
    st_lottie(lottie_coding, height=300 , key="DNA")

with st.form("my_form"):
   st.write("Please Fill The Requirements")
   url= st.text_input("Please insert the file URL")
   url_access = st.checkbox("The URL is Accessable")
   extension = st.selectbox("Kindly Choose the Extension of Your File",['fastq', 'fastq.gz', '.gz'])
   parameter1 = st.text_input("Kindly Enter the Start Parameter of Your Sequence")
   parameter2 = st.text_input("Kindly Enter the End Parameter of Your Sequence")
   adapter_type = st.selectbox('Kindly Choose the Adapter Type', ['illumina', 'TruSeq','Nextra'])

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("File Extension: ", extension, ", URL Accessability: ", url_access, 
                ", Start Parameter: ", parameter1, ", End Parameter: ", parameter2, ",Adapter Type: ", adapter_type)
















