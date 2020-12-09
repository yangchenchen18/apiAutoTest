from ZongHe.caw.Mysql import connect, execute, disconnect


def delete_user(db,mobile):
    conn = connect(db)
    sql = f"delete from member where mobilephone={mobile} "
    execute(conn, sql)
    disconnect(conn)


if __name__ == '__main__':
    db = {"host": "192.168.150.54", "port": 3306, "name": "apple", "user": "root", "pwd": "123456"}
    delete_user(db,13256789012)