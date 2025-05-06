import os

class TemplateLoader:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file '{path}' does not exist")
        
        if os.path.getsize(path) == 0:
            raise ValueError(f"The file '{path}' is empty")

        with open(path, 'r') as f:
            self.starting_letter = f.read()
    
    def getTemplate(self):
        return self.starting_letter
