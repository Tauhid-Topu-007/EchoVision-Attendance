import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("📚 Quick Enrollment")
def auto_enroll_dialog(subject_code):
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
    .stDialog .stAlert {
        background: #f8f9fa !important;
        border-radius: 12px !important;
    }
    .stDialog .stAlert * {
        color: #1a1a1a !important;
    }
    .stDialog .stSuccess {
        background: #d4edda !important;
        border-left: 4px solid #28a745 !important;
    }
    .stDialog .stError {
        background: #f8d7da !important;
        border-left: 4px solid #dc3545 !important;
    }
    .stDialog .stInfo {
        background: #d1ecf1 !important;
        border-left: 4px solid #17a2b8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name').eq('subject_code', subject_code).execute()
    
    if not res.data:
        st.error('❌ Subject Code not found!')
        if st.button('Close', type='secondary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return
    
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    
    if check.data:
        st.info('✅ You\'re already enrolled!')
        if st.button('Got it!', type='primary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return
    
    st.markdown(f"""
    <div style="padding: 1rem 0;">
        <p style="font-size: 1.1rem; color: #1a1a1a;">
            Would you like to enroll in <strong style="color: #5865F2;">{subject['name']}</strong>?
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button('❌ No thanks', type='secondary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
    
    with col2:
        if st.button('✅ Yes, enroll now!', type='primary', use_container_width=True):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success(f'✅ Successfully enrolled in {subject["name"]}!')
            st.query_params.clear()
            time.sleep(1)
            st.rerun()