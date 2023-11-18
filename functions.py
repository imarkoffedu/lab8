# Визначення функцій, які виконують різні операції з базою даних

from models import Goods, Clients, Orders
from sqlalchemy import func


# Функція для створення нового товару
def create_goods(session, name, price):
    new_goods = Goods(name=name, price=price)
    session.add(new_goods)
    session.commit()


# Функція для додавання нового клієнта
def create_clients(session, name, email):
    new_clients = Clients(name=name, email=email)
    session.add(new_clients)
    session.commit()


# Функція для додавання нового замовлення
def create_orders(session, client_id, goods_id, quantity):
    new_orders = Orders(client_id=client_id, goods_id=goods_id, quantity=quantity)
    session.add(new_orders)
    session.commit()


# Функція для отримання всіх товарів
def get_all_goods(session):
    return session.query(Goods).all()


# Функція для оновлення інформації про товар
def update_goods(session, goods_id, new_name, new_price):
    goods_to_update = session.query(Goods).filter_by(id=goods_id).first()
    if goods_to_update:
        goods_to_update.name = new_name
        goods_to_update.price = new_price
        session.commit()


# Функція для видалення товару
def delete_goods(session, goods_id):
    goods_to_delete = session.query(Goods).filter_by(id=goods_id).first()
    if goods_to_delete:
        session.delete(goods_to_delete)
        session.commit()


# Функція для отримання деталей замовлення (ім'я клієнта, назва товару та кількість)
def get_order_details(session):
    return session.query(Clients.name, Goods.name, Orders.quantity).\
        join(Orders, Clients.id == Orders.client_id).\
        join(Goods, Goods.id == Orders.goods_id).all()


# Функція для отримання деталей замовлення за заданим клієнтом по спаданню кількості (ім'я клієнта, назва товару та кількість)
def get_order_details_filtered(session, client_name=None, descending_order=True):
    query = session.query(Clients.name, Goods.name, Orders.quantity).\
        join(Orders, Clients.id == Orders.client_id).\
        join(Goods, Goods.id == Orders.goods_id)

    if client_name:
        query = query.filter(Clients.name == client_name)

    if descending_order:
        query = query.order_by(Orders.quantity.desc())

    return query.all()


# Функція для вибірки кількості замовлень для кожного клієнта
def order_count_per_client(session):
    return session.query(Clients.name, func.count(Orders.id).label('order_count')).\
        outerjoin(Orders, Clients.id == Orders.client_id).\
        group_by(Clients.id).all()


# Функція для вибірки суми кількості товарів для кожного клієнта
def total_quantity_per_client(session):
    return session.query(Clients.name, func.sum(Orders.quantity).label('total_quantity')).\
        outerjoin(Orders, Clients.id == Orders.client_id).\
        group_by(Clients.id).all()


# Функція для вибірки середньої ціни товару
def average_price_of_goods(session):
    return session.query(func.avg(Goods.price).label('average_price')).scalar()

