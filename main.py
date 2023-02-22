"""
Author: UC3M
MODIFIED BY TEAM 20 (Eduardo Alarcón and Sergio Barragán)
"""
# pylint: disable=import-error
# This one is added to avoid the warning of the import error, which is the import of UC3MLogistics
import string
from barcode import EAN13
from barcode.writer import ImageWriter
from UC3MLogistics import OrderManager

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3


def Encode(word):
    """
    This functions encodes a number
    :param word: EAn13 number
    :return: string
    """
    Encoded = ""
    for Letter in word:
        if Letter == ' ':
            Encoded = Encoded + ' '
        else:
            Xvariable = (letters.index(Letter) + shift) % len(letters)
            Encoded = Encoded + letters[Xvariable]
    return Encoded

def Decode(word):
    """
    This function decode the EAn13 Number
    :return: string
    """
    Encoded = ""
    for Letter in word:
        if Letter == ' ':
            Encoded = Encoded + ' '
        else:
            Xvariable = (letters.index(Letter) - shift) % len(letters)
            Encoded = Encoded + letters[Xvariable]
    return Encoded

def Main():
    """
    main functin of the
    encode / deconde function for EAn13 numbers
    :return:
    """
    Mng = OrderManager()
    Res = Mng.read_product_code_from_json("test.json")
    StrRes = str(Res)
    #StrRes = Res.__str__()
    print(StrRes)
    EncodeRes = Encode(StrRes)
    print("Encoded Res "+ EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)
    print("Codew: " + Res.product_code)
    with open("barcodeEan13.jpg", 'wb') as Stored:
        Imagew = ImageWriter()
        EAN13(Res.product_code, writer=Imagew).write(Stored)


if __name__ == "__main__":
    Main()
