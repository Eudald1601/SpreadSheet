import csv
from UI.UserInterface import UserInterface

class Loader():

    def __init__(self):
        self.UI = UserInterface()

    def loadSpreadSheet(self,name):
        cells = {}

        with open(name, 'r') as archivo_csv:
            #Lee el fichero linea por linea
            csv_reader = csv.reader(archivo_csv, delimiter=';')

            for fila, valores in enumerate(csv_reader, start=1):
                for i, valor in enumerate(valores, start=1):
                    columna = chr((i-1 % 26) + ord('A'))
                    clave = f'{columna}{fila}'
                    cells[clave] = valor
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
        