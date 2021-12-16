import typing

valor = ("Hi", "Python", 2)
#Verificando o tipo do valor
print(type(valor))

#imprimindo o valor
print(valor)

#Valor Cortado
print(valor[1:])
print(valor[0:1])

#Valor concatenado usando + operador
print(valor + valor)

#Valor repetido usando * operador
print(valor * 3)

#Adicionando valores a esse valor. Isso gerará um erro.
typing[2] = "Hi"