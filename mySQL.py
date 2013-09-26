# _*_ coding: utf-8 _*_ 
import sqlite3
conn=sqlite3.connect('example')
##若想创建内存数据库，可以conn=sqlite3.connect(':memory:')
##连接创建好后，再创建游标对象，执行他的execute()方法进行SQL语句执行
c=conn.cursor()
#create a table
c.execute('''create table table1
(date text, trans text, symbol text,
 qty real, price real)''')
#insert a row of data
c.execute('''insert into table1
          values ('2011-01-05','BUY','RHAT',100,35.14)''')
#save the changes
conn.commit()
#we can also close the cursor if we are done with it
c.close()

# Do this instead
t = (symbol,)
c.execute('select * from stocks where symbol=?', t)
# Larger example
for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
         ]:
    c.execute('insert into stocks values (?,?,?,?,?)', t)
