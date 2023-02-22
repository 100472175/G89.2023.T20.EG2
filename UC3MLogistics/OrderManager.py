# pylint: disable=missing-module-docstring
import json
# Used to get the nearest number to the sum of the 12 elements of the barcode with .ceil
# pylint: disable=unused-variable
# Used to remove the warning of the unused variable, which is the name of the class
import math
from OrderMangementException import OrderManagementException
from OrderRequest import OrderRequest


class OrderManager:
    """
    This is the class that manages the orders.
    It is in charge of reading the JSON file.
    """

    def __init__(self):
        pass

    def validate_ean13(self, ean13):
        """
        This function validates the EAN13 code.
        :param eAn13:
        :return:
        """
        CheckSum = 0
        for i in range(len(ean13) - 1):
            CurrentNumber = int(ean13[i])
            if i % 2 != 0:
                CheckSum += CurrentNumber * 3
            else:
                CheckSum += CurrentNumber
        Difference = 10 * math.ceil(CheckSum / 10) - CheckSum
        return int(ean13[-1]) == Difference

    def read_product_code_from_json(self, fi):
        """
        This function reads the product code from the JSON file.
        And raises an exception if the file is not found or the JSON is not valid.
        """
        try:
            with open(fi, encoding='utf-8') as File:
                Data = json.load(File)
        except FileNotFoundError as Elem:
            raise OrderManagementException("Wrong file or file path") from Elem
        except json.JSONDecodeError as Elem:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from Elem

        try:
            PRODUCT = Data["id"]
            PhP = Data["phoneNumber"]
            ReqOrd = OrderRequest(PRODUCT, PhP)
        except KeyError as Elem:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from Elem
        if not self.validate_ean13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return ReqOrd
