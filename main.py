from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import random
import time

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION (APIs & PROXIES) ---
# यहाँ आप अपनी असली API Keys बाद में बदल सकते हैं
CAPTCHA_API_KEY = "your_2captcha_key_here"
TEMP_MAIL_URL = "https://www.1secmail.com/api/v1/"

# प्रॉक्सी लिस्ट (Render पर बैन से बचने के लिए)
PROXIES = [
    "http://uitliupr:1vea0shlqnaf@142.111.48.253:7030",
    "http://uitliupr:1vea0shlqnaf@23.95.150.145:6114"
]

# --- HELPER FUNCTIONS ---

def get_random_bot_email():
    """स्वचालित रूप से बॉट के लिए ईमेल बनाना"""
    try:
        res = requests.get(f"{TEMP_MAIL_URL}?action=genRandomMailbox&count=1").json()
        return res[0]
    except:
        return f"niva_bot_{random.randint(1000,9999)}@gmail.com"

# --- ROUTES ---

@app.route('/')
def health_check():
    return {
        "status": "online",
        "server": "Niva Cloud Engine v4",
        "message": "System is ready for Instagram Operations"
    }

@app.route('/start-bot', methods=['POST'])
def start_bot():
    try:
        data = request.json
        target = data.get('username')
        service_type = data.get('type', 'Followers')
        quantity = int(data.get('quantity', 0))

        if not target or quantity <= 0:
            return jsonify({"status": "error", "message": "Invalid Target or Quantity"}), 400

        # --- INSTAGRAM PROCESS SIMULATION ---
        # 1. प्रॉक्सी चयन
        proxy = random.choice(PROXIES)
        
        # 2. बॉट अकाउंट वेरिफिकेशन सिमुलेशन
        bot_email = get_random_bot_email()
        
        # 3. ऑपरेशन लॉजिक (Follow/Like/Comment)
        # यहाँ असली इंस्टाग्राम API रिक्वेस्ट जाती है
        time.sleep(1) # सर्वर प्रोसेसिंग टाइम

        return jsonify({
            "status": "success",
            "message": f"Successfully initiated {service_type} for @{target}",
            "data": {
                "order_id": random.randint(100000, 999999),
                "total_sent": quantity,
                "bot_used": bot_email,
                "proxy_node": proxy.split('@')[1],
                "status": "Delivering"
            }
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- INSTAGRAM LOGIN SIMULATION ROUTE ---
@app.route('/insta-login', methods=['POST'])
def insta_login():
    data = request.json
    # यहाँ आप अपना इंस्टाग्राम लॉगिन हैंडलिंग कोड जोड़ सकते हैं
    return jsonify({
        "status": "connected",
        "session_id": f"sid_{random.getrandbits(32)}",
        "message": "Instagram Account Linked Successfully!"
    })

if __name__ == "__main__":
    # Render के लिए पोर्ट 10000 जरूरी है
    app.run(host="0.0.0.0", port=10000)
          
