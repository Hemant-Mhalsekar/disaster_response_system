from flask import Flask, render_template, jsonify
import sqlite3
from models import preprocess_data, categorize_data

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route that renders the dashboard
@app.route('/')
def dashboard():
    conn = get_db_connection()
    disaster_data = conn.execute('SELECT * FROM disaster_reports').fetchall()
    conn.close()
    return render_template('dashboard.html', disaster_data=disaster_data)

# API route for real-time data aggregation (mocked for simplicity)
@app.route('/api/collect_data')
def collect_data():
    # Mock data collection from external sources
    raw_data = [
        {"source": "Twitter", "text": "Flood in City A!", "location": "City A"},
        {"source": "News", "text": "Earthquake hits City B", "location": "City B"},
    ]
    
    # Preprocess and categorize data
    processed_data = preprocess_data(raw_data)
    categorized_data = categorize_data(processed_data)
    
    # Store in database
    conn = get_db_connection()
    for entry in categorized_data:
        conn.execute('INSERT INTO disaster_reports (source, text, category, location) VALUES (?, ?, ?, ?)', 
                     (entry['source'], entry['text'], entry['category'], entry['location']))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "Data collected and categorized!"})

if __name__ == '__main__':
    app.run(debug=True)
