# import requests module
import requests
 
# Making a get request


response = requests.get('https://api.github.com/search/repositories?q=language:python')
  

# print response
print(response)
 
# print json content
print(response.json())