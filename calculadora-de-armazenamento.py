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

print('Insira o valor a ser convertido de byte para bit')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido de bit para byte')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)