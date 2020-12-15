#!/usr/bin/env python3
""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 12/14/20
    Notes: Simple main to run all files needed for simple text incryption and decryption

"""
import menu

encrypt = []
decrypt = []

""" Infanate loop to run the program until the user selects the 0 exit option """
while True:
    menu.displayMenu()
    option = int(menu.promptMenuOption())
    if option == 2:
        encrypt = menu.executeOption(option,encrypt,decrypt)
    elif option == 3:
        decrypt = menu.executeOption(option,encrypt,decrypt)
    else:
        menu.executeOption(option,encrypt,decrypt)
