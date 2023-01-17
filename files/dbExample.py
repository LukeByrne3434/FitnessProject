import sqlite3

conn = sqlite3.connect('pythonDB.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)')

def data_entry():
	number = input()
	name = input()
     
	c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
	conn.commit()

def select_all_tasks():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM RecordONE")

    rows = cur.fetchall()

    for row in rows:
        print(row)

create_table()
data_entry()
select_all_tasks()



   

c.close()
conn.close()

