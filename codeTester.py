#!/usr/bin/env python3

import simpleEncryption

def testCode():
    string = "a b"
    print(string)

    code = simpleEncryption.encodeString(string, 100)
    print(code)

    code = simpleEncryption.decodeString(code, 100)
    print(code)