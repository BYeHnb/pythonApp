# 写一个方法，验证两个时间戳间隔的天数
# 2018-1-1 2018-1-3 间隔2天
# 2018-1-1 2018-1-1 间隔0天
# 2018-1-1 2018-1-2 间隔1天

import datetime

def get_days(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    return (end - start).days

# 写一个类，连接数据库，里面方法有：查询，插入，删除，修改
# 用的是pymysql

import pymysql

class Mysql(object):
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def select(self, sql):
        self.connect()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.close()
        return result

    #插入并返回id
    def insert(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        result = self.cursor.lastrowid
        self.close()
        return result
    

    def delete(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()

    def update(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()

if __name__ == '__main__':
    # 连接数据库ip123.123.123.123，用户名root，密码123456，数据库名test，端口3306，编码utf8
    db=Mysql("123.123.123.123","root","123456","test")
    # 插入一条数据，name为张三，sex为男，age为18
    








    


