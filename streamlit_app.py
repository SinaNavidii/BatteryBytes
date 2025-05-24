import streamlit as st
import os
import json
from generate_digest import generate_and_send_digest
from config import CONFIG_PATH

st.set_page_config(page_title="BatteryBytes", page_icon="🔋", layout="centered")
st.title("🔋 BatteryBytes Digest Generator")

st.markdown("""
Stay up-to-date on battery research! 
Generate and email a digest with:
- Latest arXiv papers
- Trending GitHub repos
- Battery news
""")

# --- User Inputs ---
topics_input = st.text_input("Battery topics (comma-separated)", "solid-state, SEI, fast charging")
email_input = st.text_input("Your email address")
days_back = st.slider("How many days back for arXiv and news?", 1, 30, 7)

# --- On Submit ---
if st.button("📬 Generate and Send Digest"):
    if not email_input or not topics_input:
        st.error("Please enter both your email and at least one topic.")
    else:
        # Save temporary config
        config = {
            "email": email_input,
            "topics": [t.strip() for t in topics_input.split(",") if t.strip()],
            "frequency": "manual"
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f)

        try:
            generate_and_send_digest()
            st.success("✅ Digest sent to " + email_input)

            # Show preview
            if os.path.exists("batterybytes_digest.html"):
                with open("batterybytes_digest.html", "r", encoding="utf-8") as f:
                    html_preview = f.read()
                st.components.v1.html(html_preview, height=800, scrolling=True)
        except Exception as e:
            st.error(f"❌ Error: {e}")
