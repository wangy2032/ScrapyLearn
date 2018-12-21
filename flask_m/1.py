import sql_test
import json
import time
def getSql():
    dict1 = {}
    now = time.time()
    sql_test.writeSql(now)
    time.sleep(1)
    data = sql_test.readSql(now)
    dict1['cpu']=float(data[1])
    data = json.dumps(dict1)
    print(dict1)
    print(type(dict1))
    print(type(data))

getSql()

app = Flask(__name__)

bssedir = os.path.abspath(os.path.dirname(__file__))
# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(bssedir, "pythontest.db")
# 设置每次提交结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True


def craete_db():
    db.drop_all()
    db.create_all()
    ro1 = Role(id=1, name='1111', email='2@2.com')
    ro2 = Role(id=2, name='aaa', email='1@1.com')
    ro3 = Role(id=3, name='bbb', email='3@3.com')
    ro4 = Role(id=4, name='ccc', email='4@4.com')
    db.session.add_all([ro1, ro2, ro3, ro4])  # 插入
    db.session.commit()


db.init_app(app)