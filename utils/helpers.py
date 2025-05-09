import hashlib
import sqlite3
import os

def hash_password(password):
    """
    Hash a password using SHA-256
    """
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_database():
    """
    Create database and table if they don't exist
    """
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'passwords.db')
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    
    return db_path
    
def add_password(db_path, website, username, password):
    """
    Add a new password entry to the database
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    
    cursor.execute('''
    INSERT INTO passwords (website, username, password_hash)
    VALUES (?, ?, ?)
    ''', (website, username, password_hash))
    
    conn.commit()
    conn.close()
    
def get_all_passwords(db_path):
    """
    Retrieve all passwords from the database
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, website, username, password_hash, date_added FROM passwords')
    results = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return results

def delete_password(db_path, password_id):
    """
    Delete a password entry by ID
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM passwords WHERE id = ?', (password_id,))
    
    conn.commit()
    conn.close()