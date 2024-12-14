class Smartphone:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
    def display_info(self):
        return f"Brand: {self.brand}, Color: {self.color}"
    
    def make_call(self):
        return f"Calling from {self.brand} {self.color} phone"


phone = Smartphone("Apple", "Black")

print(phone.display_info())

print(phone.make_call())


# adding inheritance and polymorphism
class Tecno(Smartphone):
    def __init__(self, brand, color): #constructor function for creating a new instance of the class object and assigning values to its attributes
        super().__init__(brand, color) # calling the parent class constructor
    
    def make_call(self):
        return f"Calling from {self.brand} {self.color} phone"
    
    def play_game(self):
        return f"Playing game on {self.brand} {self.color} phone"

phone2 = Tecno("Tecno", "Blue")

print(phone2.display_info())

print(phone2.make_call())

print(phone2.play_game())

phone2.color = "Red"

print(phone2.display_info())



        