import requests

BASE= "http://127.0.0.1:5000/"

word="Hello How Are You"
response = requests.get(BASE+ "helloworld/" +word)

print(response )