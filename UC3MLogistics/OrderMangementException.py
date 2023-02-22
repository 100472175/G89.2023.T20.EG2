# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unused-variable
# This one is added to avoid the warning of the unused variable, which is the name of the class
class OrderManagementException(Exception):
    """
    This is the class that manages the exceptions of the OrderManager class.
    It also manages the exceptions of the OrderRequest class.
    """
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value
