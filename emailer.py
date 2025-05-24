import smtplib
from email.message import EmailMessage
import os
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=".env")


def send_digest_email(to_email: str, subject: str = "Your BatteryBytes Digest"):
    # Load the rendered HTML file
    digest_path = os.path.join(os.getcwd(), "batterybytes_digest.html")
    if not os.path.exists(digest_path):
        print("❌ Digest HTML file not found. Generate it before sending.")
        return

    with open(digest_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Load sender info from .env
    from_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not from_email or not app_password:
        print("❌ Missing SENDER_EMAIL or APP_PASSWORD in .env file.")
        return

    try:
        validate_email(from_email)
    except EmailNotValidError as e:
        print(f"❌ Invalid sender email: {e}")
        return

    # Create email
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content("This email contains HTML content. Please view it in an HTML-compatible client.")
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, app_password)
            smtp.send_message(msg)
        print(f"✅ Digest emailed to {to_email}")
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check your email or app password.")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
