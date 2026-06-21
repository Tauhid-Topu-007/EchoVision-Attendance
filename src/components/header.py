import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 20px;">
        <div style="background: rgba(255,255,255,0.1); border-radius: 50%; padding: 15px; backdrop-filter: blur(10px);">
            <img src='{logo_url}' style='height: 80px;' />
        </div>
        <h1 style="text-align: center; color: white; margin-top: 10px; text-shadow: 0 2px 20px rgba(0,0,0,0.2);">ECHO<br/>ATTENDANCE</h1>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; margin-top: -5px;">AI-Powered Attendance</p>
    </div>   
    """, unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 15px; padding: 10px 0;">
        <div style="background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%); border-radius: 50%; padding: 10px;">
            <img src='{logo_url}' style='height: 60px;' />
        </div>
        <div>
            <h2 style="text-align: left; color: #5865F2; margin: 0; line-height: 1;">ECHO<br/><span style="font-size: 1.2rem;">ATTENDANCE</span></h2>
            <p style="color: #999; margin: 0; font-size: 0.8rem;">Smart Attendance System</p>
        </div>
    </div>   
    """, unsafe_allow_html=True)