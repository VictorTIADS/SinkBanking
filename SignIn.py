import ConsolePrint as Cp
import DBService


def sign_in():
    print()
    Cp.printBlue("=====> Login")
    print("Para logar entre com usuário e senha")
    user_name = ask_user_credential()
    user_password = ask_password_credential()
    user = DBService.sign_in_user(user_name, user_password)
    if user is not None:
        Cp.printGreen("Usuário logado com sucesso!")
    else:
        Cp.printYellow("Credenciais incorretas ou usuário não cadastrado!")
    print()
    return user


def ask_user_credential():
    user_credential = input("Digite o nome de usuário:")
    return user_credential.replace(" ", "_")


def ask_password_credential():
    user_credential = input("Digite a senha:")
    return user_credential
