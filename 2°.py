class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def calcular_bonus(self):
        pass

    def consultar_informacoes(self):
        return f"Nome: {self._nome}, Salário: {self._salario}"

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.2

class Analista(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.1

class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.05

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    print("Selecione o cargo do funcionário\nDigite\n1 se o funcionário for Gerente\n2 se o funcionário for Analista\n3 se o funcionário for Estagiário")
    cargo = input("Digite o número correspondente ao cargo escolhido: ")
    
    funcionario = None
    
    if cargo == "1":
        funcionario = Gerente(nome, salario)
    elif cargo == "2":
        funcionario = Analista(nome, salario)
    elif cargo == "3":
        funcionario = Estagiario(nome, salario)
    else:
        print("Cargo inválido!")
        return None

    if funcionario:
        print(f"Cadastro concluído!\nNome: {nome}\nSalário R$: {salario}\nCargo: {'Gerente' if cargo == '1' else 'Analista' if cargo == '2' else 'Estagiário'}")
    
    return funcionario

def consultar_funcionarios(funcionarios):
    nome = input("Digite o nome do funcionário a ser consultado: ")
    for func in funcionarios:
        if func._nome == nome:
            print(func.consultar_informacoes())
            return
    print("Funcionário não encontrado!")

def calcular_bonus_funcionario(funcionarios):
    nome = input("Digite o nome do funcionário: ")
    for func in funcionarios:
        if func._nome == nome:
            print(f"Bônus de {func._nome}: {func.calcular_bonus()}")
            return
    print("Funcionário não encontrado!")

def menu():
    funcionarios = []
    
    while True:
        print("\nＳｉｓｔｅｍａ ｄｅ Ｆｕｎｃｉｏｎáｒｉｏｓ ｅ Ｃáｌｃｕｌｏ ｄｅ Ｂôｎｕｓ")
        print("\nDigite 1 para Cadastrar funcionário")
        print("Digite 2 para Consultar funcionário")
        print("Digite 3 para Calcular bônus")
        print("Digite 4 para Sair\n")
        opcao = input("⬇ Digite aqui ⬇ \n:")

        if opcao == "1":
            funcionario = cadastrar_funcionario()
            if funcionario:
                funcionarios.append(funcionario)
        elif opcao == "2":
            consultar_funcionarios(funcionarios)
        elif opcao == "3":
            calcular_bonus_funcionario(funcionarios)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

menu()
