def operation_crud():
    marked = ""
    while "q" != marked:
        print("Marque la tecla 'l' para listar los articulos")
        print("Marque la tecla 'v' para ver un articulo")
        print("Marque la tecla 'n' para crear nuevo articulo")
        print("Marque la tecla 'u' para actualizar un articulo")
        print("Marque la tecla 'd' para borrar un articulo articulo")
        print("Marque la tecla 'q' para salir")
        marked = input("Seleccione una opción:")
    
    return marked