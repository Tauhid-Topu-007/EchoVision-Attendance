import streamlit as st
import segno
import io

@st.dialog("🔗 Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    # Force visibility
    st.markdown("""
    <style>
    .stDialog, .stModal {
        background: white !important;
        color: #1a1a1a !important;
        padding: 1.5rem !important;
        border-radius: 1.5rem !important;
        max-width: 800px !important;
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
    .stDialog .stCodeBlock {
        background: #f8f9fa !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    .stDialog code {
        color: #1a1a1a !important;
        background: #f0f0f0 !important;
        padding: 4px 8px !important;
        border-radius: 6px !important;
    }
    .stDialog .stImage {
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    .stDialog .stAlert {
        background: #f8f9fa !important;
        border-radius: 12px !important;
        border-left: 4px solid #5865F2 !important;
    }
    .stDialog .stAlert * {
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
    </style>
    """, unsafe_allow_html=True)

    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.markdown(f"""
    <div style="text-align: center; padding: 0.5rem 0;">
        <h3 style="color: #1a1a1a;">🔗 Share: {subject_name}</h3>
        <p style="color: #666; font-size: 0.95rem;">Scan QR code or copy link to share</p>
    </div>
    """, unsafe_allow_html=True)

    # Generate QR Code
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("💡 Copy this link to share on WhatsApp or Email")
        
        if st.button("📋 Copy Link", type="primary", use_container_width=True):
            st.toast("✅ Link copied to clipboard!")
    
    with col2:
        st.markdown("### 📱 Scan to Join")
        st.image(out.getvalue(), caption="QR Code for class joining", use_container_width=True)