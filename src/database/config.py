import streamlit as st
from supabase import create_client, Client
import os

# Try to load from secrets first (Streamlit Cloud)
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except (KeyError, AttributeError):
    # Fallback to environment variables (local development)
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # If still not found, try to load from .env file
    if not SUPABASE_URL or not SUPABASE_KEY:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            SUPABASE_URL = os.getenv("SUPABASE_URL")
            SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        except ImportError:
            pass

# Validate credentials
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Supabase credentials not found! Please set SUPABASE_URL and SUPABASE_KEY in:\n"
        "1. .streamlit/secrets.toml (for Streamlit), or\n"
        "2. .env file (for local development), or\n"
        "3. Environment variables"
    )

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)