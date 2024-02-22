import random

class Agent:
    def __init__(self):
        self.location = None
        self.status = None
        self.model = {"A": "Coin", "B": "Coin", "C": "Coin"}
        self.visited = set()
        
    def act(self):
        if self.location is None and self.status is None:
            self.move()
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
        unvisited_locations = set(self.model.keys()) - self.visited
        if unvisited_locations:
            self.location = random.choice(list(unvisited_locations))
        else:
            print("All locations visited.")
            return
        self.visited.add(self.location)
        print("Agent is moving to {}".format(self.location))

# Test
agent = Agent()
for _ in range(10):
    agent.act()
