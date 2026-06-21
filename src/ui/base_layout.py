import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            /* Fix: Ensure content is visible */
            .stApp {
                background: linear-gradient(135deg, #5865F2 0%, #4752C4 50%, #363F9E 100%) !important;
                min-height: 100vh !important;
            }
            
            /* Fix: Make sure columns are visible and have proper styling */
            .stApp div[data-testid="stColumn"] {
                background: rgba(255, 255, 255, 0.95) !important;
                padding: 3rem 2.5rem !important;
                border-radius: 2rem !important;
                box-shadow: 0 25px 80px rgba(0, 0, 0, 0.25) !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                margin: 1rem 0 !important;
                position: relative !important;
                z-index: 1 !important;
            }
            
            /* Fix: Make ALL text white on home page */
            .stApp * {
                color: white !important;
            }
            
            /* But keep column text dark for readability */
            .stApp div[data-testid="stColumn"] * {
                color: #1a1a1a !important;
            }
            
            /* Keep button text white in columns */
            .stApp div[data-testid="stColumn"] button * {
                color: white !important;
            }
            
            /* Keep header text in columns dark */
            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2,
            .stApp div[data-testid="stColumn"] h3,
            .stApp div[data-testid="stColumn"] h4,
            .stApp div[data-testid="stColumn"] p,
            .stApp div[data-testid="stColumn"] label {
                color: #1a1a1a !important;
                -webkit-text-fill-color: #1a1a1a !important;
            }
            
            /* Make images in columns visible */
            .stApp div[data-testid="stColumn"] .stImage img {
                border: 4px solid white !important;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15) !important;
            }
        </style>  
    """, unsafe_allow_html=True)
    

def style_background_dashboard():
    st.markdown("""
        <style>
            /* Fix: Ensure dashboard background is visible */
            .stApp {
                background: linear-gradient(135deg, #EEF0FF 0%, #D6DAFF 50%, #C2C7F5 100%) !important;
                min-height: 100vh !important;
            }
            
            /* Ensure all text is dark and visible on dashboard */
            .stApp * {
                color: #1a1a1a !important;
            }
            
            /* But keep button text white */
            .stApp button * {
                color: white !important;
            }
            
            .stApp button[kind="tertiary"] * {
                color: #5865F2 !important;
            }
            
            .stApp button[kind="tertiary"]:hover * {
                color: white !important;
            }
            
            /* Keep headers visible */
            .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                color: #1a1a1a !important;
                -webkit-text-fill-color: #1a1a1a !important;
            }
            
            /* Make images in dashboard visible */
            .stImage img {
                border: 4px solid white !important;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1) !important;
            }
        </style>  
    """, unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
        /* Import Modern Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* ===== BASE STYLES ===== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Hide Streamlit Default Elements */
        #MainMenu, footer, header {
            visibility: hidden !important;
        }
        
        /* Fix: Ensure block container is visible */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            max-width: 1200px !important;
            background: transparent !important;
            min-height: 80vh !important;
        }
        
        /* ===== IMAGE SIZING - GLOBAL CONTROL ===== */
        /* Force all images to be uniform size */
        .stImage img,
        .stImage > div > img,
        .element-container img:not(.st-emotion-cache-*) {
            width: 200px !important;
            height: 200px !important;
            object-fit: cover !important;
            border-radius: 50% !important;
            border: 4px solid white !important;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15) !important;
            transition: all 0.3s ease !important;
        }
        
        /* Hover effect for images */
        .stImage img:hover,
        .stImage > div > img:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.25) !important;
        }
        
        /* Container for images to center them */
        .stImage {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 1rem auto !important;
        }
        
        .stImage > div {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
        }
        
        /* ===== TYPOGRAPHY ===== */
        .stApp {
            color: #1a1a1a !important;
        }
        
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.2 !important;
            margin-bottom: 0.5rem !important;
            color: #1a1a1a !important;
        }
        
        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.2rem !important;
            line-height: 1.2 !important;
            margin-bottom: 0.5rem !important;
            color: #1a1a1a !important;
        }
        
        h3 {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.5rem !important;
            color: #1a1a1a !important;
            margin-bottom: 0.5rem !important;
        }
        
        h4, p, li, label, div, span, .stMarkdown, .stText {
            font-family: 'Outfit', sans-serif !important;
            color: #1a1a1a !important;
        }
        
        p {
            line-height: 1.6 !important;
            font-weight: 400 !important;
        }
        
        /* ===== BUTTONS ===== */
        button {
            border-radius: 2rem !important;
            background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%) !important;
            color: white !important;
            padding: 12px 28px !important;
            border: none !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            font-weight: 600 !important;
            font-family: 'Outfit', sans-serif !important;
            font-size: 0.95rem !important;
            letter-spacing: 0.3px !important;
            box-shadow: 0 4px 15px rgba(88, 101, 242, 0.3) !important;
            cursor: pointer !important;
        }
        
        button:hover {
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 8px 30px rgba(88, 101, 242, 0.4) !important;
        }
        
        button:active {
            transform: translateY(0px) scale(0.98) !important;
        }
        
        /* Secondary Buttons */
        button[kind="secondary"] {
            background: linear-gradient(135deg, #EB459E 0%, #C73D85 100%) !important;
            box-shadow: 0 4px 15px rgba(235, 69, 158, 0.3) !important;
        }
        
        button[kind="secondary"]:hover {
            box-shadow: 0 8px 30px rgba(235, 69, 158, 0.4) !important;
        }
        
        /* Tertiary Buttons (Outlined) */
        button[kind="tertiary"] {
            background: transparent !important;
            color: #5865F2 !important;
            border: 2px solid #5865F2 !important;
            box-shadow: none !important;
        }
        
        button[kind="tertiary"]:hover {
            background: #5865F2 !important;
            color: white !important;
            box-shadow: 0 4px 20px rgba(88, 101, 242, 0.3) !important;
        }
        
        /* Fix: Button text color */
        button * {
            color: white !important;
        }
        
        button[kind="tertiary"] * {
            color: #5865F2 !important;
        }
        
        button[kind="tertiary"]:hover * {
            color: white !important;
        }
        
        /* ===== INPUT FIELDS ===== */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stTextArea > div > div > textarea,
        .stNumberInput > div > div > input {
            border-radius: 1.2rem !important;
            border: 2px solid #E2E8F0 !important;
            padding: 0.75rem 1.2rem !important;
            font-family: 'Outfit', sans-serif !important;
            transition: all 0.3s ease !important;
            background: white !important;
            font-size: 0.95rem !important;
            color: #1a1a1a !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus,
        .stTextArea > div > div > textarea:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #5865F2 !important;
            box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.1) !important;
            outline: none !important;
        }
        
        /* ===== DIVIDERS ===== */
        hr {
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, transparent, #5865F2, #EB459E, #5865F2, transparent) !important;
            margin: 2.5rem 0 !important;
            border-radius: 10px !important;
        }
        
        /* ===== ALERTS ===== */
        .stAlert {
            border-radius: 1.2rem !important;
            border-left: 5px solid #5865F2 !important;
            font-family: 'Outfit', sans-serif !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05) !important;
        }
        
        .stAlert * {
            color: #1a1a1a !important;
        }
        
        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem !important;
            background: rgba(88, 101, 242, 0.08) !important;
            padding: 0.5rem !important;
            border-radius: 2rem !important;
            margin-bottom: 1.5rem !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 1.5rem !important;
            padding: 0.6rem 1.8rem !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            color: #4A5568 !important;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(88, 101, 242, 0.1) !important;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%) !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(88, 101, 242, 0.3) !important;
        }
        
        .stTabs [aria-selected="true"] * {
            color: white !important;
        }
        
        /* ===== DATAFRAME ===== */
        .stDataFrame {
            border-radius: 1.5rem !important;
            overflow: hidden !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
            border: 1px solid #E2E8F0 !important;
        }
        
        .stDataFrame thead tr th {
            background: linear-gradient(135deg, #5865F2 0%, #4752C4 100%) !important;
            color: white !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            padding: 1rem !important;
        }
        
        .stDataFrame tbody tr td {
            color: #1a1a1a !important;
        }
        
        /* ===== CONTAINER ===== */
        .stContainer {
            border-radius: 1.5rem !important;
            border: 2px solid #E2E8F0 !important;
            padding: 2rem !important;
            background: white !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04) !important;
        }
        
        .stContainer * {
            color: #1a1a1a !important;
        }
        
        /* ===== PROGRESS BAR ===== */
        .stProgress > div > div {
            background: linear-gradient(90deg, #5865F2, #EB459E) !important;
            border-radius: 1rem !important;
            height: 8px !important;
        }
        
        /* ===== CAMERA INPUT ===== */
        .stCameraInput {
            border-radius: 1.5rem !important;
            overflow: hidden !important;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1) !important;
            border: 2px solid #E2E8F0 !important;
        }
        
        /* ===== TOAST ===== */
        .stToast * {
            color: #1a1a1a !important;
        }
        
        /* ===== DIALOG AND MODAL VISIBILITY ===== */
        /* Make all dialog content visible */
        .stDialog, .stModal, .element-container:has(.stDialog) {
            background: white !important;
            color: #1a1a1a !important;
        }
        
        .stDialog * {
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
        
        .stDialog input, .stDialog textarea, .stDialog select {
            color: #1a1a1a !important;
            background: white !important;
            border: 2px solid #e0e0e0 !important;
            border-radius: 12px !important;
        }
        
        .stDialog input:focus, .stDialog textarea:focus {
            border-color: #5865F2 !important;
            box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.1) !important;
        }
        
        .stDialog .stCaption {
            color: #666 !important;
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
        }
        
        .stDialog .stWarning {
            background: #fff3cd !important;
        }
        
        .stDialog .stError {
            background: #f8d7da !important;
        }
        
        /* Make buttons in dialogs visible */
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
        
        .stDialog button[kind="secondary"]:hover {
            background: #d0d0d0 !important;
        }
        
        /* Divider in dialogs */
        .stDialog hr {
            border-color: #e0e0e0 !important;
            background: #e0e0e0 !important;
        }
        
        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem !important;
            }
            h2 {
                font-size: 1.8rem !important;
            }
            .block-container {
                padding: 1rem !important;
            }
            button {
                padding: 10px 20px !important;
                font-size: 0.85rem !important;
            }
            /* Smaller images on mobile */
            .stImage img,
            .stImage > div > img {
                width: 150px !important;
                height: 150px !important;
            }
            /* Adjust columns on mobile */
            .stApp div[data-testid="stColumn"] {
                padding: 1.5rem !important;
                margin: 0.5rem 0 !important;
            }
        }
        </style>  
    """, unsafe_allow_html=True)