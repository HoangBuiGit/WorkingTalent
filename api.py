print("start api request")

import requests
print("test")
paginaresults = requests.get("https://catfact.ninja/facts")
feitjes = paginaresults.json

print(feitjes["data"][0])