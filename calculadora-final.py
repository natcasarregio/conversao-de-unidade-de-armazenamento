#valores constantes e lista de unidade
unidades_de_armazenamento = ['bit','byte','Kb','Mb','Gb','Tb','Pb']
VALOR_CONVERSAO = 1024
VALOR_COVERSAO_BIT = 8

print('Bem vindo(a)!Essa é uma calculadora de unidade de armazenamentos \n Aqui está as unidades que você pode usar', unidades_de_armazenamento)
print('\nInsira os valores pedidos:')

#dados inseridos
unidade_inicial = input(" Unidade Inicial:")
while unidade_inicial not in unidades_de_armazenamento:
    unidade_inicial = input("Unidade invalida insira uma que tem na lista")
else:
    posicao_inc = unidades_de_armazenamento.index(unidade_inicial)

unidade_final = input(" Unidade Final:")
while unidade_final not in unidades_de_armazenamento:
    unidade_final = input("Unidade invalida insira uma que tem na lista")
else:
    posicao_final = unidades_de_armazenamento.index(unidade_final)

valor_converter = int(input(" Valor a ser convertido:"))

#conversão dos valores
def conversao ():
    if posicao_inc >= posicao_final:
        distancia = posicao_inc - posicao_final
        resultado = valor_converter * (VALOR_CONVERSAO ** distancia)
    elif   posicao_inc < posicao_final:
        distancia = posicao_final - posicao_inc
        resultado = valor_converter / (VALOR_CONVERSAO ** distancia)
    print('\n O resultado da conversão é:',resultado, unidade_final)

conversao()