import pymysql


class SQLHelper(object):
    @staticmethod
    def open():
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='externalcompany')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def fetch_one(sql, args):
        conn, cursor = SQLHelper.open()
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        SQLHelper.close(conn, cursor)
        return obj

    @staticmethod
    def fetch_all(sql, args):
        conn, cursor = SQLHelper.open()
        cursor.execute(sql, args)
        obj = cursor.fetchall()
        SQLHelper.close(conn, cursor)
        return obj
