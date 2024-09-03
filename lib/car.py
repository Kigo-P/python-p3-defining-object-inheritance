from vehicle import Vehicle# have to import first

class Car(Vehicle):# subclass- inherits from the superclass/parent
    # overwriting the go function from the superclass/parent
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass

# toyota = Car(14, 4)
# print(toyota.wheel_size) # The Car has access to the parent/super class
# print(toyota.wheel_number)
# # The go method will overwrite the one from the superclass
# print(toyota.go())# VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!! instead of  "vrrrrrrrooom!"