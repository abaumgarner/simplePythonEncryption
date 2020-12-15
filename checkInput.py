#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 12/14/20
    Notes: Various functions to check user input for the main python script. Functions are 
            genericized enouth to work with other scripts if needed.

"""
import re
import fileIO

""" Checks menu option entered is in the menu """
def checkOption(option, options):
    found = False
    optionRegex = re.compile(options)
    if re.match(optionRegex, option):
        found = True
    return found

""" Prompts the user for a file name. If it does not exist then prompt till exists """
def promptFileName(path):
    exist = False

    while exist != True:
        fileName = path
        fileName += input("File Name: ")
        exist = fileIO.checkFileExists(fileName)
        if exist == False:
            print("File " + fileName + " wasn't found. Please try again.\n")
            path = input("Folder File is in: ")
            path += "/"
    return fileName

""" Prompts user for a number and checks to see if what is entered is a number. Then returns it """
def promptNumber():
    isNum = False

    while isNum != True:
        num = input("Secret Number: ")
        isNum = num.isdigit()

        if isNum == False:
            print(num + " is not a number. Please try again.\n")
    return int(num)