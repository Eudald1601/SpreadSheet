# The `NumericalContent` class is a subclass of `Content` that represents numerical content and
# provides methods to retrieve the numerical and textual values of the content.

from Content.entities.Content import Content

class NumericalContent(Content):
    def __init__(self, content) -> None:
        super().__init__("NumericalContent", content)
        self.content = content

    def getNumericalValue(self):
        return float(self.content)
        

    def getTextualValue(self):
        return str(self.content)
        