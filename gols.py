time1 = vars("Digite o nome do time 1: ")
time2 = vars("Digite o nome do time 2: ")
totalgols1 = print(int("Digite quantos gols o time 1 fez: "))
totalgols2 = print(int("Digite quantos gols o time 2 fez: "))

if totalgols1 > totalgols2:

    print("O time" + time1 + "ganhou a partida com" + totalgols1 + "gols")

elif totalgols1 == totalgols2:

    print("Empate")

elif totalgols1 < totalgols2:

    print("O time" + time2 + "ganhou a partida com" + totalgols2 + "gols")