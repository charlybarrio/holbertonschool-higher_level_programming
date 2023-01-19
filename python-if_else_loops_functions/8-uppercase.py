#!/usr/bin/python3
def uppercase(str):

    Ascii = ""
    strMayus = ""
    Strlrg = len(str)

    for n in range(Strlrg):
        Ascii = ord(str[n])
        if (97 <= Ascii <= 122):
            Ascii = Ascii - 32
        strMayus += chr(Ascii)

    print("{}".format(strMayus))
