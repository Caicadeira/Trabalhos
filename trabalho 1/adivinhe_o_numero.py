import random
def inserir_valor():
    valor=input("insira um numero: ")
    try:
        valor=int(valor)
        return valor
    except:
        print("o valor deve ser um numero,tente de novo")
        return inserir_valor()


numero=random.randint(0,20)
valor=inserir_valor()
while valor != numero:
    if valor<numero:
        print("o valor informado é menor que o numero gerado")
    else:
        print("o valor informado é maior que o numero gerado")
    valor = inserir_valor()
print("voce acertou!")
print("o valor gerado foi",numero)