import requests
from requests_toolbelt.utils import dump

url = input("URL: ")
response = requests.get(url)

## Print all the response
# data = dump.dump_all(response)
# print(data.decode('utf-8'))

## Print the status code of the response
# print(response)

try:
    servidor = response.headers['Server']
    print(f"Server: {servidor}")
except KeyError:
    print("Erro!")