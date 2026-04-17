from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import sqlite3
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app) # 允许前端请求后端

# 使用最新的 Google GenAI SDK
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

# 初始化数据库
def init_db():
    conn = sqlite3.connect('chatbot_sessions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS session_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            user_query TEXT NOT NULL,
            ai_response TEXT NOT NULL,
            query_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/chat', methods=['POST'])
def chat():
    if not client:
        return jsonify({"error": "API Key is missing"}), 500

    data = request.json
    user_message = data.get('message', '')
    student_id = data.get('student_id', 'guest_student') 
    
    # 构建 Socratic 提示词
    system_prompt = (
        "You are an educational AI assistant for secondary school students in Hong Kong. "
        "IMPORTANT RULE: Use the Socratic method. DO NOT give direct answers. "
        "Instead, ask guiding questions to help the student find the answer themselves. "
        f"Student question: {user_message}"
    )

    try:
        # 使用新版 SDK 调用大模型
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=system_prompt
        )
        ai_reply = response.text

        # 记录到真实的数据库
        conn = sqlite3.connect('chatbot_sessions.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO session_logs (student_id, user_query, ai_response) VALUES (?, ?, ?)',
            (student_id, user_message, ai_reply)
        )
        conn.commit()
        conn.close()

        return jsonify({"status": "success", "response": ai_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "response": "Sorry, the AI is taking a short break."}), 500

if __name__ == '__main__':
    print("Starting REAL AI Chatbot Backend Server on port 5000 (Upgraded SDK)...")
    app.run(debug=True, port=5000)
