import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <h2 style="font-family: 'Climate Crisis', sans-serif; color: #1a1a1a;">I'm Student</h2>
            <div style="width: 200px; height: 200px; margin: 1rem auto; border-radius: 50%; overflow: hidden; 
                        box-shadow: 0 10px 40px rgba(0,0,0,0.15); border: 4px solid white;">
                <img src="https://img.magnific.com/free-vector/cute-boy-with-backpack-book-cartoon-vector-icon-illustration-people-education-icon-isolated_138676-13454.jpg?semt=ais_hybrid&w=740&q=80" 
                     style="width: 100%; height: 100%; object-fit: cover;">
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('Student Portal', type='primary',icon_position='right', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <h2 style="font-family: 'Climate Crisis', sans-serif; color: #1a1a1a;">I'm Teacher</h2>
            <div style="width: 200px; height: 200px; margin: 1rem auto; border-radius: 50%; overflow: hidden; 
                        box-shadow: 0 10px 40px rgba(0,0,0,0.15); border: 4px solid white;">
                <img src="https://thumbs.dreamstime.com/b/cute-teacher-mascot-chibi-glasses-points-to-blank-board-simple-setting-preparing-teach-lesson-character-stands-423693864.jpg" 
                     style="width: 100%; height: 100%; object-fit: cover;">
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button('Teacher Portal', type='secondary',icon_position='right', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()