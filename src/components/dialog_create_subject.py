import streamlit as st
from src.database.db import create_subject

@st.dialog("📝 Create New Subject")
def create_subject_dialog(teacher_id):
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
    .stDialog input::placeholder {
        color: #999 !important;
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
    .stDialog .stAlert {
        background: #f8f9fa !important;
        border-radius: 12px !important;
    }
    .stDialog .stAlert * {
        color: #1a1a1a !important;
    }
    .stDialog .stWarning {
        background: #fff3cd !important;
        border-left: 4px solid #ffc107 !important;
    }
    .stDialog .stError {
        background: #f8d7da !important;
        border-left: 4px solid #dc3545 !important;
    }
    .stDialog .stSuccess {
        background: #d4edda !important;
        border-left: 4px solid #28a745 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 0.5rem 0;">
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.5rem;">
            Enter the details of the new subject
        </p>
    </div>
    """, unsafe_allow_html=True)

    sub_id = st.text_input("📚 Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("📖 Subject Name", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("📋 Section", placeholder="e.g. A")

    st.divider()

    if st.button("✅ Create Subject Now", type='primary', use_container_width=True):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast(f"✅ Subject '{sub_name}' Created Successfully!")
                time.sleep(0.5)
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please fill all the fields")