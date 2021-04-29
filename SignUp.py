import ConsolePrint as Cp
import DBService
import Utils


def sign_up():
    print()
    Cp.printBlue("=====> Cadastro")
    print("Vamos criar a sua conta. Você vai precisar criar um usuário e senha. Vamos lá?")
    success_store = False
    user = None
    while not success_store:
        user_name = ask_user_credential()
        user_password = ask_user_password()
        user = DBService.sign_up_user(user_name, user_password)
        if user is not None:
            Cp.printGreen("Usuário cadastrado com sucesso!")
            success_store = True
        else:
            Cp.printYellow("Já existe um usuário cadastrado com esse nome. Tente outro!")
    return user


def ask_user_credential():
    user_credential = input("Digite um nome de usuário:")
    while not Utils.is_valid_input(user_credential):
        user_credential = input("Nome de usuário invalido, tente outro:")
    return user_credential.replace(" ", "_")


def ask_user_password():
    user_credential = input("Digite uma senha:")
    while not Utils.is_valid_input(user_credential):
        user_credential = input("Senha inválida, tente outra:")
    return user_credential
