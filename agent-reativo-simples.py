# Importing random module
import random

class Agent:
    def __init__(self):
        self.location = "A"
        self.status = "Coin"
        self.model = {"A": "Coin", "B": "Coin", "C": "Coin"}  # Add the model here
        
    def act(self):
        if self.status == "Coin":
            self.clean()
        else:
            self.move()
            
    def clean(self):
        print("Coin Collected!", self.location)
        self.status = "Empty"
        
    def move(self):
        self.location =  random.choice(list(self.model.keys()))
        print('Agent is moving to', self.location)

# Test the code
if __name__ == "__main__":
    agent = Agent()
    print("Initial Location:", agent.location)
    print("Initial Status:", agent.status)

    for i in range(10):
        print("Agent is performing an action:")
        agent.act() 
        print("New Location:", agent.location)
        print("New Status:", agent.status)
