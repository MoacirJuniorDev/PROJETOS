# Funções da calculadora

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração do segundo número pelo primeiro."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão do primeiro número pelo segundo. Retorna mensagem se divisão por zero."""
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Código principal
while True:
    
    #Dá as boas-vindas ao usuário
    print("\n\nBem-vindo à Calculadora Simples!\n\nInsira os números.")

    # Pede ao usuário dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Pede ao usuário a operação desejada
    operacao = input("\nEscolha a operação\n[1] somar\n[2] subtrair\n[3] multiplicar\n[4] dividir\n-> ").lower()

    # Executa a operação correta usando if/elif
    if operacao == "somar" or operacao == "1":
        resultado = somar(num1, num2)
    elif operacao == "subtrair" or operacao == "2":
        resultado = subtrair(num1, num2)
    elif operacao == "multiplicar" or operacao == "3":
        resultado = multiplicar(num1, num2)
    elif operacao == "dividir" or operacao == "4":
        resultado = dividir(num1, num2)
    else:
        resultado = "Operação inválida!"

    # Exibe o resultado
    print(f"Resultado: {resultado}")