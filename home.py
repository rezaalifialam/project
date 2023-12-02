import streamlit as st

st.set_page_config(
    page_title="Portfolio | AA. REZA",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("tuma.jpg", width= 190)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : REZA ALIFI ALAM")
   st.caption("NIM : 0402201090")
   st.write(
            """
            - Nama Panggilan       : AA. REZA
            - Tempat Tanggal Lahir : Indramayu, 13 Oktober 1998 
            - Alamat               : Dukuhjati Krangkeng Indramayu
            - Hal Yang Disukai     : Mayoran
            - Hobi                 : Main Bola
            - Status               : Lajang
            """
        )
   
   col1, col2, col3, col4, = st.columns(4)
with col1:
   
    st.image("yt.png", width= 50)
    st.link_button("Youtube Chanel", "https://www.youtube.com/@kangtumachanel6294")
with col2:
   
    st.image("fb.png", width= 50)
    st.link_button("Facebook", "https://www.facebook.com/reza.tumaritiz.7?mibextid=ZbWKwL")
with col3:
    
    st.image("ig.png", width= 50)
    st.link_button("Instagram", "https://instagram.com/rezatumaritiz?igshid=NGVhN2U2NjQ0Yg==")
with col4:
    
    st.image("bl.png", width= 50)
    st.link_button("Blogger", "https://rezatumaritiz.blogspot.com/")



st.header("*Call Me If You Want*")

import streamlit as st

st.link_button("Go to contact", "http://localhost:8501/contact_dan_saran")

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("waweb.jpeg", width= 190)
    st.write("*Save : 0895 0908 7211*")
    




