constante_de_conversão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteparaKB(valorASerConvertido):
    print('valor convertido de byte para KB')
    KBCalculado = valorASerConvertido / constante_de_conversão
    return KBCalculado

def KBparabyte(valorASerConvertido):
    print('valor convertido de KB para byte')
    byteCalculado = valorASerConvertido * constante_de_conversão
    return byteCalculado

print('Insira o valor a ser convertido de bit para Byte')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de Byte para KB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = byteparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)



print('Insira o valor a ser calculado de KB para Byte')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de byte para bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)