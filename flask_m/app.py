from flask import Flask,render_template
from houtai import hard_disk, Ram, psid
import pymysql
from flask import request
import sql_test
import json
import time

app = Flask(__name__)
db = pymysql.connect('localhost', 'root', '123456', 'test1')
cur = db.cursor()


# 登陆路由
@app.route('/login', methods=['POST'])
def index():
    #获取用户的邮箱和密码
    semail = request.form['email']
    spasswd = request.form['password']
    #判断用户输入的数据在数据库中是否存在
    sql = """ select email,passwd from zhuce where email='%s' and passwd='%s' """%(semail, spasswd)
    cur.execute(sql)
    #不存在返回None
    results = cur.fetchone()
    if results:
        #获取论坛中的招聘数据
        db1 = pymysql.Connection('localhost', 'root', '123456', 'test')
        cur1 = db1.cursor()
        sql_shuju = """ select name,salary_min,salary_max,job_address,work_years,Enducation,job_type,job_advantage,job_bts,field from lagou ORDER BY RAND() limit 5"""
        cur1.execute(sql_shuju)
        results = cur1.fetchall()
        db1.commit()
        print(results)
        #把整个数据传入boke.html页面
        return render_template('boke.html', u=results)
        db.close()
        db1.close()
    else:
        return render_template('login.html', message='密码或账号错误',)
        db.close()


@app.route('/zhuce', methods=['POST'])
def zhuce():
    return render_template('zhuce.html')

#注册表单验证
@app.route('/', methods=['POST'])
def zhu():
    #获取用户输入数据
    sname = request.form['first_name']
    slast = request.form['last_name']
    email1 = request.form['email']
    passwd = request.form['password']
    #判断邮箱是否存在
    sql_yan = """ select email from zhuce where email='%s'"""%(email1)
    cur.execute(sql_yan)
    emails = cur.fetchone()  #none
    if not emails:
        #不存在是写入数据库的注册表单
        sql_cun = """ insert into zhuce(first_name, last_name, email, passwd) values('%s', '%s', '%s', '%s') """
        cur.execute(sql_cun%(sname, slast, email1, passwd))
        db.commit()
        #注册成功跳转登陆页面
        return render_template('login.html')
    else:
        return render_template('zhuce.html', message='邮箱已注册')
    db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('cuowu.html'), 404


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/jiankong')
def first():
    info = Ram()
    #硬盘
    zong, shiyong = hard_disk()

    return render_template("test.html", info=info, zong=zong, shiyong=shiyong)


#把此时间点的cpu的利用率存入数据库
#再从数据库中取出此时间的cpu的利用率
@app.route('/data')
def getSql():
    dict1 = {}
    #设置时间戳
    now = time.time()
    sql_test.writeSql(now)
    time.sleep(1)
    data = sql_test.readSql(now)
    #取出利用率且转换为浮点型
    dict1['cpu'] = float(data[1])
    data = json.dumps(dict1)
    print(data)
    #把数据返回给jquery代码
    return data

@app.route('/zhexian')
def zhe():
    info = Ram()
    return render_template('zhexian.html', info=info)

@app.route('/jincheng')
def jin():
    jc = psid()
    return render_template('jincheng.html', jc=jc )
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=778, debug=True)

