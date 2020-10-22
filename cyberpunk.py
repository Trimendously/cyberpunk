from character_creation import*
from weapons import*

def main():
    # Creating an interface for my Cyberpunk program
    characters = []
    print('Hello welcome to the Cyberpunk 2020 RPG Character creator.')
    print('This character creator is designed to be used to quickly create background/ combatant characters, who don\'t need immediate background info.')
    character_count = int(input('Please enter how many characters that you would like to create today:  '))
    characters = [character_count]
    for x in range(0,character_count):
        print('\nCreation for character ', (x+1))
        type = input('Enter whether the character is a \'armed\' or \'unarmed\'\n')
        if (type == 'armed'):
            #characters[x] = physical_description(names.get_full_name(gender=gender()), gender(), ancestry(), age())
            characters[x] = physical_description('Blank', gender(), ancestry(), age()) # Temporarily blank name
            print(characters[x].name)
            stats()
            weapon_parser()
            #situation() # Need to fix this first
        elif (type == 'unarmed'):
            #characters[x] = physical_description(names.get_full_name(gender=gender()), gender(), ancestry(), age())
            characters[x] = physical_description('Blank', gender(), ancestry(), age()) # Temporarily blank name
            print(characters[x].name)
            stats()
        else:
            print('Please enter the type of character properly with no gramatical mistakes.')
            x = x-1 # Keeps the code at the same point in the loop
    print('Thank you for using this Cyberpunk program. It is still a work in progress so any suggestions are more than welcome.')

main()
