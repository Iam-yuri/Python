filme1 = "O menino do pijama listrado"
filme2 = "A viagem de Chihiro"
filme3 = "Mad Max: Estrada da furia"
print(filme1, filme2, filme3)

filmes = ["O menino do pijama listrado", "A viagem de Chihiro", "Mad Max: Estrada da furia"]
print(filmes)

filmes = [filme1, filme2, filme3]
print(filmes)

def imprime_filmes(filmes_imprimrir):
    print("Lista de filmes disponíveis")
    print(filmes_imprimrir)

imprime_filmes(filmes)
imprime_filmes(filmes)
imprime_filmes(filmes)

filmes[1]
print(filmes)
filmes[-1]
print(filmes)
filmes[-2]
print(filmes)
filmes[1:]
print(filmes)

for filme in filmes:
    print(filme)

for filme in filmes:
    print(filme)
    print("...")
print("Fora")

def imprime_filmes(filmes_imprimrir):
    print("Lista de filmes disponíveis")
    for filme in filmes_imprimrir:
        print(filme)

imprime_filmes(filmes)