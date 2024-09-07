import os
import sqlite3
from flask import current_app

def init_db():
    db_path = os.path.join('instance', 'mydatabase.db')
    
    # Veritabanı dosyasını oluşturun
    if not os.path.isfile(db_path):
        open(db_path, 'w').close()
    
    # SQLite bağlantısını kur
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Tablo oluşturma komutlarını çalıştır
    cursor.executescript('''
    -- User tablosunu oluştur
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );

    -- Post tablosunu oluştur
    CREATE TABLE IF NOT EXISTS post (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES user(id)
    );

    -- Comment tablosunu oluştur
    CREATE TABLE IF NOT EXISTS comment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY(post_id) REFERENCES post(id)
    );

    -- Reaction tablosunu oluştur
    CREATE TABLE IF NOT EXISTS reaction (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY(post_id) REFERENCES post(id)
    );
    ''')

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        init_db()
