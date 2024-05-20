class Vehicle: # parent or superclass
                    # instances of Vehicle initialize with a wheel size and number. v       v
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    #  instance method 
    def go(self):
        return "vrrrrrrrooom!"
    
    #  instance method 
    def fill_up_tank(self):
        return "filling up!"
