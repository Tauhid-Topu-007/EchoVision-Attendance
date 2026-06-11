import streamlit as st


from src.ui.base_layout import style_background_dashboard,style_base_layout

from src.components.header import header_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    teacher_screen_login()
    

def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment="center",gap='xxlarge')
    
    with c1:
        header_dashboard()
    with c2:
        st.button("Go Back to Home", type='secondary',key='loginbackbtn',shortcut='ctrl+backspace')
        
    st.header("Login with password",text_align="center")
    


def teacher_screen_register():
    c1,c2=st.columns(2,vertical_alignment="center",gap='xxlarge')
    
    with c1:
        header_dashboard()
    with c2:
        st.button("Go Back to Home", type='secondary',key='loginbackbtn',shortcut='ctrl+backspace')
        
    st.header("Register your teacher profile",text_align="center")