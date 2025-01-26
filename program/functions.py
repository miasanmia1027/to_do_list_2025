import sqlite3
def add_list_DB(what_i_do, date_start,group):
    connect = sqlite3.connect('to_do_list_2025.db')
    cursor = connect.cursor()
    # 리스트를 문자열로 변환 (예: ["A", "B"] -> "A,B")
    group_str = ",".join(group) if isinstance(group, list) else group
    cursor.execute("""
    INSERT INTO to_do_list (what_i_do, date_start, finish, date_end, grouplist)
    VALUES (?, ?, ?, ?, ?)
    """, (what_i_do, date_start, 0,None,group_str))
    connect.commit()
    connect.close()

def add_group_DB(group_input):
    connect = sqlite3.connect('group_table.db')
    cursor = connect.cursor()
    cursor.execute("""
    INSERT INTO group_table (groupvalue)
    VALUES (?)
    """, (group_input,))

    connect.commit()
    connect.close()

def group_list():
    connect_group = sqlite3.connect('group_table.db')
    cursor_group = connect_group.cursor()
    cursor_group.execute("SELECT groupvalue FROM group_table;")
    DB_group = cursor_group.fetchall()
    group_list = [item[0] for item in DB_group]
    return group_list


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


