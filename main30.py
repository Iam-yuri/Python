terms = int(input("Digite um termo: "))
#Os primeiros dois termos iniciais
a = 0
b = 1
count = 0

#verifique se o número de termos é zero ou negativo
if (terms <= 0):
    print("Por favor insira um número inteiro válido")
elif (terms == 1):
    print("Sequencia de fibonacci ate",'limit',":")
    print(a)
else:
    print("Sequencia de Fibonacci")
    while (count < terms):
        print(a, end = '')
        c = a + b
        #Atualizano os valores
        a = b
        b = c
        
    count += 1