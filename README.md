# 🎙️ AI News Simulation Platform

A full-stack AI-powered news chatbot that dynamically generates news reports,
anchor broadcast scripts, and answers any user query using the Anthropic Claude API.

---

## ⚡ Quick Start (5 Steps)

### Step 1 — Clone / Unzip the project
```
ai_news_platform/
├── app.py
├── news_data.json
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

### Step 2 — Create a Python virtual environment
```bash
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set your Anthropic API key
Get a free key at https://console.anthropic.com

```bash
# Windows (CMD):
set ANTHROPIC_API_KEY=sk-ant-...your-key-here...

# Windows (PowerShell):
$env:ANTHROPIC_API_KEY="sk-ant-...your-key-here..."

# Mac / Linux:
export ANTHROPIC_API_KEY="sk-ant-...your-key-here..."
```

> ⚠️ If you skip this step, the platform runs in **Fallback Mode** using local JSON data.

### Step 5 — Run the Flask server
```bash
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

---

## 🧪 Example Queries to Try

| Query | Intent Detected |
|---|---|
| "Tell me latest AI news" | 📰 NEWS |
| "Give anchor script for sports news" | 🎙️ ANCHOR |
| "What is machine learning?" | 💬 GENERAL |
| "Breaking news on climate change" | 📰 NEWS |
| "How does artificial intelligence work?" | 💬 GENERAL |
| "Read the news like an anchor" | 🎙️ ANCHOR |

---

## 🏗️ Architecture Overview

| Component | File | Role |
|---|---|---|
| **Backend** | `app.py` | Flask server, intent detection, API calls, fallback logic |
| **Frontend** | `templates/index.html` | Chat UI, JavaScript, event handling |
| **Styling** | `static/style.css` | Dark broadcast-room aesthetic |
| **Fallback Data** | `news_data.json` | Offline articles and topic explanations |

---

## 🔧 How Each Component Works

### `app.py` — Backend Brain
- **`detect_intent()`**: Scans user message for trigger keywords to classify as `news`, `anchor_script`, or `general`
- **`build_system_prompt()`**: Returns a specialized system prompt that shapes Claude's response style
- **`call_ai_api()`**: Sends the user message + system prompt to the Anthropic Claude API
- **`generate_fallback_response()`**: Searches `news_data.json` for matching articles when API is unavailable
- **`/chat` route**: Orchestrates the full request → intent → AI → response pipeline

### `index.html` — Frontend Intelligence
- Auto-resizing textarea with character count
- Typing animation while awaiting AI response
- `detect_intent` badge shown on every AI reply
- Source pill shows whether response came from AI or fallback
- Live clock and news ticker in the header
- Quick-query sidebar buttons for one-click demos

### `news_data.json` — Fallback Dataset
- 7 realistic news articles with keywords for fuzzy matching
- 4 topic explanations for common knowledge queries
- Used **only** when the AI API is unavailable

---

## 🔒 Security Notes
- API key is read from environment variable — never hardcoded
- All user input is length-limited (1000 chars)
- Flask runs in debug mode only locally; use Gunicorn for production

---

*Academic Demonstration Build — AI News Simulation Platform*
