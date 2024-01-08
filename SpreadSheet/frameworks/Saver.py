

class Saver():

    def __init__(self) -> None:
        pass

    def saveSpreadSheet(self,spreadsheet, path):
        # Nombre que le ponemos al archivo de texto que queremos guardar
        archivo_txt = path
        # Obtener una lista de la primera coordenada (las letras) del diciionario únicas y ordenadas
        cells = spreadsheet.cells
        unique_coordinates = sorted(set(coord[0] for coord in cells.keys()))
        
        lista_completa = [chr(letra) for letra in range(ord(unique_coordinates[0][0]), ord(unique_coordinates[-1][0]) + 1)]

        numbers = sorted(set(int(key[1:]) for key in cells.keys()))
        max_row = max(numbers)
        row = []
        matrix = []
        for i in range(1, max_row+1):
            for col in lista_completa:
                try:
                    touple = col + str(i)
                    val = cells[touple].content.getValue()
                except:
                    val = ";"
                row.append(val)
                print(val)
            matrix.append(row)
            row = []
        
    
        with open(archivo_txt, 'w', newline='') as file:
            # Crear un escritor CSV

            # Escribir valores
            for row in range(len(matrix)):
                for col in matrix[row]:
                  file.write(col)  
                
                file.write("\n")
                
                
            # for row_num in range(1, max(int(coord[1:]) for coord in cells.keys()) + 1):
            #     row_values = []
            #     for col in unique_coordinates:
            #         coordenada = f"{col}{row_num}"
            #         value = cells[coordenada].content.getValue()
                   
            #         row_values.append(value)
            #     csv_writer.writerow(row_values)


        print(f'Se ha guardado el diccionario en el archivo : {archivo_txt}')
