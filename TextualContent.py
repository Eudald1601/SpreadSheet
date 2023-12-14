from Content import Content
from exceptions.TextualCellEception import TextualCellEception
class TextualContent(Content):
    def __init__(self, content) -> None:
        self.content = self.getTextualValue(content)
        super().__init__()

    def getNumericalValue(self, content):
        if content == "":
            return 0
        else:
            try:
                num_value = float(content)
                return num_value
            except:
                raise TextualCellEception("THE SYSTEM TRIES TO GET A NUMBER FROM A NON NUMERICAL TEXTUAL CONTENT")
        
    
    def getTextualValue(self, content):
        return content