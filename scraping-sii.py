from unittest import result
import bs4
from bs4 import BeautifulSoup
import requests

url_sii = "https://resultados.as.com/resultados/futbol/primera_rfef/2021_2022/clasificacion/"

page = requests.get(url_sii)
soup = BeautifulSoup(page.content, "html.parser")

# equipos

eq = soup.find_all('span', class_='nombre-equipo')

equipos = []
count = 0

for i in eq:
    if count < 20:
        equipos.append(i.text)
        count += 1
    else:
        break

# puntos

pts = soup.find_all("td", class_="destacado")

puntos = []
count = 0

for i in pts:
    if count < 20:
        puntos.append(i.text)
        count += 1
    else:
        break

# resultado


resultado = {}

for i in equipos:
    resultado[i] = puntos[equipos.index(i)]

del count

print(resultado)
