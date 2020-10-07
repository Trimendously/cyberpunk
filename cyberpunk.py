# Pulls data from html files
from bs4 import BeautifulSoup

# Will fetch the html files
import requests

import random
def rarity():
    print('The rarities are as follows: poor, common, rare, excellent')
    rarity = raw_input('Enter the rarity you desire: ')
    rarity = rarity.lower()
    options = [poor,common,rare,excellent]
    InvalidInput = True
    while InvalidInput:
        for x in options:
            if options[x] == rarity:
                InvalidInput = False
                break
    return rarity.lower();

def weapon_parser():
    # A comprehensive webpage containing ample amount of cyber punk weapon info
    url = "https://cyberpunk.fandom.com/wiki/Weapons_in_Cyberpunk_2020"

    # Translates html code to python so as to be able to manipulate it
    article = requests.get(url).text

    soup = BeautifulSoup(article, 'lxml')

    weapon_type = soup.find_all('h3')
    weapon_table = soup.find_all('table', class_='WikiaTable')
    random_number = random.randint(1,len(weapon_type))

    print(weapon_type[random_number].span)
    weapon = weapon_table[random_number].findChildren('tr')
    #weapon[0] is header so ignore

    number = 0
    for x in weapon:
        weapon_description = x.findChildren('td')
        #5th column so index four has accuracy
        if weapon_description[4] == rarity():
            number = number+1
            potential_weapons[number] = x
    random_number = random.randint(1,len(potential_weapons))
    print(weapon[potential_weapons[random_number]])

def main():
    weapon_parser()

main()
