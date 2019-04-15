import sys, time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))
# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))
# 定义现在时间
# t01=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
t01=time.strftime("%Y-%m-%d %H:%M:%S")

# 创建测试数据
datas = {
    # 发布会数据
    'sign_event':[
        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':future_time,'create_time':t01},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':future_time,'create_time':t01},
        {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':future_time,'create_time':t01},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':past_time,'create_time':t01},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':future_time,'create_time':t01},
    ],
    # 嘉宾表数据
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':t01},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':t01},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':t01},
    ],
}


# 测试数据插入表
def init_data():
    DB().init_data(datas)
    #以下为原来不存在的代码，疑问。不需要用到，注释即可
    # db = DB()
    # for table, data in datas.items():
    #     db.clear(table)
    #     for d in data:
    #         db.insert(table, d)
# 首先调用db类中的clear方法清除表数据，然后循环调用insert()方法插入表数据


if __name__ == '__main__':
    init_data()
#     用于读取datas字典中的数据
