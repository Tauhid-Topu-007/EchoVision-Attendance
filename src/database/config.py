import streamlit as st
from supabase import create_client, Client
import os
import re

def get_supabase_credentials():
    """Get Supabase credentials from multiple sources safely"""
    
    credentials = {}
    
    # Method 1: Try Streamlit secrets (for Streamlit Cloud)
    try:
        if hasattr(st, 'secrets'):
            # Use .get() method to avoid KeyError
            url = st.secrets.get("SUPABASE_URL")
            key = st.secrets.get("SUPABASE_KEY")
            if url and key:
                credentials['url'] = url
                credentials['key'] = key
                print("✅ Credentials found in Streamlit secrets")
                return credentials
    except Exception as e:
        print(f"⚠️ Error reading Streamlit secrets: {e}")
    
    # Method 2: Try environment variables (for local development)
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if url and key:
        credentials['url'] = url
        credentials['key'] = key
        print("✅ Credentials found in environment variables")
        return credentials
    
    # Method 3: Try to read from .streamlit/secrets.toml (for local development)
    try:
        # Try to import tomllib (Python 3.11+) or tomli
        try:
            import tomllib as toml
        except ImportError:
            try:
                import tomli as toml
            except ImportError:
                toml = None
        
        if toml:
            # Check multiple possible paths
            possible_paths = [
                os.path.join(os.path.dirname(__file__), '..', '..', '.streamlit', 'secrets.toml'),
                os.path.join(os.getcwd(), '.streamlit', 'secrets.toml'),
                os.path.join(os.path.dirname(__file__), '.streamlit', 'secrets.toml')
            ]
            
            for secrets_path in possible_paths:
                if os.path.exists(secrets_path):
                    with open(secrets_path, 'rb') as f:
                        secrets = toml.load(f)
                        if 'SUPABASE_URL' in secrets and 'SUPABASE_KEY' in secrets:
                            credentials['url'] = secrets['SUPABASE_URL']
                            credentials['key'] = secrets['SUPABASE_KEY']
                            print(f"✅ Credentials found in {secrets_path}")
                            return credentials
    except Exception as e:
        print(f"⚠️ Error reading secrets.toml: {e}")
    
    # If no credentials found, return None
    return None

# Get credentials
credentials = get_supabase_credentials()