from datetime import datetime 
import sqlite3 

def ingest_Log(source, event_type, message, risk_score = 0):
    conn = sqilte3.connect("siem.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO logs (timestamp, source, event_type, message, risk_score)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.now().isoformat(), source, event_type, message, riks_score))

    conn.commit()
    conn.close()
