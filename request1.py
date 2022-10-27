# import requests module
import requests
 
# Making a get request
lista = []
laskuri = 0
while laskuri < 5:
    response = requests.get('https://catfact.ninja/fact')
    lista += response
    laskuri += 1

# print response
print(lista)
 
