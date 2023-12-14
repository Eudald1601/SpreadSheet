from Content import Content

class NumericalContent(Content):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = self.getNumericalValue(content)

    def getNumericalValue(self, content):
        return float(content)
        

    def getTextualValue(self, content):
        return str(content)
        