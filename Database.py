import sqlite3

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

def createTb():
    cur.execute("create table if not exists CashBook_Table (date text, cb_id text, amount INTEGER, remarks text, action text)")
    print("Table created successfully...")
    
createTb()

def fetchData():
    cur.execute("select * from CashBook_Table")
    print(cur.fetchall())
    
# fetchData()

def deleteData():
    cur.execute("delete from CashBook_Table where action = ?", ("Cash_Out",))
    conn.commit()
    print("Deleted successfully...")
    
# deleteData()