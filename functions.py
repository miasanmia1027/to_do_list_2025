import sqlite3
def add_list_DB(what_i_do, date_start, numbering):
    connect = sqlite3.connect('to_do_list_2025.db')
    cursor = connect.cursor()
    cursor.execute("""
    INSERT INTO to_do_list (what_i_do, date_start, numbering, finish, date_end)
    VALUES (?, ?, ?, ?, ?)
    """, (what_i_do, date_start, numbering, 0, None))
    connect.commit()
    connect.close()


def Finish_LIST(what_numbering):
    connect = sqlite3.connect('to_do_list_2025.db')
    cursor = connect.cursor()
    cursor.execute(f"UPDATE to_do_list SET finish = 1 WHERE numbering = {what_numbering};")
    connect.commit() 

def check_our_db():
    connect = sqlite3.connect('to_do_list_2025.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM to_do_list;")
    DB_LIST = cursor.fetchall()
    for i in range(len(DB_LIST)):
        print(DB_LIST[i])


