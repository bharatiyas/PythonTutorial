# Capitalize the class name

class Vehicle:

    def __init__(self, make, model):        # __init__ = consturctor
        self.make = make
        self.model = model

    def moves(self):    # self = this in java
        print('Moves along.....')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Hyundai', 'Palisade')  # create my_car object

# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Honda', 'CR-V')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    
    def __init__(self, make, model, faa_id):    # Airplane constructor
        super().__init__(make, model)       # calling super constructor
        self.faa_id = faa_id

    def moves(self):        # Override the moves method
        print('Flies along....')



class Truck(Vehicle):
    def moves(self):
        print('Carries along....')


class Golf(Vehicle):
    pass        # Inherit everything as is. We do not override anything

cessna = Airplane('Cessna', 'Skyhawk', 'VHF-091')
cessna.get_make_model()
cessna.moves()

hilux = Truck('Toyota', 'Hilux')
hilux.get_make_model()
hilux.moves()

gcwagon = Golf('Yamaha', 'GC100')
gcwagon.get_make_model()
gcwagon.moves()

print('----------------------------------------------- \n\n')
for v in (my_car, your_car, cessna, hilux, gcwagon):
    v.get_make_model()      # Using Polymorphism
    v.moves()