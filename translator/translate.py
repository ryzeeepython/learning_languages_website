
from googletrans import Translator



class Translate:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, dest):
        result = self.translator.translate(text, dest = dest)
        return result
    
