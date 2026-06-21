import streamlit as st
from src.database.db import create_attendance
import time

def show_attendance_result(df, logs):
    """Display attendance results with proper styling"""
    
    # Force visibility with inline styles
    st.markdown("""
    <style>
    .stDialog, .stModal {
        background: white !important;
        color: #1a1a1a !important;
        padding: 1.5rem !important;
        border-radius: 1.5rem !important;
        max-width: 900px !important;
    }
    .stDialog *, .stModal * {
        color: #1a1a1a !important;
    }
    .stDialog h1, .stDialog h2, .stDialog h3, .stDialog h4 {
        color: #1a1a1a !important;
        -webkit-text-fill-color: #1a1a1a !important;
    }
    .stDialog p, .stDialog .stWrite, .stDialog .stCaption {
        color: #1a1a1a !important;
    }
    .stDialog .stDataFrame, .stModal .stDataFrame {
        background: white !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06) !important;
    }
    .stDialog .stDataFrame thead tr th {
        background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
    }
    .stDialog .stDataFrame tbody tr td {
        color: #1a1a1a !important;
        padding: 10px 16px !important;
        border-bottom: 1px solid #f0f0f0 !important;
    }
    .stDialog .stDataFrame tbody tr:hover {
        background: rgba(88, 101, 242, 0.05) !important;
    }
    .stDialog .stDataFrame tbody tr:last-child td {
        border-bottom: none !important;
    }
    .stDialog button, .stModal button {
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    .stDialog button:hover, .stModal button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(88, 101, 242, 0.3) !important;
    }
    .stDialog button *, .stModal button * {
        color: white !important;
    }
    .stDialog button[kind="secondary"], .stModal button[kind="secondary"] {
        background: #e0e0e0 !important;
        color: #1a1a1a !important;
    }
    .stDialog button[kind="secondary"] *, .stModal button[kind="secondary"] * {
        color: #1a1a1a !important;
    }
    .stDialog button[kind="secondary"]:hover, .stModal button[kind="secondary"]:hover {
        background: #d0d0d0 !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
    }
    .stDialog .stAlert, .stModal .stAlert {
        background: #f8f9fa !important;
        border-radius: 12px !important;
        border-left: 4px solid #5865F2 !important;
        padding: 12px 16px !important;
    }
    .stDialog .stAlert *, .stModal .stAlert * {
        color: #1a1a1a !important;
    }
    .stDialog .stSuccess, .stModal .stSuccess {
        background: #d4edda !important;
        border-left: 4px solid #28a745 !important;
    }
    .stDialog .stError, .stModal .stError {
        background: #f8d7da !important;
        border-left: 4px solid #dc3545 !important;
    }
    .stDialog hr, .stModal hr {
        border-color: #e0e0e0 !important;
        margin: 1.5rem 0 !important;
    }
    .stToast {
        background: white !important;
        border-radius: 12px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15) !important;
    }
    .stToast * {
        color: #1a1a1a !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Dialog content
    st.markdown("""
    <div style="padding: 0.5rem 0;">
        <h3 style="color: #1a1a1a; margin-bottom: 0.5rem;">📊 Attendance Reports</h3>
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.5rem;">Please review attendance before confirming.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display dataframe
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Name": st.column_config.TextColumn("Name", width="medium"),
            "ID": st.column_config.TextColumn("ID", width="small"),
            "Source": st.column_config.TextColumn("Source", width="medium"),
            "Status": st.column_config.TextColumn("Status", width="medium"),
        }
    )
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🗑️ Discard", type="secondary", use_container_width=True):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()
    
    with col2:
        if st.button("✅ Confirm & Save", type="primary", use_container_width=True):
            try:
                with st.spinner("Saving attendance..."):
                    create_attendance(logs)
                    st.toast("✅ Attendance saved successfully!", icon="✅")
                    st.session_state.attendance_images = []
                    st.session_state.voice_attendance_results = None
                    time.sleep(0.5)
                    st.rerun()
            except Exception as e:
                st.error(f"❌ Sync failed: {str(e)}")


@st.dialog("📊 Attendance Reports")
def attendance_result_dialog(df, logs):
    """Dialog for showing attendance results"""
    show_attendance_result(df, logs)