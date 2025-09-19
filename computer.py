#This class is the framework for the computer object. 
#It gives the basic details of the computer object and a small method for prining a description of the computer
class Computer:
# lines 4-10 list all the attributes the computer class stores
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    computer_id: int
 # Here we create the constructor for the computer object attributes and methods
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int,
                    operating_system: str, year_made: int, price: int, computer_id: int): 
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.computer_id = computer_id
    def printComputer(self):
        print(self.description)
    

