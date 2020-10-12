#Update to python 3 lol

# Will fetch the html files
import requests

# Pulls data from html files
from bs4 import BeautifulSoup

import urllib.request

import random



def weapon_parser():
    # A comprehensive webpage containing ample amount of cyber punk weapon info
    url = "https://cyberpunk.fandom.com/wiki/Weapons_in_Cyberpunk_2020"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup((response.read()), "lxml")
    counter = 0
    table = soup.findAll('table')
    random_weapon = random.randint(0,len(table))

    placeholder = True


    print("The rarities are as follows: poor, common, rare, excellent")
    rare = input("Enter the rarity you desire: ")
    print(rare)
    #rare = rare.lower()
    print(rare)
    options = ["poor","common","rare","excellent"]


    while(placeholder):
        random_weapon = random.randint(0,len(table))
        if (len(table) > random_weapon): #Defensive coding
            for row in table[random_weapon].findAll('tr'):
                rarity = row.findAll('td')

                if (len(rarity)>4):
                    #print('Hi %s' %rarity[4].text)
                    if ((rarity[4].get_text(strip=True)) == rare):
                        placeholder = False
                        print(row.find('td').get_text(strip =True))
                        break


def main():
    weapon_parser()

main()
