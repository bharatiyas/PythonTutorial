class CustomException(Exception):
    pass

try:
    print(x)
except:     # Catch all exceptions
    print('Caught generic exception')

x = "2"
try:
    print(x)
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
    
    if not type(x) is int:
        # raise Exception('Type can only be int')     # raise custom exception
        raise CustomException("Custom Exception Class. Type can only be int")
    
except NameError:   # Catch a specific error, ex - NameError
    print('Caught Name Error. Something is undefined!!')
except ZeroDivisionError:
    print('Division by zero is not allowed')
except Exception as error:              # For custom exception
    print("Custom exception caught - ")
    print(error)
else:           # When no errors are thrown
    print('No errors!')    
finally:
    print('Finally reached finally ')   # Control reaches here with or without an error

