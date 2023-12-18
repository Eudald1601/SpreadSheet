class PrinterSpreadSheet():
    
    def __init__(self) -> None:
        pass

    def ordercells(self, cell_object):
        cell_id = cell_object.getCoordinate()
        return cell_id[1], ord(cell_id[0])

    # Ordenar las celdas utilizando la función definida anteriormente
    def printSpreadSheet(self, celdas, name):
        print("SPREADSHEET NAME: ", name)
        celdas_ordenadas = sorted([(cell.coordinate, cell.content.getTextualValue()) for cell in celdas], key=lambda x: (x[0], x[1]))
    # Obtener la lista de columnas distintas
        columnas = sorted(set(coord[0][0] for coord in celdas_ordenadas))
    # Imprimir encabezados de columnas
        print("        |", end="")
        for col in columnas:
            print(f"     {col}        |", end="")
        print("\n--------|", end="")
        for _ in range(len(columnas)):
            print("--------------|", end="")
        print()
        # Generar tabla con celdas vacías
        max_fila = max(coord[0][1] for coord in celdas_ordenadas)
        #print(celdas_ordenadas)
        for fila in range(1, int(max_fila) + 1):
            print(f"{fila:<8}|", end="")
            for col in columnas:
                coordenada = (col, str(fila))
                for iter in celdas_ordenadas:
                    if coordenada == iter[0]:
                        content = iter[1]
                        print(f"   {content}         |", end="")
                else:
                    print(f"              |", end="")
            print("\n--------|", end="")
            for _ in range(len(columnas)):
                print("--------------|", end="")
            print()