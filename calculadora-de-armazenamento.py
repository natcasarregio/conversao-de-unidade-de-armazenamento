constante_de_conversão = 1024

def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteparaKB(valorASerConvertido):
    print('valor convertido para KB')
    KBCalculado = valorASerConvertido / constante_de_conversão
    return KBCalculado

def KBparabyte(valorASerConvertido):
    print('valor convertido para byte')
    byteCalculado = valorASerConvertido * constante_de_conversão
    return byteCalculado

def KBparaMB(valorASerConvertido):
    print('valor convertido para MB')
    MBCalculado = valorASerConvertido / constante_de_conversão
    return MBCalculado

def MBparaKB(valorASerConvertido):
    print('valor convertido para KB')
    KBCalculado = valorASerConvertido * constante_de_conversão
    return KBCalculado

def MBparaGB(valorASerConvertido):
    print('valor convertido para GB')
    GBCalculado = valorASerConvertido / constante_de_conversão
    return GBCalculado

def GBparaMB(valorASerConvertido):
    print('valor convertido para MB')
    MBCalculado = valorASerConvertido * constante_de_conversão
    return MBCalculado

def GBparaTB(valorASerConvertido):
    print('valor convertido para TB')
    TBCalculado = valorASerConvertido / constante_de_conversão
    return TBCalculado

def TBparaGB(valorASerConvertido):
    print('valor convertido para GB')
    GBCalculado = valorASerConvertido * constante_de_conversão
    return GBCalculado

def TBparaPB(valorASerConvertido):
    print('valor convertido para PB')
    PBCalculado = valorASerConvertido / constante_de_conversão
    return PBCalculado

def PBparaTB(valorASerConvertido):
    print('valor convertido para TB')
    TBCalculado = valorASerConvertido * constante_de_conversão
    return TBCalculado

print('Insira o valor a ser convertido de bit para Byte')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de Byte para KB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = byteparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de KB para MB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = KBparaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de MB para GB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = MBparaGB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de GB para TB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = GBparaTB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de TB para PB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = TBparaPB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de PB para TB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = PBparaTB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de TB para GB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = TBparaGB(entradaDoTecladoValorASerConvertido)
print(valorConvertido) 

print('Insira o valor a ser convertido de GB para MB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = GBparaMB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de MB para KB')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = MBparaKB(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de KB para Byte')
entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
valorConvertido = KBparabyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de byte para bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)