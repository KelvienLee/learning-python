import requests

url = 'https://github.com/jbyuki/instant.nvim'
r_get = requests.get(url)


print(r_get.text)