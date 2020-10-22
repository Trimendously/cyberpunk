# Will fetch the html files
import requests
# Pulls data from html files
from bs4 import BeautifulSoup
import urllib.request
import random

def userInput():
    InvalidInput = True
    print("The rarities are as follows: poor, common, rare, excellent")
    formatted_rarity = 'Empty'
    while (InvalidInput):
        rarity = input("Enter the rarity you desire:\n")
        formatted_rarity = rarity[:1].upper() + rarity[1:].lower()
        options = ["Poor","Common","Rare","Excellent"]
        for x in range(0,4):
            if (options[x] == formatted_rarity):
                InvalidInput = False
                break
    return str(formatted_rarity)


def weapon_parser():
    # A comprehensive webpage containing ample amount of cyber punk weapon info
    url = "https://cyberpunk.fandom.com/wiki/Weapons_in_Cyberpunk_2020"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup((response.read()), "lxml")
    table = soup.findAll('table') #All tables on this website

    rare = userInput()

    placeholder = True
    while(placeholder):
        random_table = random.randint(0,len(table))
        if (len(table) > random_weapon): #Defensive coding
            weapon_type = table[random_table].findAll('tr') # Selects a random weapon table
            random_weapon = random.randint(1,len(weapon_type))
            rarity = weapon_type[random_weapon].findall('td') # Selects random weapon
            if (len(rarity)>4): #Defensive coding (column 5 has rarities)
                if ((rarity[4].get_text(strip=True)) == rare): #Strips to get rid of whitespace
                    placeholder = False # We have found a valid weapon
                    print(row.find('td').get_text(strip =True))
                    break

def situation():
    #Need to think over the situations more so I can pre edit out some guns such as no monoblades for simple thugs etc
    location = input('Is the combat in an \'urban\' or \'suburban\' area?\n')
    if ((location == 'urban'):
        long_range = False #
    elif (location == 'suburban'):
        long_range = True
    else:
        situation()

    #occasion = input('Are the individuals attacking or defending?')
