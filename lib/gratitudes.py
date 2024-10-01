class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
    
#daisy = Gratitudes()
#daisy.add("my bag of Flaming Hot Cheetos")
#daisy.add("my gym session later to make up for Flaming Hot Cheetos")

#print(daisy.format())