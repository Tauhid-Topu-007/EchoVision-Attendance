import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("📚 Enroll in Subject")
def enroll_dialog():
    # Force white background and dark text for this dialog
    st.markdown("""
    <style>
    /* Force dialog background to white */
    .stDialog {
        background: white !important;
    }
    
    /* Make all text in dialog dark and visible */
    .stDialog * {
        color: #1a1a1a !important;
    }
    
    /* Headers in dialog */
    .stDialog h1, .stDialog h2, .stDialog h3, .stDialog h4 {
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
    }
    
    /* Labels in dialog */
    .stDialog label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    /* Input fields in dialog */
    .stDialog input {
        color: #1a1a1a !important;
        background: white !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
    }
    
    .stDialog input:focus {
        border-color: #5865F2 !important;
        box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.1) !important;
    }
    
    /* Placeholder text */
    .stDialog input::placeholder {
        color: #999 !important;
    }
    
    /* Caption/text in dialog */
    .stDialog .stCaption, .stDialog .stWrite, .stDialog p {
        color: #666 !important;
    }
    
    /* Alert messages */
    .stDialog .stAlert {
        border-radius: 12px !important;
        background: #f8f9fa !important;
        border-left: 4px solid #5865F2 !important;
    }
    
    .stDialog .stAlert * {
        color: #1a1a1a !important;
    }
    
    .stDialog .stSuccess {
        background: #d4edda !important;
        border-left: 4px solid #28a745 !important;
    }
    
    .stDialog .stWarning {
        background: #fff3cd !important;
        border-left: 4px solid #ffc107 !important;
    }
    
    .stDialog .stError {
        background: #f8d7da !important;
        border-left: 4px solid #dc3545 !important;
    }
    
    /* Buttons in dialog */
    .stDialog button {
        color: white !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        border: none !important;
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
    
    .stDialog button[kind="secondary"]:hover {
        background: #d0d0d0 !important;
    }
    
    /* Divider in dialog */
    .stDialog hr {
        border-color: #e0e0e0 !important;
        background: #e0e0e0 !important;
        margin: 1rem 0 !important;
    }
    
    /* Container inside dialog */
    .stDialog .stContainer {
        background: white !important;
        border: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Dialog content with visible text
    st.markdown("""
    <div style="padding: 0.5rem 0;">
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.5rem;">
            Enter the subject code provided by your teacher to enroll
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    join_code = st.text_input(
        'Subject Code', 
        placeholder='e.g. CS101',
        key='enroll_code_input'
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('📥 Enroll now', type='primary', use_container_width=True):
            if join_code:
                with st.spinner('Enrolling...'):
                    try:
                        # Check if subject exists
                        res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code.upper()).execute()
                        
                        if res.data:
                            subject = res.data[0]
                            student_id = st.session_state.student_data['student_id']
                            
                            # Check if already enrolled
                            check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                            
                            if check.data:
                                st.warning(f"⚠️ You are already enrolled in '{subject['name']}'")
                            else:
                                # Enroll the student
                                enroll_student_to_subject(student_id, subject['subject_id'])
                                st.success(f"✅ Successfully enrolled in '{subject['name']}'!")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error(f"❌ No subject found with code '{join_code.upper()}'")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
            else:
                st.warning('⚠️ Please enter a subject code')
    
    with col2:
        if st.button('Cancel', type='secondary', use_container_width=True):
            st.rerun()