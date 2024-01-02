# The TextualContent class is a subclass of the Content class that represents textual content and
# provides methods for getting numerical and textual values from the content.

from Content.entities.Content import Content
from Content.entities.TextualCellEception import TextualCellEception

class TextualContent(Content):
    
    def __init__(self, content):
        super().__init__("TextualContent")
        self.content = content
    
    def getNumericalValue(self):
        """
        The function "getNumericalValue" takes a string as input and returns its numerical value if it can
        be converted to a float, otherwise it raises an exception.
        
        :param content: The `content` parameter is a string that represents the content of a cell. It can
        be either a numerical value or a textual value
        :return: the numerical value of the content if it is a valid number, otherwise it raises a
        TextualCellException.
        """
        if self.content == "":
            return 0
        else:
            try:
                num_value = float(self.content)
                return num_value
            except:
                #return self.content
                raise TextualCellEception("THE SYSTEM TRIES TO GET A NUMBER FROM A NON NUMERICAL TEXTUAL CONTENT")
        
    
    def getTextualValue(self):
        return str(self.content)