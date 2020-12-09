import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root",database="test",password="123456",charset="utf8")
print("连接数据成功")
cursor = conn.cursor()
