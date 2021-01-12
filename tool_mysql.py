#!/usr/bin/python3
import sys
import pymysql
import datetime
import tool_basic


# CREATE TABLE `stock_daily`  (
#   `code` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
#   `name` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
#   `date` datetime(0) NULL DEFAULT NULL,
#   `begin` int NULL DEFAULT NULL,
#   `end` int NULL DEFAULT NULL,
#   `max` int NULL DEFAULT NULL,
#   `min` int NULL DEFAULT NULL,
#   UNIQUE INDEX `PK_CODE`(`code`) USING BTREE,
#   UNIQUE INDEX `UK_NAME`(`name`) USING BTREE
# ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

class ToolMySql:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "mysql", "stocks", autocommit=True)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def execute_sql(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 执行sql语句
            self.db.commit()
            return True
        except pymysql.err.IntegrityError as e:
            self.db.rollback()
            return True
        except Exception as e:
            tool_basic.print_red("%s, %s" % (__file__, sys._getframe().f_lineno), e)
            # 发生错误时回滚
            self.db.rollback()
            return False

    def insert(self, code, name, date, begin, end, max_value, min_value):
        # SQL 插入语句
        sql = "INSERT INTO `stock_daily`(`code`, `name`, `date`, `begin`, `end`, `max`, `min`, `storation`) " \
              "VALUES ('%s', '%s', '%s', %d, %d, %d, %d, '%s'); " \
              % (code, name, date, begin, end, max_value, min_value, "origin")

        return self.execute_sql(sql)

    def insert_preStoration(self, code, name, date, end, storation):
        # SQL 插入语句
        sql = "INSERT INTO `stock_daily`(`code`, `name`, `date`, `end`, `storation`) " \
              "VALUES ('%s', '%s', '%s', %d, '%s'); " \
              % (code, name, date, end, storation)

        return self.execute_sql(sql)

    def get(self, code, storation="", date_start="1900-11-01"):

        # SQL 查询语句
        # where DATE_FORMAT(date, '%Y-%m-%d') >= DATE_FORMAT("2020-11-01", '%Y-%m-%d');

        sql = "SELECT `date`, `begin`, `end`, `max`, `min` FROM stock_daily "
        if storation == "":
            sql += "WHERE code = '%s' " % code
        else:
            sql += "WHERE code = '%s' AND storation = '%s' " % (code, storation)

        sql += "AND DATE_FORMAT(date, '%""Y-%""m-%""d') " + \
               ">= DATE_FORMAT('" + date_start + "', '%""Y-%""m-%""d') " + \
               "ORDER BY date"

        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取所有记录列表
        results = self.cursor.fetchall()
        return results

    def delete_all(self):
        # SQL 插入语句
        sql = "delete from `stock_daily`;"

        return self.execute_sql(sql)


fields = ["code", "name", "date", "begin", "end", "max", "min"]


def connect():
    db = pymysql.connect("localhost", "root", "mysql", "stocks")
    return db


def get_cursor(db):
    cursor = db.cursor()
    return cursor


def disconnect(db):
    db.close()


def insert(cursor, code, name, date, begin, end, max_value, min_value):
    # SQL 插入语句
    sql = "INSERT INTO `stock_daily`(`code`, `name`, `date`, `begin`, `end`, `max`, `min`) " \
          "VALUES ('%s', '%s', '%s', %d, %d, %d, %d); " \
          % (code, name, date, begin, end, max_value, min_value)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        return True
    except Exception as e:
        print(e)
        # 发生错误时回滚
        db.rollback()
        return False


def get():
    # SQL 查询语句
    sql = "SELECT * FROM stock_daily"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
    except Exception as e:
        print(e)
        print("Error: unable to fetch data")


if __name__ == "__main__":

    # basic
    if 0:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "mysql", "stocks")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        print("Database version : %s " % data)

        # 关闭数据库连接
        db.close()

    # test func
    if 0:
        db = connect()
        cursor = get_cursor(db)

        # print(insert(cursor, code="91", name="baaa", date=datetime.datetime.today().date(),
        #              begin=1, end=2, max_value=3, min_value=0))

        get()

        disconnect(db)

    # test class
    if 1:
        tool_mysql = ToolMySql()
        # tool_mysql.get()
        tool_mysql.delete_all()
