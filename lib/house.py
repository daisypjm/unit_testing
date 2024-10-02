
class House:

    def __init__(self, number, door_colour):
        self.number = number
        self.door_colour = door_colour
        self.floors = 2
    
    def house_details(self):
        return(f"House number {self.number} has {self.floors} floors and a {self.door_colour} door")
    
    def repaint_door(self, new_colour):
        self.door_colour = new_colour
    
#my_house = House(4, "white")
#print(my_house.door_colour)
#print(my_house.repaint_door("red"))
#print(my_house.house_details())
