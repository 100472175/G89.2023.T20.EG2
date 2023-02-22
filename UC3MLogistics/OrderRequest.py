# pylint: disable=missing-module-docstring
import json
from datetime import datetime


class OrderRequest:
    """
    This class is for creating a request latter implemented on OrderManager
    It also implements properties and setters
    """
    def __init__( self, idcode, phoneNumber ):
        self.__phone_number = phoneNumber
        self.__id_code = idcode
        JustNow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(JustNow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone( self ):
        """
        property of phone Number
        :return:
        """
        return self.__phone_number
    @phone.setter
    def phone( self, value ):
        """
        corresponding setter of phone Number
        :param value: the hidden value
        """
        self.__phone_number = value

    @property
    def product_code( self ):
        """
        property of product code
        :return:
        """
        return self.__id_code
    @product_code.setter
    def product_code( self, value ):
        """
        corresponding setter of product code
        :param value: the hidden value
        """
        self.__id_code = value
