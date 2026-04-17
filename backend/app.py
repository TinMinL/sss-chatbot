from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import sqlite3
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app) # 允许前端请求后端

# 配置 DeepSeek API (使用 OpenAI 兼容客户端)
api_key = os.getenv("DEEPSEEK_API_KEY")
if api_key:
    # DeepSeek 的基础 URL 是 https://api.deepseek.com
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
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
    )

    try:
        # 调用 DeepSeek 大模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response.choices[0].message.content

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
    print("Starting REAL AI Chatbot Backend Server on port 5000 (Powered by DeepSeek)...")
    app.run(debug=True, port=5000)
