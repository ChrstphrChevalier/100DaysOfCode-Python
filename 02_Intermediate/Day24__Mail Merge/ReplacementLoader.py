import os

class ReplacementLoader:
    def __init__(self, path):
        self.replacement = []
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file '{path}' does not exist")
        
        if os.path.getsize(path) == 0:
            raise ValueError(f"The file '{path}' is empty")

        with open(path, 'r') as f:
            for line in f:
                self.replacement.append(line.strip())
    
    def getReplacement(self):
        return self.replacement