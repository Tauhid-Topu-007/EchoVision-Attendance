import streamlit as st
from supabase import create_client, Client
import os
import re

def get_supabase_credentials():
    """Get Supabase credentials from multiple sources safely"""
    
    # Method 1: Try Streamlit secrets (for Streamlit Cloud)
    try:
        if hasattr(st, 'secrets'):
            # Use .get() method to avoid KeyError
            url = st.secrets.get("SUPABASE_URL")
            key = st.secrets.get("SUPABASE_KEY")
            if url and key:
                print("✅ Credentials found in Streamlit secrets")
                return url, key
    except Exception as e:
        print(f"⚠️ Error reading Streamlit secrets: {e}")
    
    # Method 2: Try environment variables (for local development)
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if url and key:
        print("✅ Credentials found in environment variables")
        return url, key
    
    # If no credentials found, return None
    return None, None

# Get credentials
raw_url, key = get_supabase_credentials()

# Handle missing credentials
if raw_url is None or key is None:
    error_msg = """
    ⚠️ Supabase credentials not found!

    Please configure your Supabase credentials using one of these methods:

    1. **Streamlit Cloud (Production):**
       - Go to your app → Manage app → Settings → Secrets
       - Add:

    2. **Local Development:**
       - Create .streamlit/secrets.toml with the same content

    3. **Environment Variables:**
       - Set SUPABASE_URL and SUPABASE_KEY in your environment
    """
    
    try:
        st.error("⚠️ Supabase Credentials Required")
        st.markdown(error_msg)
        st.stop()
    except:
        print(error_msg)
        raise ValueError("Supabase credentials not found!")

# Clean the URL - remove /rest/v1/ if present
try:
    url = re.sub(r'/rest/v1/?$', '', raw_url)
    url = re.sub(r'/$', '', url)
    print(f"✅ Using Supabase URL: {url}")
except Exception as e:
    try:
        st.error(f"⚠️ Error processing URL: {str(e)}")
        st.stop()
    except:
        print(f"⚠️ Error processing URL: {str(e)}")
        raise

# Create Supabase client
try:
    supabase: Client = create_client(url, key)
    print("✅ Supabase client created successfully")
except Exception as e:
    try:
        st.error(f"⚠️ Failed to create Supabase client: {str(e)}")
        st.stop()
    except:
        print(f"⚠️ Failed to create Supabase client: {str(e)}")
        raise

# Export the supabase client
__all__ = ['supabase']

print("=" * 50)
print("✅ Supabase Configuration Complete")
print("=" * 50)