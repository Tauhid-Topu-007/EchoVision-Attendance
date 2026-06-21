import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
import pandas as pd
from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime

@st.dialog("🎤 Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
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
    .stDialog label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    .stDialog .stAudioInput {
        border-radius: 12px !important;
        border: 2px dashed #5865F2 !important;
        padding: 1.5rem !important;
        background: rgba(88, 101, 242, 0.05) !important;
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
        border-left: 4px solid #5865F2 !important;
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
    .stDialog hr {
        border-color: #e0e0e0 !important;
    }
    .stDialog .stDataFrame {
        background: white !important;
        border-radius: 12px !important;
    }
    .stDialog .stDataFrame thead tr th {
        background: #5865F2 !important;
        color: white !important;
    }
    .stDialog .stDataFrame tbody tr td {
        color: #1a1a1a !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 0.5rem 0;">
        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.5rem;">
            🎙️ Record audio of students saying "I am present". AI will recognize the students.
        </p>
    </div>
    """, unsafe_allow_html=True)

    audio_data = st.audio_input("🎤 Record classroom audio")

    st.divider()

    if st.button('🔍 Analyze Audio', use_container_width=True, type='primary'):
        if audio_data:
            with st.spinner('🔄 Processing Audio data...'):
                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('⚠️ No students enrolled in this course')
                    return
                
                candidates_dict = {
                    s['students']['student_id']: s['students']['voice_embedding'] 
                    for s in enrolled_students if s['students'].get('voice_embedding')
                }

                if not candidates_dict:
                    st.error('❌ No enrolled students have voice profiles registered')
                    return
                
                audio_bytes = audio_data.read()
                detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

                results, attendance_to_log = [], []

                current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                for node in enrolled_students:
                    student = node['students']
                    score = detected_scores.get(student['student_id'], 0.0)
                    is_present = bool(score > 0)

                    results.append({
                        "Name": student['name'],
                        "ID": student['student_id'],
                        "Source": f"{score:.2f}" if is_present else "-",
                        "Status": "✅ Present" if is_present else "❌ Absent"
                    })

                    attendance_to_log.append({
                        'student_id': student['student_id'],
                        'subject_id': selected_subject_id,
                        'timestamp': current_timestamp,
                        'is_present': bool(is_present)
                    })
                
                st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)
                st.success("✅ Voice analysis complete!")
                st.rerun()
        else:
            st.warning("⚠️ Please record audio first!")

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)