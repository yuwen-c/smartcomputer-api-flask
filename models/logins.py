import sqlite3
from config import Config

DATABASE_PATH = Config.DATABASE_PATH

def get_db_connection():
  return sqlite3.connect(DATABASE_PATH)

def insert_user(name, email, password):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO login (name, email, hash) VALUES (?, ?, ?)', (name, email, password))
    conn.commit()
    cursor.close()
    conn.close()
    return ({
      'status': 'success',
      'name': name,
      'email': email
    })
  except Exception as e:
    conn.rollback()
    print(e)
    return ({'error': 'An error occurred while registering user'})
  
def get_user(email):
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM login WHERE email = ?', (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
  except Exception as e:
    print(e)
    return None

# 需要哪些功能？註冊、登入、
# 登入：取得該名user(用email)，比對密碼是否正確

def login_user(email, password):
  user = get_user(email)
  print(user)
  if not user:
    return
  if user[2] == password:
    return user
  return
