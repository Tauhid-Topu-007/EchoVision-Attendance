import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    """Subject card using pure Streamlit components - Most Reliable"""
    
    # Card using native Streamlit components
    with st.container():
        # Use columns for header
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"### {name}")
            st.caption(f"Code: `{code}` | Section: {section}")
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%); 
                        color: white; 
                        padding: 4px 12px; 
                        border-radius: 50px; 
                        text-align: center; 
                        font-size: 0.75rem; 
                        font-weight: 600;
                        display: inline-block;
                        float: right;">
                Active
            </div>
            """, unsafe_allow_html=True)
        
        # Stats using columns
        if stats:
            cols = st.columns(len(stats))
            for idx, (icon, label, value) in enumerate(stats):
                with cols[idx]:
                    st.metric(
                        label=f"{icon} {label}",
                        value=value,
                        label_visibility="visible"
                    )
        
        # Divider
        st.divider()
        
        # Footer callback
        if footer_callback:
            footer_callback()