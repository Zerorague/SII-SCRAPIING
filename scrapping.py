import bs4
from bs4 import BeautifulSoup
import requests

url_sii = "https://resultados.as.com/resultados/futbol/primera_rfef/"

page = requests.get(url_sii)
soup = BeautifulSoup(page.content, "html.parser")

# equipos

eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()
