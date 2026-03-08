class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla porque titulo y autor no deben cambiar
        self.__datos = (titulo, autor)
        self.__categoria = categoria
        self.__isbn = isbn
        self.__prestado = False

    def get_titulo(self):
        return self.__datos[0]

    def get_autor(self):
        return self.__datos[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    def esta_prestado(self):
        return self.__prestado

    def prestar(self):
        self.__prestado = True

    def devolver(self):
        self.__prestado = False

    def __str__(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        return f"{self.get_titulo()} - {self.get_autor()} | {estado}"
