import requests

r = requests.get('http://openedsauce.com')
print(r.status_code)
print(r.ok)
