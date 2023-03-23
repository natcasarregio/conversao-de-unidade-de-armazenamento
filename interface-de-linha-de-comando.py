from calculadora_de_armazenamento import converterStringParaFloat, bitParaByte, byteParaBit, byteparaKB, KBparabyte, KBparaMB, MBparaKB, MBparaGB, GBparaMB,GBparaTB,TBparaGB,TBparaPB,PBparaTB

print(' -Escreva 1 para bitparaByte \n -Escreva 2 para Byteparabit \n -Escreva 3 para ByteparaKB \n -Escreva 4 para KBparaByte \n -Escreva 5 para KBparaMB \n -Escreva 6 para MBparaKB \n -Escreva 7 para MBparaGB \n -Escreva 8 para GBparaMB \n -Escreva 9 para GBparaTB \n -Escreva 10 para TBparaGB \n -Escreva 11 para TBparaPB \n -Escreva 12 para PBparaTB')
funEscolha = input()
if(funEscolha == '1'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funEscolha == '2'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '3'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = byteparaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '4'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '5'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = KBparaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '6'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaKB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '7'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = MBparaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '8'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaMB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '9'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = GBparaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '10'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaGB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '11'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = TBparaPB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(function == '12'):
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = PBparaTB(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)