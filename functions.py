import sqlite3
def add_list_DB(what_i_do, date_start, numbering):
    connect = sqlite3.connect('D:/DataBase/to_do_list_2025.db')
    cursor = connect.cursor()
    cursor.execute("""
    INSERT INTO to_do_list (what_i_do, date_start, numbering, finish, date_end)
    VALUES (?, ?, ?, ?, ?)
    """, (what_i_do, date_start, numbering, 0, None))
    connect.commit()
    connect.close()



