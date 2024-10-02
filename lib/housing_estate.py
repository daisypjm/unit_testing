class HousingEstate:
    def __init__(self):
        self.houses = []

    def get_house_numbers(self):
        house_numbers = []
        for house in self.houses:
            house_numbers.append(house.number)
        return house_numbers
    

# return [house.number for house in self.houses] = quicker method