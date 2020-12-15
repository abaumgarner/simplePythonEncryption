#!/usr/bin/env python3
""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 12/14/20
    Notes: Simple functions to show a user a menu and prompt for an option within the menu. This was
            done to brush up on programming and just for fun. For a real encryption an external harden
            library should be used.
"""

import simpleEncryption
import fileIO
import codeTester
import checkInput

def displayMenu():
    print()
    print("Super fun menu")
    print("--------------")
    print("1) Test Script")
    print("2) Encrypt File")
    print("3) Decrypt File")
    print("4) Print Encrypt to Screen")
    print("5) Print Decrypt to Screen")
    print("6) Save Encrypt to File")
    print("7) Save Decrypt to File")
    print("0) Exit")
    print()

def promptMenuOption():
    checkOption = False

    while checkOption != True:
        option = input("Option: ")
        checkOption = checkInput.checkOption(option,"[0-7]")

        if checkOption == False:
            print("Option " + option + " is not in the menu. Please try again.\n")
            displayMenu()
    return option

def executeOption(option, encrypt, decrypt):
    if option == 1:
        codeTester.testCode()
    elif option == 2:
        path = input("Folder File is in: ")
        path += "/"
        fin = checkInput.promptFileName(path)
        lines = fileIO.getLines(fin)
        secretNum = checkInput.promptNumber()

        return simpleEncryption.encodeAra(lines, secretNum)
    elif option == 3:
        path = input("Folder File is in: ")
        path += "/"
        fin = checkInput.promptFileName(path)
        lines = fileIO.getLines(fin)
        secretNum = checkInput.promptNumber()

        return simpleEncryption.decodeAra(lines, secretNum)
    elif option == 4:
        print(encrypt)
    elif option == 5:
        print(decrypt)
    elif option == 6:
        fout = input("Folder File is in: ")
        fout += "/"
        fout += input("Output File Name: ")
        fileIO.saveToFile(encrypt, fout)
    elif option == 7:
        fout = input("Folder File is in: ")
        fout += "/"
        fout += input("Output File Name: ")
        fileIO.saveToFile(decrypt, fout)
    elif option == 0:
        exit()
    else:
        print("Not sure how you got here..... o.O")