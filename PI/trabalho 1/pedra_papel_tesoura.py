import random
opcoes=["pedra","papel","tesoura"]

def inserir_escolha():
    valor = input("escolha entre pedra papel e tesoura: ")
    if valor not in opcoes:
        print("a opção escolhida é inválida,tente de novo")
        return inserir_escolha()
    else:
        return valor

def jogar():
    opcao=opcoes[random.randint(0,len(opcoes)-1)]
    escolha=inserir_escolha()
    resultado=0#1=empate,2=vitoria,3=derrota
    if opcao == escolha:
        resultado=1

    #derrota
    elif opcao == opcoes[0] and escolha==opcoes[1]:
        resultado=2
    elif opcao == opcoes[1] and escolha==opcoes[2]:
        resultado=2
    elif opcao == opcoes[2] and escolha==opcoes[0]:
        resultado=2

    elif escolha == opcoes[0] and opcao==opcoes[1]:
        resultado=3
    elif escolha == opcoes[1] and opcao==opcoes[2]:
        resultado=3
    elif escolha == opcoes[2] and opcao==opcoes[0]:
        resultado=3

    if resultado==1:
        print("empate")
    elif resultado==3:
        print("derrota")
    elif resultado==2:
        print("vitoria")

while True:
    jogar()