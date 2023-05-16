import sqlite3

conn = sqlite3.connect('D:\\softwore work\\db work\\text.db')
print ("数据库打开成功")
c = conn.cursor()
c.execute('''CREATE TABLE classmate
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("数据表创建成功")
conn.commit()
conn.close()