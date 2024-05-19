import user_table

User, session = user_table.user()
def check(u_id):
    data = session.get(User, u_id)
    print(u_id)
    if data != None:
        return True
    else:
        return 'Вас нет в базе! Чтобы использовать команды, сначала добавьтесь в неё!'