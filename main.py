# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import string
from barcode.writer import ImageWriter
from barcode import EAN13
from UC3MLogistics import OrderManager

# GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            enc = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[enc]
    return encoded


def decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            enc = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[enc]
    return encoded


def main():
    mng = OrderManager()
    res = mng.ReadproductcodefromJSON("test.json")
    #str_res = res.__str__()
    str_res = str(res)
    print(str_res)
    encode_res = encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.PRODUCT_CODE)
    with open("barcodeEan13.jpg", 'wb') as file:
        image_writer = ImageWriter()
        # res.PRODUCT_CODE = '6969694204200'
        EAN13(res.PRODUCT_CODE, writer=image_writer).write(file)


if __name__ == "__main__":
    main()
