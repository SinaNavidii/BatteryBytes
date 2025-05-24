import json
import os

CONFIG_PATH = os.path.join(os.getcwd(), "batterybytes_config.json")


def setup_user_config():
    print("🔧 BatteryBytes: Initial Configuration")

    email = input("Enter your email address: ").strip()
    topics = input("Enter comma-separated battery topics of interest (e.g., solid-state, SEI, fast charging): ").strip()
    frequency = input("Digest frequency? (daily / weekly): ").strip().lower()

    config = {
        "email": email,
        "topics": [t.strip() for t in topics.split(",") if t.strip()],
        "frequency": frequency
    }

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

    print(f"✅ Configuration saved to {CONFIG_PATH}")

def load_user_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("User config not found. Run `batterybytes init` first.")

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)
