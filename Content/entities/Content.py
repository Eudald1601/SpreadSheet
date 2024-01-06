
#ESTA CLASE SIRVE PARA QUE LA CELDA PUEDA LLAMAR A CONTENIDO INDEPENDIENTEMENTE SI ES FORMULACONTENT, TEXTUALCONTENT O NUMERICALCONTENT
#TODOS LOS TIPOS DE CONTENTS IMPLEMENTARAN ESTOS METODOS. DESDE CELL LLAMAREMOS CONTENT.FUNCTION Y EL YA SABRA QUE OPERACIONES HACER


class Content():
    def __init__(self, type, stringvalue) -> None:
        super().__init__()
        self.type =type
        self.textulvalue = stringvalue

    def getNumericalValue(self):
        pass

    def getTextualValue(self):
        pass
    
    def getValue(self):
        return self.textulvalue
    
    def typeOfContent(self):
        return self.type