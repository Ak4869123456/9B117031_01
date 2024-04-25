import os
import json
import sqlite3
import csv

# 建立資料庫連接
conn = sqlite3.connect('users.db')
c = conn.cursor()

# 指定資料庫文件的路徑
db_path = 'library.db'

# 檢查文件是否存在
if os.path.exists(db_path):
    print(f"資料庫文件 '{db_path}' 已存在")
else:
    print(f"資料庫文件 '{db_path}' 不存在")
    

# 讀取使用者檔案
users_file = 'users.csv'
users = read_users_file(users_file) # type: ignore


with open('users.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        username = row['username']
        password = row['password']
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))


with open('books.json') as json_file:
    data = json.load(json_file)
    for book in data:
        title = book['title']
        author = book['author']
        publisher = book['publisher']
        year = book['year']
        c.execute("INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)", (title, author, publisher, year))
   

# 連接到SQLite數據庫
conn = sqlite3.connect('library.db')
c = conn.cursor()
with open('books.json', 'r', encoding='utf-8') as file:
  list_books_data = json.load(file)
with open('books.json', 'w', encoding='utf-8') as file:
    json.dump(list_books_data, file, ensure_ascii=False, indent=4)


# 登錄函數
def login():
    while True:
        username = input("請輸入帳號:")
        password = input("請輸入密碼: ")
        c.execute("SELECT * FROM users where username=? AND password=?", (username, password))
        users = c.fetchone()
        if users:
            print("登錄成功!")
            return
        else:
            print("帳號或密碼錯誤,請重新輸入")
# 顯示選單
def show_menu():
    while True:
        print("\n==== 圖書管理系統 ====")
        print("1. 新增圖書")
        print("2. 刪除圖書")
        print("3. 修改圖書資訊")
        print("4. 查詢圖書")
        print("5. 圖書清單")
        choice = input("請選擇操作(Enter退出): ")
        if choice == "":
            break
        elif choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            search_book()
        elif choice == "5":
            list_books()
        else:
            print("無效的選擇")

# 新增圖書
def add_book():
    title = input("請輸入書名: ")
    author = input("請輸入作者: ")
    publisher = input("請輸入出版社: ")
    year = input("請輸入出版年份: ")
    c.execute("INSERT INTO books (title, author, publisher, year) VALUES (?, ?, ?, ?)", (title, author, publisher, year))
    conn.commit()
    print("新增成功!")

# 刪除圖書
def delete_book():
    title = input("請輸入要刪除的書名: ")
    c.execute("DELETE FROM books WHERE title=?", (title,))
    conn.commit()
    print("刪除成功!")

# 修改圖書資訊
def update_book():
    title = input("請輸入要修改的書名: ")
    new_title = input("請輸入新書名(直接按Enter保留原書名): ") or None
    new_author = input("請輸入新作者(直接按Enter保留原作者): ") or None
    new_publisher = input("請輸入新出版社(直接按Enter保留原出版社): ") or None
    new_year = input("請輸入新出版年份(直接按Enter保留原年份): ") or None
    update_data = []
    if new_title:
        update_data.append(f"title='{new_title}'")
    if new_author:
        update_data.append(f"author='{new_author}'")
    if new_publisher:
        update_data.append(f"publisher='{new_publisher}'")
    if new_year:
        update_data.append(f"year={new_year}")
    update_query = "UPDATE books SET " + ", ".join(update_data) + " WHERE title=?"
    c.execute(update_query, (title,))
    conn.commit()
    print("修改成功!")

# 查詢圖書
def search_book():
    keyword = input("請輸入查詢關鍵字: ")
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR publisher LIKE ?", (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    books = c.fetchall()
    if books:
        print("查詢結果:")
        for book in books:
            print(f"書名: {book[0]}, 作者: {book[1]}, 出版社: {book[2]}, 年份: {book[3]}")
    else:
        print("沒有找到相關書籍")

# 列出所有圖書
def list_books():
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    if books:
        print("圖書清單:")
        for book in books:
            print(f"書名: {book[0]}, 作者: {book[1]}, 出版社: {book[2]}, 年份: {book[3]}")
    else:
        print("圖書清單為空")

# 主程式
login()
show_menu()

# 關閉數據庫連接
conn.close()