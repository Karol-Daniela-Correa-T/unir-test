import math            

from app import util   


class InvalidPermissions(Exception):   
    pass                               


class Calculator:                      

    def add(self, x, y):              
        self.check_types(x, y)         
        return x + y                   

    def substract(self, x, y):         
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):          
        if not util.validate_permissions(f"{x} * {y}", "user1"):   
            raise InvalidPermissions("User has no permissions")    
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):            
        self.check_types(x, y)
        if y == 0:                     
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):             
        self.check_types(x, y)
        if x == 0 and y < 0:           
            raise TypeError("Zero cannot be raised to a negative power")
        if x < 0 and not float(y).is_integer():   
            raise TypeError("Negative base requires an integer exponent")
        return x ** y                 

    def sqrt(self, x):                 
        self.check_type(x)             
        if x < 0:                      
            raise TypeError("Square root of a negative number is not possible")
        return math.sqrt(x)            

    def log10(self, x):                
        self.check_type(x)
        if x <= 0:                     
            raise TypeError("Logarithm is only defined for positive numbers")
        return math.log10(x)

    @staticmethod                      
    def check_type(value):           
        if isinstance(value, bool) or not isinstance(value, (int, float)):   
            raise TypeError("Parameters must be numbers")

    def check_types(self, x, y):       
        self.check_type(x)
        self.check_type(y)


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)