import csv
from UI.UserInterface import UserInterface

class Loader():

    def __init__(self):
        self.UI = UserInterface()

    def loadSpreadSheet(self, path):
        cells = {}
          
        # Abrir el archivo y leer las líneas
        with open(path, 'r') as file:
            lines = file.readlines()

        # Procesar cada línea del archivo
        for row_idx, line in enumerate(lines):
            columns = line.strip().split(';')  # Dividir cada línea en columnas separadas por ';'
            for col_idx, value in enumerate(columns):
                if value != '':  # Verificar si el valor es distinto de ';'
                    # Obtener la coordenada correspondiente
                    letra = chr(65 + col_idx)  # Convertir el índice a letra (A, B, C, ...)
                    numero = row_idx + 1  # Sumar 1 para ajustar al número de fila
                    coordenada = f"{letra}{numero}"
                    cells[coordenada] = value
        return cells
            
    def loadCommands(self,name):
        with open(name, 'r') as archivo_csv:
            c = []
            #Lee el fichero linea por linea
            csv_reader = csv.reader(archivo_csv)
            for linea in csv_reader:
                #lineas_csv.append(linea)
                cc = self.UI.mainMenu(linea)
                c.append(cc)
            return c
        
    
    def file_loader(self,namefile, spreadsheet):
        loaded_dic = self.loadSpreadSheet(namefile)
        for clave, valor in loaded_dic.items():
            spreadsheet.insertContentInCell(clave,valor)

        return spreadsheet