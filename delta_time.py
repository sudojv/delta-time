import time

class DeltaTime:
    def __init__(self): 
        self.now = time.time()
        self.previous = 0
        self.delta = self.now - self.previous

    def update(self):
        self.now = time.time()
        
        # actual time minus previous time gives the time variation
        self.delta = self.now - self.previous
         
        self.previous = self.now

    def get(self):
        return self.delta