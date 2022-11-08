#Funções que não recebem parâmetros
#E apenas executam uma tarefa
def imprimirSemParametro():
    print("Marina")

#Funções com parâmetros de entrada
#Executam uma determinada tarefa
def imprimirComParametro(nome):
    print(nome)

#Funções que possuem um retorno
#Podemos salvar os valores em variáveis
def retornaUmaString():
    return "Stuart"

def somar(numero1, numero2):
    soma = numero1 + numero2
    return soma

def criaTabuleiro(largura, altura):
    tabuleiro = []

    for i in range(altura):
        tabuleiro.append(largura * [0])

    return tabuleiro

tabuleiro = []

for i in range(5):
    tabuleiro.append(10 * [0])

tabuleiro1 = []

for i in range(3):
    tabuleiro.append(3 * [0])
