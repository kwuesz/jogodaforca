# colocar mai sde umma letra, digitar a palavra inteira
# importando o random e json

import random 
import json

# função para mostrar as letras que o usuario acertou
def mostrar(pos_letr_acrt):
    global nome 
    global letr_restantest
    letr_restantes[pos_letr_acrt] = nome[pos_letr_acrt]
    print(letr_restantes)
# função para escolher a categoria   
def catego():
    print("""
1- nomes
2- carros
3- frutas
4- t.i
""")
    categ_esc = int(input("escolha a categoria: "))
    if categ_esc == 1:
        # usando o metodo with open nao preciso fachar o arquivo
        with open('json/nomes.json') as arquivo: 
            dados = json.load(arquivo)
    elif categ_esc == 2:
        with open('json/carros.json') as arquivo: 
            dados = json.load(arquivo)
    elif categ_esc == 3:
        with open('json/frutas.json') as arquivo: 
            dados = json.load(arquivo)
    elif categ_esc == 4:
        with open('json/t_i.json') as arquivo: 
            dados = json.load(arquivo)
    return dados

repetidor1 = 0

while repetidor1 < 1:
    dados = catego()
    # pegando o numero de itens do arquivo json escolhido 
    tam_dados = len(dados)
    # sorteando um numero dentro do tamanho do json  
    num_ale = random.randrange(0,tam_dados) 
    nome = dados[num_ale]["nome"]
    tam_nome = len(nome) 
    tentativas = 6
    # numero de vezes que o usuario acertou as letras 
    acertos_letr = 0 
    # acertos gerais, para coparação com as tentativas
    acertos = 0
    pontos = 0
    letr_restantes = ["_"]*tam_nome 
    repetidor2 = 0

    print(f"a palavra é: \n {letr_restantes}")
    # iniciando a repetição para tentativas 
    while repetidor2 < 1:
        letr_insert = input("digite a letra: ") 
        # variavel feita para saber se foi acertado ou não, diminuir o numero de tentativas  
        acert = False
        # repetição para saber se a letra inserida pelo usuario esta no nome sorteado
        for y in range(tam_nome): 
            if letr_insert == nome[y]: 
                pos_letr_acrt = y
                # mandando a posição da letra acertada para a função
                mostrar(pos_letr_acrt)
                acertos_letr += 1
                acert = True
                
        if acert != True:
            tentativas -= 1   
                
        print(f"tentativas restantes sao igual de: {tentativas}") 
        
        if tentativas == 0: 
            print("VOCE PERDEU!!!")
            print(f"a palavra era: {nome}")
            break
            # ou: repetidor += 1
        
        
        for x in range(tam_nome):
            # comparando cada letra inserida pelo usuario 
            if letr_restantes[x] == nome[x]:
                acertos +=1
        if acertos == tam_nome:
            print(" PARABENS! VOCE ACERTOU! ")
            print(f"a palavra era: {nome}")
            pontos += 1
            break
            # ou: repetidor += 1
        else:
            # atribuindo os acertos de letra certos e removendo os acertos 
            acertos_letr = acertos
            acertos = 0 
    print("deseja continuar?(preesione enter para seguir)")  
    cont = input("")
    if cont != "":
        break