

class Calculator(object):
    # We are defining a Class called Calculator that derives from object (ISA).
    # This class will encapsulate functionality associated with a calculator.

    def add(self, value1, value2):
        # This function returns the sum of the two values.
        # self, the first argument to the function, is a reference to the
        # Calculator instance.
        return value1 + value2
