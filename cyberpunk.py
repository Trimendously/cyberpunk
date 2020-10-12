#Update to python 3 lol

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
        rarity = input("Enter the rarity you desire: ")
        formatted_rarity = rarity[:1].upper() + rarity[1:].lower()
        options = ["Poor","Common","Rare","Excellent"]

        for x in range(0,4):
            if (options[x] == formatted_rarity):
                InvalidInput = False
                break
hn
    return str(formatted_rarity)


def weapon_parser():

    # A comprehensive webpage containing ample amount of cyber punk weapon info
    url = "https://cyberpunk.fandom.com/wiki/Weapons_in_Cyberpunk_2020"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup((response.read()), "lxml")
    table = soup.findAll('table') #All tales on this website

    rare = userInput()


    placeholder = True
    while(placeholder):
        random_weapon = random.randint(0,len(table))
        if (len(table) > random_weapon): #Defensive coding
            for row in table[random_weapon].findAll('tr'):
                rarity = row.findAll('td')

                if (len(rarity)>4): #Defensive coding
                    if ((rarity[4].get_text(strip=True)) == rare): #Strips to get rid of whitespace
                        placeholder = False
                        print(row.find('td').get_text(strip =True))
                        break


def main():
    weapon_parser()

main()
