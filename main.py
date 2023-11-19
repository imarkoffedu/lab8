from database import create_session, close_session
import functions as f


def main():
    session = create_session()
    
    # CRUD операції
    
    # юзери
    print("\n\n\n\n- Користувачі")


    # створення нових користувачів
    print("Створення нових акаунтів")
    users_to_add = [
        ['linz', '123456', 'Linda Z.', 'lsdavkklasm@gmail.com', 'user'],
        ['peter', '123456', 'Peter S.', 'sdafsdlscjsam@gmail.com', 'tester'],
        ['john', '123456', 'John D.', 'safmnsvjnfsjdnfd@gmail.com', 'developer'],
        ['jane', '123456', 'Jane D.', 'afonsaklnjkgnjk@gmail.com', 'user'],
        ['james', '123456', 'James B.', 'safjosdlvndklvndfnj@gmail.com', 'developer'],
        ['jim', '123456', 'Jim C.', 'errgyushrdhjhciu@gmail.com', 'user'],
        ['jessica', '123456', 'Jessica A.', 'foisegvlh@gmail.com', 'user'],
        ['jennifer', '123456', 'Jennifer M.', 'sdudiunfhel@gmail.com', 'user'],
        ['julie', '123456', 'Julie W.', 'vrsaguckj@gmail.com', 'tester'],
        ['jason', '123456', 'Jason S.', 'tsiuvgynrd@gmail.com', 'developer']
    ]

    for item in users_to_add:
        print(item)
        f.create_user(session, username=item[0], password=item[1], full_name=item[2], email=item[3], role=item[4])

    # пошук всіх користувачів з юзернеймом ark
    print("\nПошук всіх користувачів з юзернеймом ark")
    get_users_by_username = f.get_users_by_username(session, 'ark')
    for el in get_users_by_username:
        print("#{} | {} | {} | {} | {}".format(el.id, el.username, el.full_name, el.email, el.role))

    # пошук всіх користувачів з роллю user
    print("\nПошук всіх користувачів з роллю user")
    get_users_by_role = f.get_users_by_role(session, 'user')
    for el in get_users_by_role:
        print("#{} | {} | {} | {}".format(el.id, el.username, el.full_name, el.email, el.role))

    # видалення користувача
    user_id = 10
    print(f"\nВидалення користувача #{user_id}")
    f.delete_user(session, user_id)

    # повторний пошук всіх користувачів з роллю user
    get_users_by_role = f.get_users_by_role(session, 'user')
    for el in get_users_by_role:
        print("#{} | {} | {} | {} | {}".format(el.id, el.username, el.full_name, el.email, el.role))

    # баг-репорти
    print("\n\n\n\n- Баг-репорти")


    # створення нових баг-репортів
    print("\nСтворення нового баг-репорту")
    bugs_to_add = [
        ['Address GNOME45 Workspace indicator', 'Dark theme is fine, but the workspace indicator\
          is not visible in the top bar. It should be white or some other light color.', 4],
    ]

    for item in bugs_to_add:
        print(item)
        f.create_bug(session, title=item[0], description=item[1], created_by=item[2])

    # всі незабершені баги впорядковані за пріоритетом
    print("\nВивід всіх незавершених багів впорядковані за пріоритетом")
    get_not_closed_bugs = f.get_not_closed_bugs(session)
    for el in get_not_closed_bugs:
        print(f"#{el.id} | {el.title} | {el.priority} | {el.status} | {el.assigned_to}")

    # оновлення баг-репорту
    bug_id = get_not_closed_bugs[-1].id # останній баг-репорт
    title = 'Workspace indicator is not visible on GNOME 45'
    priority = 'HIGH'
    status = 'ASSIGNED'
    assigned_to = 3
    print(f"\nОновлення баг-репорту #{bug_id}")
    f.update_bug(session, bug_id, title=title, priority=priority, status=status, assigned_to=assigned_to)

    # повторний вивід всіх незавершених багів
    get_not_closed_bugs = f.get_not_closed_bugs(session)
    for el in get_not_closed_bugs:
        print(f"#{el.id} | {el.title} | {el.priority} | {el.status} | {el.assigned_to}")

    # коментарі
    print("\n\n\n\n- Коментарі")

    # вивід всіх коментарів, що відповідають баг-репорту
    bug_id = 2
    print(f"\nВивід всіх коментарів від самого старого до самого нового, що відповідають баг-репорту #{bug_id}")
    get_all_comments_in_bug = f.get_all_comments_in_bug(session, bug_id)
    for el in get_all_comments_in_bug:
        print(f"\n#{el.id} | {el.bug_id} | {el.comment} | {el.created_at}")

    # оновлення коментаря
    comment_id = 2
    comment = "default height LGTM\n \
the no button bg would be great as a tweak, but that wouldn't be good for people who have blurred panels, \
unless they change the colour of the blur etc. \
so maybe a tweak on top of that to change text colour for the panel or something"
    print(f"\nОновлення коментаря #{comment_id}")

    get_comment_by_id = f.get_comment_by_id(session, comment_id)
    print(f"\n#{get_comment_by_id.id} | {get_comment_by_id.bug_id} | {get_comment_by_id.comment} | {get_comment_by_id.created_at}")

    f.update_comment(session, comment_id, comment)

    # вивід оновленого коментаря
    print(f"\nВивід оновленого коментаря #{comment_id}")
    get_comment_by_id = f.get_comment_by_id(session, comment_id)
    print(f"\n#{get_comment_by_id.id} | {get_comment_by_id.bug_id} | {get_comment_by_id.comment} | {get_comment_by_id.created_at}")

    # Закриття сесії
    close_session(session)


if __name__ == '__main__':
    main()