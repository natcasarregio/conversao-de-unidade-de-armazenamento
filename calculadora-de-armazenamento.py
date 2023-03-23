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

def KBparaMB(valorASerConvertido):
    print('valor convertido de KB para MB')
    MBCalculado = valorASerConvertido / constante_de_conversão
    return MBCalculado

def MBparaKB(valorASerConvertido):
    print('valor convertido de MB para KB')
    KBCalculado = valorASerConvertido * constante_de_conversão
    return KBCalculado

def MBparaGB(valorASerConvertido):
    print('valor convertido de MB para GB')
    GBCalculado = valorASerConvertido / constante_de_conversão
    return GBCalculado

def GBparaMB(valorASerConvertido):
    print('valor convertido de GB para MB')
    MBCalculado = valorASerConvertido * constante_de_conversão
    return MBCalculado

print('Insira o valor a ser convertido de bit para Byte')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de Byte para KB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = byteparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de KB para MB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = KBparaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de MB para GB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = MBparaGB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de GB para MB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = GBparaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de MB para KB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = MBparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser calculado de KB para Byte')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de byte para bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)