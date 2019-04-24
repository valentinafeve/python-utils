import requests

r = requests.get('https://www.facebook.com')
print(r.text)
