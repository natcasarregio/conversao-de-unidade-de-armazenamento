#valores constantes e lista de unidade
unidades_de_armazenamento = ['bit','byte','Kb','Mb','Gb','Tb','Pb']
VALOR_CONVERSAO = 1024
VALOR_CONVERSAO_BIT = 8

print('Bem vindo(a)!Essa é uma calculadora de unidade de armazenamentos \n Aqui está as unidades que você pode usar:', unidades_de_armazenamento)
print('\n Insira os valores pedidos:')

def repeticao ():
    #dados inseridos
    unidade_inicial = input(" Unidade Inicial:")
    while unidade_inicial not in unidades_de_armazenamento:
        unidade_inicial = input("Unidade invalida insira uma que tem na lista")
    else:
        posicao_inc = unidades_de_armazenamento.index(unidade_inicial)

    unidade_final = input(" Unidade Final:")
    while unidade_final not in unidades_de_armazenamento:
        unidade_final = input("Unidade invalida insira uma que tem na lista:")
    else:
        posicao_final = unidades_de_armazenamento.index(unidade_final)

    valor_converter = int(input(" Valor a ser convertido:"))

    #conversão da unidade bit
    def conversao ():
        if unidade_inicial == 'bit' and unidade_final != 'bit':
            primeira_conversao = valor_converter/ VALOR_CONVERSAO_BIT
            distancia = posicao_final - unidades_de_armazenamento.index('byte')
            resultado = primeira_conversao/ (VALOR_CONVERSAO**distancia)
        elif unidade_final == 'bit' and unidade_inicial != 'bit':
            distancia = posicao_inc - unidades_de_armazenamento.index('byte')
            primeira_conversao = valor_converter * (VALOR_CONVERSAO)
            resultado = primeira_conversao * VALOR_CONVERSAO_BIT
        elif unidade_final == 'bit' and unidade_inicial == 'bit':
            resultado = valor_converter
    #conversão das outras unidades
        else:
            if posicao_inc >= posicao_final:
                distancia = posicao_inc - posicao_final
                resultado = valor_converter * (VALOR_CONVERSAO ** distancia)
            elif posicao_inc < posicao_final:
                distancia = posicao_final - posicao_inc
                resultado = valor_converter / (VALOR_CONVERSAO ** distancia)
        print('\n O resultado da conversão é:',resultado, unidade_final)
    conversao()
repeticao()

parar_calculadora = False
while parar_calculadora == False:
    print('Quer continuar calculando? Responda com "Sim" ou "Não":')
    repetir = input()
    if repetir == 'Sim':
        repeticao()
    else:
        repetir == 'Não'
        print('Obrigada por utilizar a calculadora até a proxima volte logo :)')
        parar_calculadora = True
