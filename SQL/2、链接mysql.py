import json

from pymysql import Connection


class DataSet:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return {"id": self.id, "name": self.name, "age": self.age, "gender": self.gender}


# 获取mysql数据库的链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='2016kevinZ@',
    autocommit=True
)
# print(conn.get_server_info())
# # 关闭mysql数据库
# conn.close()

"""
执行肥查询性质的sql
"""
# 获取游标对象
cursor = conn.cursor()
# 创建数据库
# cursor.execute('create database kevin_test')
# 选择数据库
conn.select_db('kevin')
# # 执行sql
# cursor.execute('create table kevin_pymysql(id int, name varchar(10));')
# cursor.execute('INSERT INTO kevin_pymysql(id, name) VALUES(1, "kevin");')
# cursor.execute("insert into student values(13, 'kevin13', 18, 0)")

"""
将数据插入表---事务
    pymysql在执行数据插入或者其他产生数据更改的sql语句时。默认是需要提交更改的，通过代码"确认"
    1、通过链接对象.commit()
    2、自动提交，可以在Connention对象是加上autocommit=True
"""
# cursor.execute("insert into student values(14, 'kevin14', 14, 1)")
# conn.commit()

cursor.execute('select * from student')

result: tuple = cursor.fetchall()
f = open('data.json', 'a', encoding='UTF-8')
list1: list = []
for i in result:
    data = DataSet(i[0], i[1], i[2], i[3])
    list1.append(data.__str__())
obj1 = {'data': list1}
f.write(json.dumps(obj1))
f.close()
print(json.dumps(list1))
conn.close()
