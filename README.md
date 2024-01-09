Proyecto SpreadSheet - ARQSOFT Máster MATT UPC

Cómo lanzar el código:

Ejecutar python3 main.py en el terminal arranca el programa desde el fichero main.py.
    Al inicio, se muestran instrucciones con 4 opciones:
    E: Editar celda
    RF: Leer comandos de un fichero
    C: Crear SpreadSheet
    L: Cargar fichero S2V
    S: Guardar fichero S2V


Consideraciones:

    1.- Antes de editar una celda, es necesario crear un fichero.
    2.- La sintaxis debe ser válida, de lo contrario, se lanza una excepción.


Problemas identificados en el código:

    1.- La ausencia de valores en un rango al llamarlo puede generar una excepción. Al intentar introducir contenido en una celda que depende de otra inexistente, el código lanza una excepción durante el testing.

    2.- Error en /Content/usecases/Functions/adapters/ContentManager.py. Al introducir una función dentro de otra con un rango de celdas (e.g., PROMEDIO(A1:B2;SUMA(B1:B2;6))), el programa no interpreta correctamente los argumentos de la segunda función y no guarda el valor correcto. El test de fórmulas obtiene un 10 debido a la diferencia en el formato de las fórmulas de testing.

Importante:

    1.- Modificaciones durante el testeo:

        1.- En circular_dependencies_test.py, se agrega un condicional para calcular correctamente la nota si se lanza la excepción CircularDepencencyExeption.
        2.- En marker_save_test_ref.s2v, si se introduce un dato no válido relacionado con el primer problema identificado, se produce un bucle. Se realiza un ajuste para mostrar el error y  el cálculo esperado.
        
    2.- La ejecución del test podría no funcionar en sistemas operativos distintos a Linux. El problema podría estar relacionado con la ruta en los ficheros TestRunner.py o SettingEnvironment.py dentro de las carpetas mencionadas.