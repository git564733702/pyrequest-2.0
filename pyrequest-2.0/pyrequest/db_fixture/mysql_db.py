# coding=utf-8
import pymysql.cursors
from os.path import abspath, dirname
import configparser as cparser
import time


# ======== 读取文件 db_config.ini 的设置 ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== 封装 MySql 基本操作 ===================
class DB:

    def __init__(self):
        # 初始化数据库连接
        try:
            # 连接 database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清理表数据
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 插入表数据，对插入的字典传化为str，以便于插入数据库
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    # 关闭数据库连接
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

# t01=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
t01=time.strftime("%Y-%m-%d %H:%M:%S")  #定义现在时间
if __name__ == '__main__':

    db = DB()
    table_name = "sign_event"
    data = {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2016-08-20 00:25:42','create_time':t01}
    table_name2 = "sign_guest"
    data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'create_time':'','event_id':1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
