import streamlit as st
import base64 

def web_app_portfolio():
    st.set_page_config(page_title="Hailu Gudissa's portfolio", page_icon="⭐")
    with open("style/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)  

    with open("asset/hailu_pic.jpg", "rb") as img_file:
         img = "data:image/jpg;base64," + base64.b64encode(img_file.read()).decode()

    with open("asset/Profile.pdf", "rb") as pdf_file: 
       pdf_bytes= pdf_file.read()
          

    st.write(f"""<div class= "title"> Hello! My name is <strong> Hailu Gudissa</strong> 👋</div>
        """, unsafe_allow_html= True)
    
    st.write(f"""
        <div style = "display: flex; justify-content: center;"> 
            <img src= "{img}" alt= "Hailu Gudissa" width="300 height="300" style= "border-radius:50%;object-fit:cover;margin-top: 40px;margin-bottom: 40px;">
        </div>
        """, unsafe_allow_html= True)
    
    st.write(f"""
        <div class= "subtitle" style= "text-align: center;"> Data Science and AI Professional</div>""", unsafe_allow_html= True)
             
    # st.write(f"""
    # <div class= "title" style= "text-align: center;">
    # <span style='font-size= 32px;'>Hello! My name is Hailu Gudissa</span>
    # </div>
    # """, unsafe_allow_html= True)
    
    # st.markdown('<style> div.block-container{padding-top:4rem;}</style>', unsafe_allow_html= True)

    # with open("Profile.pdf", "rb") as pdf_file: 
    #    pdf_bytes= pdf_file.read()

    # st.write(f"""
    # <div class= "subtitle" style= "text-align: center;"> 
    # <span style='font-size= 12px;'>Data Scientist and AI Engineer</span>
    # </div>
    # """, unsafe_allow_html= True)

    social_media_data = {
    "Kaggle":["https://www.kaggle.com/hailugud","https://www.kaggle.com/static/images/site-logo.svg"],
    "LinkedIn":["https://www.linkedin.com/in/hailu-gudissa-a254a1108/","https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    "Github":["https://github.com/Hailata","https://cdn-icons-png.flaticon.com/128/25/25231.png"]
    }
    social_media_html = [
    f"<a href='{social_media_data[platform][0]}' target= '_blank' style='margin-right:10px;'>"
    f"<img class='social-icon' src='{social_media_data[platform][1]}' alt='{platform}'"
    f" style= 'width:30px; height:30px;'></a>"
    for platform in social_media_data
    ]
    st.write(f"""
    <div style= "display :flex; justify-content:center; margin-bottom: 20px;"> 
    {'' .join(social_media_html)}
    </div>
    """, unsafe_allow_html= True)

    st.write('##')

    st.subheader("About Me")

    st.markdown("""
    - I am a **Data Science and AI Professional** with a solid foundation in *statistical analysis, machine 
      learning, and deep learning*. 
    - Adept at developing, fine-tuning, and deploying models using Python, SQL, and industry
      standard AI frameworks such as Hugging Face Transformers and PyTorch. 
    - Strong analytical mindset with hands-on experience in solving real-world problems through data-driven solutions. 
    - Eager to contribute to innovative, AI-powered teams in dynamic environments.
    - You can contact me through debinathuka@gmai.com
    - Based in USA
    """)

    st.write('##')

    st.download_button(label="📥 Download my Resume", data= pdf_bytes, file_name= "Profile.pdf", mime= "Application/pdf",)

if __name__ =="__main__":
  web_app_portfolio()

