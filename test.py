import requests

name = input("Your name? ")
print("Hello, ", name)

r = requests.get('https://coreyms.com')
print(r.status_code)
print(r.ok)

