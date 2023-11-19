# Визначення функцій, які виконують різні операції з базою даних

from models import Users, Bugs, Comments
from sqlalchemy import func, case


# Функція для створення нового об'єкта
def create(session, model):
    session.add(model)
    session.commit()


# Функція для оновлення об'єкта
def update(session, model, row_id, **kwargs):
    object_to_update = session.query(model).filter_by(id=row_id).first()
    if object_to_update:
        for key, value in kwargs.items():
            setattr(object_to_update, key, value)
        session.commit()
    return object_to_update


# Функція для видалення об'єкта
def delete(session, model, id):
    object_to_delete = session.query(model).filter_by(id=id).first()
    if object_to_delete:
        session.delete(object_to_delete)
        session.commit()
    return object_to_delete


# Користувачі

# створення нового користувача
def create_user(session, username, password, email, full_name=None, role='user'):
    new_user = Users(username=username, password=password, full_name=full_name, email=email, role=role)
    create(session, new_user)


# користувачі з роллю
def get_users_by_role(session, role):
    return session.query(Users).where(Users.role == role).all()


# вибір користувача по id
def get_user_by_id(session, user_id):
    return session.query(Users).where(Users.id == user_id).first()


# пошук по юзернейму
def get_users_by_username(session, username):
    return session.query(Users).where(Users.username.like(f'%{username}%')).all()


# Функція для видалення користувача
def delete_user(session, user_id):
    return delete(session, Users, user_id)


# Баг-репорти

# створення нового баг-репорту
def create_bug(session, title, created_by, description=None, status=None, priority=None, assigned_to=None):
    new_bug = Bugs(title=title, description=description, status=status, priority=priority,
                   created_by=created_by, assigned_to=assigned_to)
    create(session, new_bug)


# Функція для отримання всіх баг-репортів
def get_all_bugs(session):
    return session.query(Bugs).all()


# отримання баг-репорту по id
def get_bug_by_id(session, bug_id):
    return session.query(Bugs).where(Bugs.id == bug_id).first()


# всі незакриті баг-репорти
def get_not_closed_bugs(session):
    return session.query(Bugs)\
            .filter((Bugs.status != 'WONTFIX') & (Bugs.status != 'RESOLVED'))\
            .order_by(
                case(
                    (Bugs.priority == 'HIGH', 1),
                    (Bugs.priority == 'MEDIUM', 2),
                    (Bugs.priority == 'LOW', 3),
                    else_=4
                ).asc()
            ).all()


# оновлення баг-репорту
def update_bug(session, bug_id, title=None, description=None, 
               status=None, priority=None, assigned_to=None, is_open=None):
    values_to_update = {}
    for key, value in locals().items():
        if value != None and key != 'session' and key != 'bug_id':
            values_to_update[key] = value
    print(values_to_update)
    return update(session, Bugs, bug_id, **values_to_update)


# Функція для видалення баг-репорту
def delete_bug(session, bug_id):
    return delete(session, Bugs, bug_id)


# Коментарі

# створення нового коментаря
def create_comment(session, bug_id, created_by, comment):
    new_comment = Comments(bug_id=bug_id, created_by=created_by, comment=comment)
    create(session, new_comment)


# пошук всіх коментарів, що відповідають баг-репорту
def get_all_comments_in_bug(session, bug_id):
    return session.query(Comments)\
        .where(Comments.bug_id == bug_id)\
        .order_by(Comments.created_at.asc()).all()


# пошук конкретного коментаря
def get_comment_by_id(session, comment_id):
    return session.query(Comments).where(Comments.id == comment_id).first()


# оновлення коментаря
def update_comment(session, comment_id, comment):
    return update(session, Comments, comment_id, comment=comment)


# Функція для видалення коментаря
def delete_comment(session, comment_id):
    return delete(session, Comments, comment_id)