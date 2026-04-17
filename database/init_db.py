import sqlite3

def setup_database():
    """
    Initializes the SQLite database for the AI Chatbot project.
    Tracks user sessions to prevent exceeding the API budget (Risk Matrix R5).
    """
    conn = sqlite3.connect('chatbot_sessions.db')
    cursor = conn.cursor()

    # Create table for user session logging
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS session_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            query_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            token_usage INTEGER,
            hallucination_flag BOOLEAN DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()
    print("Database 'chatbot_sessions.db' initialized successfully.")

if __name__ == '__main__':
    setup_database()