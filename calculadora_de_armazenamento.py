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
    print('valor convertido  de GB para MB')
    MBCalculado = valorASerConvertido * constante_de_conversão
    return MBCalculado

def GBparaTB(valorASerConvertido):
    print('valor convertido de GB para TB')
    TBCalculado = valorASerConvertido / constante_de_conversão
    return TBCalculado

def TBparaGB(valorASerConvertido):
    print('valor convertido  de TB para GB')
    GBCalculado = valorASerConvertido * constante_de_conversão
    return GBCalculado

def TBparaPB(valorASerConvertido):
    print('valor convertido de TB para PB')
    PBCalculado = valorASerConvertido / constante_de_conversão
    return PBCalculado

def PBparaTB(valorASerConvertido):
    print('valor convertido de PB para TB')
    TBCalculado = valorASerConvertido * constante_de_conversão
    return TBCalculado

