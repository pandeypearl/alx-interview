#!/usr/bin/python3
""" A method that checks if a given data set represents a valid UTF-8 """


def eight_bits(integer):
    """ A function that:
    converts an integer to its binary representation,
    removes the 'Ob' prefixe
    and returns the full 8 bits of the binary string """
    binary = bin(integer)[2:]
    add = '0' * (8 - len(binary))
    return add + binary


def validUTF8(data):
    """ A method that checks if a given data set represents a valid UTF-8 """
    i = 0
    while i < len(data):
        if eight_bits(data[i])[0] == '0':
            i += 1
        elif (eight_bits(data[i])[:3] == '110' and i + 1 < len(data) and
                eight_bits(data[i + 1])[:2] == '10'):
            i += 2
        elif (eight_bits(data[i])[:4] == '1110' and i + 2 < len(data) and
                eight_bits(data[i + 1])[:2] == '10' and
                eight_bits(data[i + 1])[:2] == '10'):
            i += 3
        elif (eight_bits(data[i])[:5] == '11110' and i + 3 < len(data) and
                eight_bits(data[i + 1])[:2] == '10' and
                eight_bits(data[i + 2])[:2] == '10' and
                eight_bits(data[i + 3])[:2] == '10'):
            i += 4
        else:
            return False
    return True
