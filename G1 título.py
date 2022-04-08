import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com/'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

print(f"\n{' ':30} Títulos G1\n")
for pergunta in html.select('.feed-post-body'):  # classe do corpo do título
    titulo = pergunta.select_one('.feed-post-body-title')  # classe onde está o título
    print(titulo.text)  # extraindo somente o título
