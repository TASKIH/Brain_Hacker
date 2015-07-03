# -*- coding: utf-8 -*-
from models.user import User


def check_group_permission(f):
    """
    グループに所属していない場合は、リダイレクトする。
    """
    def wrapper(*args):
        user = args[0].get_current_user()
        if not user:
            args[0].redirect(args[0].reverse_url('login'))
            return
        user = args[0].session.query(User).filter_by(id=user['id']).first()
        if user.belongs_to_group(int(args[1])):
            pass
        else:
            error_message = 'この操作は許可されていません。'
            args[0].redirect(args[0].reverse_url('index') + '?error_message={0}'.format(error_message))
            return
        return f(*args)
    return wrapper

"""
def pickup(session, model, id):
    return session.query(model).get(id)


def edit(session, model, id, params):
    record = pickup(session, model, id)
    record.update(**params)
    session.add(record)
    session.commit()


def delete(session, model, id):
    record = pickup(session, model, id)
    session.delete(record)
    session.commit()
"""