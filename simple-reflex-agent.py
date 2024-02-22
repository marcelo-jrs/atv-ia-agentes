import random

class Agent:
    def __init__(self):
        self.location = "A"
        self.status = "Coin"
        self.model = {"A": "Coin", "B": "Coin", "C": "Coin"}
        
    def act(self):
        location_status = self.model[self.location]
        if location_status == "Coin":
            self.collect()
        else:
            self.move()
            
    def collect(self):
        print("Coin Collected in Location {}".format(self.location))
        self.model[self.location] = "Empty"
        self.status = "Empty"
        
    def move(self):
        self.location =  random.choice(list(self.model))
        print("Agent is moving to {}".format(self.location))

# Test
agent = Agent()
for _ in range(10):
    agent.act()
