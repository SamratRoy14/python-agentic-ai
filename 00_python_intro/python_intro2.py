class Tea:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
        print("Tea ready with sweetness = " + str(sweetness) + " and milk level = " + str(milk_level))
    
    def sip_tea(self):
        print("Sipping Tea")
        
    def add_sugar(self, amount):
        print("Added sugar of " + str(amount) + " spoon")

my_tea = Tea(2, 4)
my_tea.sip_tea()
my_tea.add_sugar(3)
        