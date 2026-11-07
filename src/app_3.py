from stegano import lsb 
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Stegano Project")
option = st.sidebar.selectbox("Select Your option:", 
                              ("Hide Text ", "Reveal Text"))

if option == "Hide Text ":
    host_pic = st.file_uploader("select your image", type=("png", "jpg"))
    secret_text = st.text_area("Enter your text to hide:")


    if host_pic and secret_text:

        temp_img = Image.open(host_pic)
        final_img = lsb.hide(temp_img, secret_text)
        final_img.save("./final_img_pars.png")

elif option == "Reveal Text":
    final_secreted_image = st.file_uploader("select image fo reveal text", type=("png", "jpg"))

    if final_secreted_image:
        temp_imge = Image.open(final_secreted_image)

        secret_text_reveald = lsb.reveal(temp_imge)  

        if secret_text_reveald != None:
            st.write(secret_text_reveald)
            st.success