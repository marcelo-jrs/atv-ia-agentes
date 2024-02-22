import random

class Agent:
    def __init__(self, location_start, status_start, model_map):
        self.location = location_start
        self.status = status_start
        self.map = model_map
        
    def act(self):
        if self.location is None and self.status is None:
            self.move()
        location_status = self.map[self.location]
        if location_status == "Coin":
            self.collect()
        else:
            self.move()
            
    def collect(self):
        print("Coin Collected in Location {}".format(self.location))
        self.map[self.location] = "Empty"
        self.status = "Empty"
        
    def move(self):
        self.location =  random.choice(list(self.map))
        print("Agent is moving to {}".format(self.location))

# Test
agent = Agent("A", "Coin", {"A": "Coin", "B": "Empty", "C": "Coin", "D": "Coin", "E": "Empty"})
for _ in range(10):
    agent.act()
