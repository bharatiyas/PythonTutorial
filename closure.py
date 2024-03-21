# Closure is a function having access to the scope of its parent function
# After the parent function has returned

# Creating closures is a good way to avoid creating global variable

def paren_function(person, coins):
    # coins = 3         # We can have coins as an input param or variable, for closures to work

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.") 
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.") 
        else:
            print("\n" + person + " has no coins left.") 

    return play_game    # Here we are creating a closure, when the parent function is returning the child function

tommy = paren_function("Tommy", 4)   # This is start of Functional Programming because are assigning a function to a variable
tommy()     # And then calling the function using a variable. And with each call the values of the variables returned in the
            # previous call are retianed. It is behaving similar to recursion.

jenny = paren_function("Jenny", 5)

 
tommy() # We are able to save the value of coins across multiple function calls

jenny()




