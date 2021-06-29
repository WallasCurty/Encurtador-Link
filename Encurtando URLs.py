

import pyshorteners

#URL a ser encurtada
url = input("Digite a url que deseja encurtar:")
 
#Carrega a lib
s = pyshorteners.Shortener()

#Gera a URL encurtada
shortUrl = s.tinyurl.short(url)

#Mostra a nova url
print(f"URL Encurtada: {shortUrl}")
