#!/usr/bin/env python3

""" Author: Aaron Baumgarner
    Created: 12/14/20
    Updated: 12/14/20
    Notes: Collection of functions to do a simple bit shift strings/lists in ASCII code to encrypt the text

"""
""" Takes an input string, changes the chars to ASCII codes, shifts the code by an amount, and returns as a string """
def encodeString(string, num):
    code = ""

    for char in string:
        code += str(ord(char)+num) + " "
    return code.strip()

""" Takes an input string, changes the ASCII codes to chars after shifting by an amount, and returns as a string"""
def decodeString(string,num):
    code = ""
    temp = string.strip().split(" ")

    for ascii in temp:
        if ascii != "":
            code += str(chr(int(ascii)-num))
        
    return code

""" Takes a list, encodes each line with the encodeString function, and saves to a new list before returning it """
def encodeAra(ara, num):
    encode = []
    
    for line in ara:
        encode.append(encodeString(line, num))
    encode.pop()

    return encode

""" Takes a list, decodes each line with the decodeString function, and saves to a new list before returning it """
def decodeAra(ara, num):
    decode = []

    for line in ara:
        decode.append(decodeString(line, num))
    decode.pop()

    return decode