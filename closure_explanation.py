############################ Explanation from other channel #############################################

# Closure: When an inner function is returned from outer function then it carries the state of the outer function scope
# State means all the variable defined in the outer function as also present for access

def create_traffic_light_validator():   # outer function
    traffic_light_colors = ("GREEN", "RED", "ORANGE")

    def is_valid_light(color):      # inner function
        if color.upper() in traffic_light_colors:
            return True
        else:
            return False
        
    return is_valid_light       # We are retuning an iiner function from an outer function
                                # Functions in python are objects
                                # They can be passed as arguments in other functions and can be returned from another function

# Now validator is a new variable which is pointing to the function object which is pointed by is_valid_light()
# From this point onwards validator == is_valid_light()
# validator and is_valig_light are poiniting to the same function object
validator = create_traffic_light_validator()    

color = "Green"
print(validator(color))        # This will now invoke is_valid_light()