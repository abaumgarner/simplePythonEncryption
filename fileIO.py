#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/9/20
    Updated: 12/14/20
    Notes: Opens a file and reads each line into a list. Able to save a new line to the file. Made as
            generic as possible to be used for other projects. 
            12/14/20 - Added a save to file which saves a list to a file with each element being a new line
            
"""
import os.path

""" Opens and reads in all lines from the users text file. Returns as a list """
def getLines(fileName):
    lines = open(fileName, 'r')
    allLines = []
    while True:
        line = lines.readline()
        allLines.append(line.rstrip('\n'))

        if not line:
            lines.close()
            break
    return allLines

""" Saves a new line to the file """
def saveNewLine(line, fileName):
    fout = open(fileName, "a")
    fout.write(line +"\n")
    fout.close()

""" Checks if file given eists """
def checkFileExists(fileName):
    return os.path.isfile(fileName)

""" Saves a list to a file """
def saveToFile(ara, fileName):
    fout = open(fileName, "w")
    temp = []

    for line in ara:
        temp.append(line + "\n")

    last = temp.pop()
    temp.append(last.replace("\n",""))

    fout.writelines(temp)
    fout.close()
