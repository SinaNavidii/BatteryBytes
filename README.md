# 🔋 BatteryBytes

BatteryBytes is a simple tool that sends you a digest of:

- 📄 Recent battery research papers (from arXiv)  
- 📦 Trending GitHub projects  
- 📰 Battery-related news articles  

All delivered as a clean HTML email, weekly or on demand.

---

## 💡 Why

I built this to keep up with battery research without checking multiple sources. It’s focused on batteries, but you can customize it for any research area. Thought it might be useful to others, so I made it public.

---

## 🚀 How to Use

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/batterybytes.git
   cd batterybytes
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
3. **Create a `.env` file**  
   ```env
   GITHUB_TOKEN=your_github_token
   SENDER_EMAIL=your_email@gmail.com
   APP_PASSWORD=your_gmail_app_password
4. **Run the Streamlit app**  
   ```bash
   streamlit run streamlit_app.py
5. **Or use the CLI**  
   ```bash
   python cli.py send
---
## 🧪 Customize

Change the topic keywords in the Streamlit app or `batterybytes_config.json` to monitor any field.

---
## 📬 License

MIT License — feel free to fork it and build on top of it!
