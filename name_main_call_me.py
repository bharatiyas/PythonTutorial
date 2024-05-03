# Every py file is not a script. Script is the file which has function to run

####   !script = module    ####

# module/library will have helper methods which are called in other modules or scripts. module will be imported in other
# file for using the functions and constants defined in the module

#### __name__   ####
# It is a special variable we use when we interact with modules
# It allows us to make a distinction between:
#   A) The modules (libraries, functions, classes) we import
#   B) And the Python file, into which we import A (above), that currently runs in the console

# All the functions in python starting with __ are callback functions, meaning we do not call them instead they are
# called by the interpreter
#### __main__   ####
# It is the value that represents the __name__ of the top level environment, where top level code runs


def call_me():
    print("If without if condition this function will be called even when we import this module")

# When the following line is uncommented then call_me() will be invoked even when name_main_call_me.py
# is imported in any other py file    
# call_me()
    
# In order to avoid the above problem we need to have the following check
    
if __name__ == '__main__':
    call_me()