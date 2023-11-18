from database import create_session, close_session
import functions as f


def main():
    # Приклад використання:
    session = create_session()

    # CRUD операції

    goods_to_add = [['IPhone 14', 799],['IPhone 15',999], ['IPhone 15 Pro', 1299]]
    for item in goods_to_add:
        f.create_goods(session, item[0], item[1])

    clients_to_add = [['John', 'john@mail.com'],['Jane','jane@mail.com']]
    for item in clients_to_add:
        f.create_clients(session, item[0], item[1])

    orders_to_add = [[1, 2, 2], [1, 1, 3], [1, 1, 3], [2, 3, 1], [2, 1, 3]]
    for item in orders_to_add:
        f.create_orders(session, item[0], item[1], item[2])

    # Вивід всіх товарів
    all_goods = f.get_all_goods(session)
    print("Всі товари:")
    for goods in all_goods:
        print(goods.id, goods.name, goods.price)

    # Виведення деталей замовлень
    order_details = f.get_order_details(session)
    print("\nДеталі замовлення:")
    for detail in order_details:
        print(f"{detail[0]} | {detail[1]} | {detail[2]}")

    # Виведення деталей замовлень для клієнта Jane, відсортованих за кількістю у порядку спадання
    jane_orders = f.get_order_details_filtered(session, client_name='Jane', descending_order=True)
    print("\nЗамовлення Jane:")
    for order in jane_orders:
        print(f"{order[0]} | {order[1]} | {order[2]}")

    # Інші операції
    order_count = f.order_count_per_client(session)
    print("\nКількість замовлень в клієнта:")
    for row in order_count:
        print(row)

    total_quantity = f.total_quantity_per_client(session)
    print("\nЗагальна кількість товарів на клієнта:")
    for row in total_quantity:
        print(row)

    average_price = f.average_price_of_goods(session)
    print("\nСередня ціна товарів:", average_price)

    # Закриття сесії
    close_session(session)


if __name__ == '__main__':
    main()