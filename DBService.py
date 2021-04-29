import sys

import ConsolePrint as Cp
from User import User


def sign_up_user(user_name, user_password):
    dic_users = __get_register_users()
    if dic_users.get(user_name) is None:
        __register_user(user_name, user_password)
        return User(user_name, user_password)
    else:
        return None


def sign_in_user(user_name, user_password):
    dic_users = __get_register_users()
    if dic_users.get(user_name) is not None and dic_users.get(user_name) == user_password:
        return User(user_name, user_password)
    else:
        return None


def __register_user(user_name, user_password):
    try:
        db = open("login.dat", "a+")
        with db:
            db.write(f"{user_name};{user_password}\r")
        db.close()
        return db
    except OSError:
        Cp.printRed("Houve um problema ao carregar o banco de dados")
        sys.exit()


def __get_register_users():
    dic_users = {}
    try:
        with open('login.dat', 'r') as current:
            lines = current.readlines()
            if lines:
                for line in lines:
                    (key, value) = line.split(";")
                    dic_users[key] = value.replace("\n", "")
    except OSError:
        pass
    return dic_users
