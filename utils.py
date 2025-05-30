import pymysql

def connect():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='courseselection1', port = 3306, charset='utf8')
    return db