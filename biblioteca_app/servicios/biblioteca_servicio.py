from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set para controlar IDs únicos
        self.ids_usuarios = set()

    # ---------------- LIBROS ----------------

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro agregado")

    def eliminar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("Usuario ya registrado")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # ---------------- PRESTAMOS ----------------

    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no existe")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro.esta_prestado():
            print("El libro ya está prestado")
            return

        libro.prestar()
        usuario.agregar_libro(libro)

        print("Libro prestado correctamente")

    def devolver_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no existe")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        libro.devolver()
        usuario.devolver_libro(libro)

        print("Libro devuelto")

    # ---------------- BUSQUEDAS ----------------

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():

            if libro.get_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():

            if libro.get_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():

            if libro.get_categoria().lower() == categoria.lower():
                print(libro)

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.get_libros_prestados():
            print(libro)
