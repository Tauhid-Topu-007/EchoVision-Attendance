import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time

@st.dialog("📸 Capture or Upload Photos")
def add_photos_dialog():
    # Force visibility
    st.markdown("""
    <style>
    .stDialog, .stModal {
        background: white !important;
        color: #1a1a1a !important;
        padding: 1.5rem !important;
        border-radius: 1.5rem !important;
    }
    .stDialog *, .stModal * {
        color: #1a1a1a !important;
    }
    .stDialog h1, .stDialog h2, .stDialog h3, .stDialog h4 {
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
    }
    .stDialog label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    .stDialog p, .stDialog .stWrite {
        color: #1a1a1a !important;
    }
    .stDialog button {
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
    }
    .stDialog button * {
        color: white !important;
    }
    .stDialog button[kind="secondary"] {
        background: #e0e0e0 !important;
        color: #1a1a1a !important;
    }
    .stDialog button[kind="secondary"] * {
        color: #1a1a1a !important;
    }
    .stDialog hr {
        border-color: #e0e0e0 !important;
    }
    .stDialog .stAlert {
        background: #f8f9fa !important;
        border-radius: 12px !important;
    }
    .stDialog .stAlert * {
        color: #1a1a1a !important;
    }
    .stDialog .stCameraInput, .stDialog .stFileUploader {
        border-radius: 12px !important;
        border: 2px solid #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 0.5rem 0;">
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.5rem;">
            Add classroom photos to scan for attendance
        </p>
    </div>
    """, unsafe_allow_html=True)

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'secondary'
        if st.button('📷 Camera', type=type_camera, use_container_width=True):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'secondary'
        if st.button('📤 Upload photos', type=type_upload, use_container_width=True):
            st.session_state.photo_tab = 'upload'

    st.divider()

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('📸 Take Snapshot', key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('✅ Photo Captured Successfully!')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader(
            '📁 Choose image files', 
            type=['jpg', 'png', 'jpeg'], 
            accept_multiple_files=True, 
            key='dialog_upload'
        )
        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast(f'✅ {len(uploaded_files)} Photos Uploaded Successfully!')
            st.rerun()

    st.divider()
    
    if st.button('✅ Done', type='primary', use_container_width=True):
        st.rerun()