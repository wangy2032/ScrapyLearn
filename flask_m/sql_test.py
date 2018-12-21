import psutil
import pymysql

# 获取cpu利用率
def cup_shuju():
    cpu_use = psutil.cpu_percent(1)
    return cpu_use

#写入数据库
def writeSql(now):
    date = cup_shuju()
    db = pymysql.connect('localhost', 'root', '123456', 'jiankong')
    cur = db.cursor()
    sql = """ insert into cpu_per(jtime, jcpu) value(%s, %s) """
    cur.execute(sql%(now, date))
    db.commit()
    db.close()
#读取数据库中的cpu数据
def readSql(now):
    db = pymysql.connect('localhost', 'root', '123456', 'jiankong')
    cur = db.cursor()
    sql = """ select * from cpu_per where jtime = '%s' """
    cur.execute(sql%now)
    result = cur.fetchone()
    db.close()
    return result





