import requests
from bs4 import BeautifulSoup

URL = 'https://leagueoflegends.fandom.com/wiki/Aatrox/LoL'  # replace with the URL of the page you want to scrape
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

response = requests.get(URL, headers=headers)

#check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

abilityDiv = soup.findAll('div', 'ability-info-container')

#abilityCoeff = soup.findAll('dd', '')

for dd in abilityCoeff:
# print('++++++++')
# print(dd.text)
# print('++++++++')

for div in abilityDiv:
    print('SECTION')
    abilityCoeff = div.findAll('dd')
    for ability in abilityCoeff:
        print('++++++++')
        print(ability.text)
        print('++++++++')