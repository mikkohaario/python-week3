

with open ("exercise4-wordlist.txt") as file:
    lista = [line.rstrip() for line in file]
    

lista.sort() # sorts normally by alphabetical order
lista.sort(key=len) # sorts by descending length

with open(r"new_wordlist2.txt", "w") as tiedosto:
    tiedosto.write("\n".join(lista))