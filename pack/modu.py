import json
import sqlite3
import csv


def jsonToTable(conn,books_path):
    # 建立資料庫游標
    c = conn.cursor()
    # 創建書籍表格
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  author TEXT NOT NULL,
                  publisher TEXT NOT NULL,
                  year INTEGER NOT NULL)''')
    
    # 讀取JSON檔案並插入資料到資料庫
    with open("books.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for book in data:
            title = book['title']
            author = book['author']
            publisher = book['publisher']
            year = book['year']
            c.execute("INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)", (title, author, publisher, year))
    
    # 儲存資料庫
    conn.commit()
    
    
    # 建立資料庫連接
conn = sqlite3.connect('users.db')
c = conn.cursor()

# 創建使用者表格
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL)''')

# 讀取CSV檔案並插入資料到資料庫
with open('users.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        username = row['username']
        password = row['password']
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# 儲存變更並關閉資料庫連接
conn.commit()
conn.close()

print("資料已成功轉換並存入SQLite3資料庫中。")

# 建立資料庫連接
conn = sqlite3.connect('books.db')
c = conn.cursor()

# 創建書籍表格
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              author TEXT NOT NULL,
              publisher TEXT NOT NULL,
              year INTEGER NOT NULL)''')

# 讀取JSON檔案並插入資料到資料庫
with open('books.json') as json_file:
    data = json.load(json_file)
    for book in data:
        title = book['title']
        author = book['author']
        publisher = book['publisher']
        year = book['year']
        c.execute("INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)", (title, author, publisher, year))

# 儲存變更並關閉資料庫連接
conn.commit()
conn.close()

print("資料已成功轉換並存入SQLite3資料庫中。")

conn = sqlite3.connect('users.db')
c = conn.cursor()

# 創建使用者表格
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL)''')

# 讀取CSV檔案並插入資料到資料庫
with open('users.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        username = row['username']
        password = row['password']
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# 儲存變更並關閉資料庫連接
conn.commit()
conn.close()

print("資料已成功轉換並存入SQLite3資料庫中。")