'''
数据库的操作
'''
import pymysql


def connect(db):
    '''

    :param db: 数据库相关的信息，字典格式的
    :return:
    '''
    host=db['host']
    port=db['port']
    user=db['user']
    pwd=db['pwd']
    name=db['name']
    try:
        conn=pymysql.connect(host=host,port=port,user=user,password=pwd,database=name,charset='utf8')
        print("连接数据库成功")
        return conn
    except Exception as e:
        print(f"连接数据失败，异常信息为：{e}")

def disconnect(conn):
    try:
        conn.close()
        print("断开数据库连接成功")
    except Exception as e:
        print(f"断开数据库连接失败，异常信息为：{e}")
def execute(conn,sql):
    '''

    :param conn:
    :param sql:
    :return:
    '''
    try:
        c=conn.cursor()#获取游标
        c.execute(sql)#使用游标执行sql语句
        conn.commit()#提交
        c.close()#关闭游标
        print("执行sql语句成功")
    except Exception as e:
        print(f"执行sql语句失败，异常信息为：{e}")





if __name__ == '__main__':
    db={"host":"192.168.150.54","port":3306,"name":"apple","user":"root","pwd":"123456"}
    conn=connect(db)
    sql="delete from member where mobilephone='13512340095' "
    execute(conn,sql)
    disconnect(conn)