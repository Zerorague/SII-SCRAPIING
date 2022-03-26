import bs4
from bs4 import BeautifulSoup
import requests

url_sii = "https://www4.sii.cl/mapasui/internet/#/contenido/index.html"

result = requests.get(url_sii)
codigo_html = result.text

soup = BeautifulSoup(codigo_html, 'lxml')

soup.prettify()

caja = soup.find('div', class_='col-xs-12')

#coordenadas = soup.find('center')

print(caja.get_text())
