import os

from EmailGenerator import EmailGenerator as EG

class EmailWriter:
    def __init__(self, path, EG):
        self.emails = EG.emailsGenerate()
        for name, content in self.emails.items():
            final_path = os.path.join(path, name)
            with open(final_path, 'w') as f:
                f.write(content)