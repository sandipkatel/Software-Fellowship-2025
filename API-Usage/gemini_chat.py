import requests

# Paste your API key here directly (for testing only — not safe for production)
API_KEY = "your-api-key-here"  # 🔐 Replace this with your Gemini API key

def ask_gemini(question):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    data = {"contents": [{"parts": [{"text": question}]}]}
    
    try:
        res = requests.post(url, json=data)
        return res.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "❌ Error. Check your API key or internet."

print("💬 Gemini Chat (type 'quit' to exit)")

while True:
    q = input("You: ").strip()
    if q.lower() == "quit":
        break
    if not q:
        continue
    print("AI:", ask_gemini(q))
