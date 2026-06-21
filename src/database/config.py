import os
from dotenv import load_dotenv
from supabase import create_client, Client
import streamlit as st

# Load environment variables
load_dotenv()

# Try to get from secrets first (for Streamlit Cloud), fallback to env variables
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except (KeyError, AttributeError):
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validate that variables exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials not found. Please set SUPABASE_URL and SUPABASE_KEY in secrets or .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)