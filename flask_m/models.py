from exts import db
class Role(db.Model):
    __tablename__='role'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), index=True)
    email=db.Column(db.String(64))






