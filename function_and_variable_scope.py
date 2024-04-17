# Global scope
# We should try not to have any global scope variables. This can lead to problems which can be hard
# to debug. To understand better watch: https://www.youtube.com/watch?v=g_wlZ9IhbTs

name = "Sanjay"
count = 1

def globalGreeting():
    # Local scoped variable
    color = "blue"
    #print(count)    # We can access the global variable count
    #count += 1 
    # ERROR: We CANNOT modify it inside the function
    
    global count    # Before modifying a global variable we need to declare it
    count += 1  # Now we can modify it
    print(count)

    print("Hello " + name)

def globalGreetingWithName(name):
    # Local scoped variable
    color = "blue"
    print("Hello " + name) # Function parameter takes precedence over global variable

def another():
    globalGreetingWithName("Vidrohi")   # Call one function from inside another function

def parent():
    parentColor = "purple"
    def child(name):
        color = "charcoal"
        #print(parentColor)  # variable defined in the parent function is accessible in child()
        print("child() - "+ name)
        nonlocal parentColor    # BUT To modify a variable defined in parent class
        parentColor = "child-purple"
        print("nonlocal parentColor - " + parentColor)

    child("Idhant") # Nested function can be ONLY called from the parent function. If this 
                    # needs to be only called from within the parent() then it should be 
                    # defined inside the parent(). You do not want to pollute the Global 
                    # scope by defining the child() in the global scope
    print("parent() - " + name)    

globalGreeting() # print(color) # This is error because color is scoped to the 
                 # function globalGreeting()

globalGreetingWithName("Bharatiya")
parent()


