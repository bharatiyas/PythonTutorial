import argparse     # CLI option and argument, sub-commands parsing library

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "Hindi": "Namaste"
    }

    msg = f"{greetings[lang]} {name}"
    print(msg)

parser = argparse.ArgumentParser(
    description="Provides a personal greeting"
)

parser.add_argument(     # sub-command or option for the command
    "-n",               # smaller format of the argument
    "--name",           # longer format of the argument
    dest = "nameArg",      # variable name in which it will stored
    metavar="name",     # metavar is the diaplay name
    required=True, 
    help="The name of the person to greet"      # help text for the argument -n/--name
)

parser.add_argument(
    "-l", 
    "--lang", 
    metavar="language",
    dest = "langArg",
    required=True, 
    choices = ["English", "Spanish", "Hindi"],   
    help="The language to greet"
)

args = parser.parse_args()      

# message = f"Hello {args.nameArg}! "    # Here nameArg is defined in dest

#print(message)  # from here we define how we want to proceed further and handle the arguments passed. In this case
                # we just want to print a message.

hello(args.nameArg, args.langArg)