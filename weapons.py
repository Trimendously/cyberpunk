# Will fetch the html files
import requests
# Pulls data from html files
from bs4 import BeautifulSoup
import urllib.request
import random

def randomizer(a,b): #Just trying to make the code more conscise
    return random.randint(a, b)

def userInput():
    print("The rarities are as follows: poor, common, rare, excellent")
    formatted_rarity = 'Empty'
    while True:
        rarity = input("Enter the rarity you desire:\n")
        formatted_rarity = rarity[:1].upper() + rarity[1:].lower() #Sets first letter to upper and rest to lower
        options = ["Poor","Common","Rare","Excellent"] # Valid inputs
        if formatted_rarity in options:
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

    while True:
        random_table = randomizer(0,len(table))
        if (len(table) > random_table): #Defensive coding
            weapon_type = table[random_table].findAll('tr') # Selects a random weapon table
            header = weapon_type[0].findAll('th') # The header row for the column
            random_weapon = randomizer(1,len(weapon_type)) #Start at index 1 to avoid header
            if (len(weapon_type) > random_weapon):
                weapon = weapon_type[random_weapon].findAll('td') # Selects random weapon
                if (len(weapon)>4): #Defensive coding
                    if ((weapon[4].get_text(strip=True)) == rare): #Strips to get rid of whitespace
                        try:
                            for i in range(0,len(weapon)-1):
                                print(header[i].get_text(strip=True), ": ", weapon[i].get_text(strip=True))
                        except Exception as e:
                            continue
                        break  # We have found a valid weapon
    #Note need to account for some weapons body restrictions + modifiers with body
#Currently unfinished
def situation():
    #Need to think over the situations more so I can pre edit out some guns such as no monoblades for simple thugs etc
    location = input('Is the combat in an \'urban\' or \'suburban\' area?\n')
    if ((location == 'urban')):
        long_range = False #
    elif (location == 'suburban'):
        long_range = True
    else:
        situation()

    #occasion = input('Are the individuals attacking or defending?')
