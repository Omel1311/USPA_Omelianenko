class Risk:
    def __init__(self, name, level, color, weight):
        self.name = name
        self.level = level
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.level} {self.color} {self.weight}"

    def get_risk_level(self):
        print(self.name)


war = Risk("War", 1, "red", 10)
print(war)

business = Risk("Business", 3, "blue", 20)
print(business)

tech = Risk("Tech", 3, "green", 30)
print("\n", tech)
