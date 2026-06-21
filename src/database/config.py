import streamlit as st
from supabase import create_client, Client
import os
import re

def get_supabase_credentials():
    """Get Supabase credentials from multiple sources safely"""
    
    # Try Streamlit secrets
    try:
        if hasattr(st, 'secrets'):
            if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
                return st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"]
    except:
        pass
    
    # Try environment variables
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if url and key:
        return url, key
    
    # Try to read from .streamlit/secrets.toml
    try:
        import tomllib
        secrets_path = os.path.join(os.getcwd(), '.streamlit', 'secrets.toml')
        if os.path.exists(secrets_path):
            with open(secrets_path, 'rb') as f:
                secrets = tomllib.load(f)
                if 'SUPABASE_URL' in secrets and 'SUPABASE_KEY' in secrets:
                    return secrets['SUPABASE_URL'], secrets['SUPABASE_KEY']
    except:
        pass
    
    # If no credentials found, show error
    if hasattr(st, 'error'):
        st.error("""
        ⚠️ Supabase credentials not found!
        
        Please set your credentials in:
        1. Streamlit Cloud Secrets (Settings → Secrets)
        2. .streamlit/secrets.toml (local)
        3. Environment variables (SUPABASE_URL, SUPABASE_KEY)
        """)
        st.stop()
    else:
        raise ValueError("Supabase credentials not found!")

# Get credentials
raw_url, key = get_supabase_credentials()

# Clean URL
url = re.sub(r'/rest/v1/?$', '', raw_url)
url = re.sub(r'/$', '', url)

# Create client
supabase: Client = create_client(url, key)