import sqlite3
import os

# 'instance' klasörünün var olup olmadığını kontrol edin, yoksa oluşturun
os.makedirs('instance', exist_ok=True)

# Veritabanı dosyasını oluşturun
conn = sqlite3.connect('instance/mydatabase.db')
conn.close()
