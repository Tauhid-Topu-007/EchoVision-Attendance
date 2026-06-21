import streamlit as st

def footer_home():
    logo_url = "/images/logoai.png"
    
    st.markdown(f"""
    <div style="margin-top: 3rem; padding: 1rem 0; text-align: center; border-top: 1px solid rgba(255,255,255,0.2);">
        <div style="display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style="font-weight: 600; color: rgba(255,255,255,0.9); margin: 0;">Created with ❤️</p>
        </div>
        <p style="color: rgba(255,255,255,0.6); font-size: 0.8rem; margin-top: 0.5rem;">
            AI-Powered Smart Attendance System
        </p>
    </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    logo_url = "images/logoai.png"
    
    st.markdown(f"""
    <div style="margin-top: 3rem; padding: 1rem 0; text-align: center; border-top: 1px solid #e0e0e0;">
        <div style="display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p style="font-weight: 600; color: #1a1a1a; margin: 0;">Created with ❤️</p>  
        </div>
        <p style="color: #999; font-size: 0.8rem; margin-top: 0.5rem;">
            AI-Powered Smart Attendance System
        </p>
    </div>
    """, unsafe_allow_html=True)