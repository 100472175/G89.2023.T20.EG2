import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

"Used to get the nearest number to the sum of the 12 elements of the barcode with .ceil"
import math

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13( self, eAn13 ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        check_sum = 0
        for i in range(len(eAn13)-1):
            if eAn13[i] % 2 != 0:
                check_sum += eAn13[i]*3
            else:
                check_sum += eAn13[i]
        difference = 10*math.ceil(check_sum%10) - check_sum
        return eAn13[-1] == difference

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req