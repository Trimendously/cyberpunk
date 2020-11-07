from character_creation import*
from weapons import*

def main():
    x = 0
    # Creating an interface for my Cyberpunk program
    characters = []
    print('Hello welcome to the Cyberpunk 2020 RPG Character creator.')
    print('This project is possible all through the great people behind the Cyberpunk at https://cyberpunk.fandom.com so a great thanks to all of you for making this possible.')
    print('This character creator is designed to be used to quickly create background/ combatant characters, who don\'t need immediate background info.')
    character_count = int(input('Please enter how many characters that you would like to create today:  '))
    #characters = [character_count]
    while(character_count > x):
        print('\nCreation for character ', (x+1))
        type = input('Enter whether the character is a \'armed\' or \'unarmed\'\n')
        if (type == 'armed'):
            sex = gender()
            characters.append(physical_description(name(sex),ancestry(),sex,age()))
            characters[x].introduction()
            stats()
            print('Weapon stats: ')
            weapon_parser()
            #situation() # Need to fix this first
        elif (type == 'unarmed'):
            sex = gender()
            characters[x] = physical_description(name(sex),ancestry(),sex,age())
            characters[x].introduction()
            stats()
        else:
            print('Please enter the type of character properly with no gramatical mistakes.')
            x = x -1 # Keeps the code at the same point in the loop
        x = x+1
    print('Thank you for using this Cyberpunk program. It is still a work in progress so any suggestions are more than welcome.')

main()
