from TemplateLoader import TemplateLoader as T
from ReplacementLoader import ReplacementLoader as R


class EmailGenerator:
    def __init__(self, T, R):
        self.template = T.getTemplate()
        self.replacement = R.getReplacement()
        self.emailGenerator = {}

    def emailsGenerate(self):
        if "[name]" not in self.template:
            raise ValueError(f"Warning: '[name]' not found in template.")
        
        if not self.replacement:
            raise ValueError("No replacement names found in the provided file.")
        
        for replacement_word in self.replacement:
                value = self.template.replace("[name]", replacement_word)
                self.emailGenerator[replacement_word + '.txt'] = value

        return self.emailGenerator