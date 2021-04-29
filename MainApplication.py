import sys

import BankInvesting
import ConsolePrint as Cp
import SignIn
import SignUp
import Utils as utils


def start_system():
    tries = 4
    user = get_user()
    while user is None and tries != 0:
        tries -= 1
        Cp.printYellow(f"Tentativas restantes {tries + 1}")
        user = get_user()

    if tries == 0:
        Cp.printRed("Número de tentativas atingidas, tente novamente mais tarde!")
        sys.exit()
    show_menu(user)
    BankInvesting.start_simulation()


def show_menu(user):
    Cp.printBlue("******* Sink Banking and Services inc. - Menu *******")
    Cp.printBlue(f"Você está logado. Usuário: {user.name}")
    print()
    cpf = ask_for_cpf()
    while not confirm_cpf(cpf):
        cpf = ask_for_cpf()


def ask_for_cpf():
    hard_cpf = input("Infome o CPF, apenas números:")
    if hard_cpf.lower() == "sair":
        sys.exit()
    valid_cpf = utils.is_valid_cpf(hard_cpf)
    while not valid_cpf:
        Cp.printYellow("CPF inválido, tente novamente!")
        new_cpf = input("Infome o CPF, apenas números:")
        if new_cpf.lower() == "sair":
            sys.exit()
        if utils.is_valid_cpf(new_cpf):
            hard_cpf = utils.clean_cpf_if_contains_dash_or_dot(new_cpf)
        valid_cpf = utils.is_valid_cpf(hard_cpf)
    return utils.apply_cpf_format(hard_cpf)


def confirm_cpf(cpf):
    print(f"Confirma o CPF: {cpf}?")
    print(f"S:Sim N:Não")
    option = input("Digite sua opção:").upper().replace(" ", "")
    while not utils.is_yes_or_no(option):
        option = input("Desculpe, não entendi. Tente novamente: ").upper()
    if option == "S":
        return True
    else:
        return False


def get_user():
    Cp.printBlue("******* Sink Banking and Services inc. *******")
    print("Bem-vindo(a) ao Sink Banking and Services, os melhores serviços bancários para você.")
    print()
    print("Você já tem uma conta? \nS:Sim N:Não")
    user = SignIn.sign_in() if ask_user_has_account() else SignUp.sign_up()
    return user


def ask_user_has_account():
    option = input("Digite sua opção:").upper().replace(" ", "")
    while not utils.is_yes_or_no(option):
        option = input("Desculpe, não entendi. Tente novamente: ").upper()
    if option == "S":
        return True
    else:
        return False


if __name__ == '__main__':
    start_system()
