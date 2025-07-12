import requests
import os
from dotenv import load_dotenv
load_dotenv()

def ask_gemini(question):
    """Ask Gemini AI a question and get response"""
    
    # Get API key from environment variable

    API_KEY = os.getenv('GEMINI_API_KEY')

    if not API_KEY:
        return "API key not found. Please set GEMINI_API_KEY environment variable."
    
    # Gemini API endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    
    # Prepare the data to send
    data = {
        "contents": [{
            "parts": [{
                "text": question
            }]
        }]
    }
    
    try:
        # Send request to Gemini
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            # Get the AI's answer
            if 'candidates' in result:
                answer = result['candidates'][0]['content']['parts'][0]['text']
                return answer
            else:
                return "Sorry, I couldn't understand that."
        else:
            return f"Error: {response.status_code}. Check your API key."
            
    except requests.exceptions.RequestException:
        return "Network error. Check your internet connection."

def main():
    """Main chat program"""
    
    print("🤖 Simple AI Chat with Gemini")
    print("Type 'quit' to exit")
    print("-" * 30)
    
    # Chat loop
    while True:
        # Get user input
        user_question = input("\nYou: ").strip()
        
        # Check if user wants to quit
        if user_question.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        # Skip empty messages
        if not user_question:
            continue
        
        # Get AI response
        print("🤖 Thinking...")
        ai_response = ask_gemini(user_question)
        
        # Show AI response
        print(f"AI: {ai_response}")

# Run the program
if __name__ == "__main__":
    main()