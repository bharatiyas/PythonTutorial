# If we do not have a __name__ == '__main__' check in name_main_call_me.py file,
# the following import statement will result in executing the call_me() inside name_main_call_me file
# even without exclusively invoking the call_me()
import name_main_call_me    

# But when we have __name__ == '__main__' check in name_main_call_me.py file,
# we need to exclusively invoke the call_me()
name_main_call_me.call_me() 