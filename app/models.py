from app import db

ROLE_READ = 0
ROLE_READ_WRITE = 1
ROLE_READ_WRITE_DELETE = 3
ROLE_ADMIN = 4


class WeightList(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    create_user = db.Column(db.String(64))
    create_time = db.Column(db.String(64))
    update_user = db.Column(db.String(64))
    update_time = db.Column(db.String(64))

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        value = {'id': check_null(self.id), 'name': check_null(self.name), 'create_user': check_null(self.create_user), 'create_time': check_null(self.create_time), 'update_user': check_null(self.update_user), 'update_time': check_null(self.update_time)}
        return value


class WeightDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String())
    create_user = db.Column(db.String(64))
    create_time = db.Column(db.String(64))
    update_user = db.Column(db.String(64))
    update_time = db.Column(db.String(64))
    base_id = db.Column(db.Integer)

    def __repr__(self):
        return {'id': check_null(self.id), 'code': check_null(self.code), 'base_id': check_null(self.base_id), 'create_user': check_null(self.create_user), 'create_time': check_null(self.create_time), 'update_user': check_null(self.update_user), 'update_time': check_null(self.update_time)}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(64))
    create_time = db.Column(db.String(64))
    role = db.Column(db.SmallInteger, default=ROLE_READ)

    def __repr__(self):
        return {'id': check_null(self.id), 'name': check_null(self.name), 'create_time': check_null(self.create_time), 'level': check_null(self.level)}


# 校验字符串是否为空,不能传int
def check_null(value):
    if isinstance(value, int):
        return value
    if value and not value.isspace():
        return value
    else:
        return ''


