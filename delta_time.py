import time

class DeltaTime:
    def __init__(self): 
        self.now = self.previous = time.time()
        self.delta = 0

    def update(self):
        self.now = time.time()
        
        # actual time minus previous time gives the time variation
        self.delta = self.now - self.previous
         
        self.previous = self.now

    def get(self):
        return self.delta