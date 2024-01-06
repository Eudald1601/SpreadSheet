import csv


class Saver():

    def __init__(self) -> None:
        pass

    def saveSpreadSheet(self,name,cells):
        # Nombre que le ponemos al archivo de texto que queremos guardar
        archivo_txt = name

        # Obtener una lista de la primera coordenada (las letras) del diciionario únicas y ordenadas
        unique_coordinates = sorted(set(coord[0] for coord in cells.keys()))

        # Escribir el diccionario en el archivo CSV
        with open(archivo_txt, 'w', newline='') as csv_file:
            # Crear un escritor CSV
            csv_writer = csv.writer(csv_file, delimiter=';')

            # Escribir valores
            for row_num in range(1, max(int(coord[1:]) for coord in cells.keys()) + 1):
                row_values = []
                for col in unique_coordinates:
                    coordenada = f"{col}{row_num}"
                    if coordenada in cells and cells[coordenada].content.typeOfContent()!="FormulaContent":
                        value = cells[coordenada].content.getTextualValue()
                    elif coordenada in cells:
                        value=cells[coordenada].content.getNumericalValue() ##NOSE com fer perq mostri la formula y no el resultat
                    else:
                        value=""
                    row_values.append(value)
                csv_writer.writerow(row_values)

        print(f'Se ha guardado el diccionario en el archivo CSV: {archivo_txt}')