from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n--- BIBLIOTECA DIGITAL ---")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro por titulo")
        print("6. Listar libros de usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "3":

            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")

            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "4":

            isbn = input("ISBN del libro: ")
            id_usuario = input("ID del usuario: ")

            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "5":

            titulo = input("Título del libro: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "6":

            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_usuario(id_usuario)

        elif opcion == "7":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    menu()
