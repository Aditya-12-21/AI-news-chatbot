import os
import json
import random
from datetime import datetime
from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv()

app = Flask(__name__)

# ✅ Correct way
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# ---------------- FALLBACK ----------------
def load_fallback_data():
    try:
        with open("news_data.json", "r") as f:
            return json.load(f)
    except:
        return {"news": [], "topics": []}

# ---------------- INTENT ----------------
def detect_intent(msg):
    msg = msg.lower()

    if "anchor" in msg or "script" in msg:
        return "anchor_script"
    if "news" in msg or "latest" in msg:
        return "news"
    return "general"

# ---------------- PROMPT ----------------
def build_prompt(intent):
    base = f"Today's date is {datetime.now()}."

    if intent == "anchor_script":
        return base + " Speak like a TV news anchor."
    elif intent == "news":
        return base + " Give a proper news report."
    return base + " Answer normally."

# ---------------- API ----------------
def call_api(user_msg, intent):
    if not GROQ_API_KEY:
        raise Exception("API KEY MISSING")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": build_prompt(intent)},
            {"role": "user", "content": user_msg}
        ]
    }

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]

# ---------------- FALLBACK ----------------
def fallback():
    data = load_fallback_data()
    if data["news"]:
        return random.choice(data["news"])["headline"]
    return "Fallback mode running..."

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    intent = detect_intent(user_msg)

    try:
        reply = call_api(user_msg, intent)
        source = "ai"
    except Exception as e:
        print("ERROR:", e)
        reply = fallback()
        source = "fallback"

    return jsonify({
        "reply": reply,
        "intent": intent,
        "source": source
    })

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)