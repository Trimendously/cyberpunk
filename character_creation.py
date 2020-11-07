# File to create actual character
# Will fetch the html files
import requests
#import PyPDF2

#import names #Having trouble getting a library so may make my own or webscrape
# Pulls data from html files
from bs4 import BeautifulSoup
import urllib.request
import random


import array as ar

def randomizer(a,b): #Just trying to make code more conscise
    return random.randint(a, b)

class physical_description:
    #Will eventually balance so that either I or you the user can decide the proportion of each category
    def __init__(person, name, ancestry, gender, age):
        person.name = name
        person.ancestry = ancestry
        person.gender = gender
        person.age = age
    def introduction(person):
        print(person.name , " is a " , person.age , " year old " , person.ancestry, person.gender ,".")

def name(gender):
    if (gender == 'male'):
        file = open('boy_names.txt')
    elif(gender == 'female'):
        file = open('girl_names.txt')
    else:
        print("Error")
        return
    random_name = randomizer(0,999)
    lines = file.readlines()

    return lines[random_name].rstrip("\n")

def gender():
    gender = randomizer(0,2)
    if (gender == 0):
        return 'male'
    elif (gender == 1):
        return 'female'

def ancestry():
    ancestry_file = open("ancestry.txt")
    lines = ancestry_file.readlines()
    random_ancestry = randomizer(0,len(lines))

    return lines[random_ancestry].rstrip("\n")
"""
#Need to edit this still
def roles():
    supported_roles = ["Rockerboy", "Solo", "Netrunner", "Techie", "Media", "Cop", "Corporate", "Fixer", "Nomad"]
    url = "https://rpg.web-mage.ca/pages/roles.php"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    soup = BeautifulSoup((response.read()), "lxml")
    table = soup.findAll('table') #All tables on this website
"""
def age():
    return randomizer(18,50)

def quality(sum,type):
    if (sum >= 9):
        if (type != 'inhuman'):
            return False
    elif (sum > 5):
        if (type != 'trained'):
            return False
    elif (sum == 5):
        if (type != 'average'):
            return False
    else:
        if (type != 'subpar'):
            return False
    return True

def stats():
    skills = ar.array('i', range(9))
    skill_names = ["INTELLIGENCE","REFLEX","DEXTERITY","TECHNOLOGY","COOL","LUCK","MOVEMENT","BODY SIZE","EMPATHY"]
    type = input('Enter the type of person you desire from the following: inhuman, trained, average, or subpar.\n')
    x = 0
    while (x < 9):
        skills[x] = randomizer(0,10)
        x = x +1
        if (x == 9):
            sum = 0
            for i in skills:
                sum = sum + i
            if (quality(float(sum/9),type)):
                continue
            else:
                x = 0
    for x in range(0,9):
        print(skill_names[x],":", skills[x])
