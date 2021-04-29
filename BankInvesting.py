import ConsolePrint as Cp
import Utils


def start_simulation():
    print()
    Cp.printBlue("=====> Simulação de Investimento")
    print("Veremos em quantos meses você se tornará milionário")
    print("Valor da taxa: 0,35% ao mês")
    wanna_play = True
    while wanna_play:
        salario = ask_salario_mensal()
        custos = ask_custos_mensal()
        simulate(salario, custos)
        wanna_play = want_simulate_again()


def want_simulate_again():
    print()
    print(f"Quer fazer outra simulação?")
    print(f"S:Sim N:Não")
    option = input("Digite sua opção:").upper().replace(" ", "")
    while not Utils.is_yes_or_no(option):
        option = input("Desculpe, não entendi. Tente novamente: ").upper()
    print()
    if option == "S":
        return True
    else:
        return False


def simulate(salario, custos):
    try:
        print()
        int_salario = int(salario)
        int_custos = int(custos)
        liquido = int_salario - int_custos
        Cp.printBlue(f"Salário liquido: R${liquido}")
        porcent = ask_porcent(liquido)
        c = porcent * liquido
        m = c
        meses = 0
        while m < 1000000:
            m = c + m * (1 + 0.35 / 100)
            meses += 1
        print()
        if meses / 12 > 50:
            Cp.printYellow("Esta aplicação é inviável para o seu perfil financeiro!")
        else:
            Cp.printBlue(f"Você precisará de {meses} meses ou {round(meses / 12)} anos para se tornar milionário.")
    except:
        print("Error")


def ask_porcent(liquido):
    porcent = input(f"Quantos % de R${liquido} você deseja aplicar $:").replace(" ", "")
    while porcent is not int:
        try:
            porcent = int(porcent)
            while not 0 < porcent < 101:
                Cp.printYellow("Procentagem inválida, tente novamente!")
                porcent = input(f"Quantos % de R${liquido} você deseja aplicar $:")
            break
        except:
            Cp.printYellow("Salário inválido, tente novamente!")
            porcent = input(f"Quantos % de R${liquido} você deseja aplicar $:")
    return porcent / 100


def ask_salario_mensal():
    salario = input("Infome seu salário mensal $:").replace(" ", "")
    while salario is not int:
        try:
            salario = int(salario)
            break
        except:
            Cp.printYellow("Salário inválido, tente novamente!")
            salario = input("Infome seu salário mensal $:")
    return int(salario)


def ask_custos_mensal():
    salario = input("Infome os seus custos mensais $:").replace(" ", "")
    while salario is not int:
        try:
            salario = int(salario)
            break
        except:
            Cp.printYellow("Custo inválido, tente novamente!")
            salario = input("Infome os seus custos mensais $:")
    return int(salario)
