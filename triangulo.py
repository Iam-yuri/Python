ladoA = print("Digite o valor do lado A: ")
ladoB = print("Digite o valor do lado B: ")
ladoC = print("Digite o valor do lado C: ")

if ladoA < ladoB + ladoC & ladoB < ladoA + ladoC & ladoC < ladoA + ladoB:
    
    if ladoA == ladoB & ladoB == ladoC:

        mens = "Triangulo Equliatero"
    
    elif ladoA == ladoB | ladoB == ladoC:

        mens = "Triangulo Isoceles"

    else:

        mens = "Triangulo Escaleno"

else:

    mens = "Nao tem nenhuma forma de triangulo"

print("A forma do triangulo e: ", + mens)