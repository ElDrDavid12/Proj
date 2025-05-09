#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:30:34 2024

@author: david
"""

# Definición de la clase Libro
class Book:
    def __init__(self, title, author):
        self.title = title  # Título del libro
        self.author = author  # Autor del libro
        self.available = True  # Estado de disponibilidad del libro
    
    # Método para prestar el libro
    def borrow(self):
        if self.available:
            self.available = False  # Marca el libro como no disponible
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")
    
    # Método para devolver el libro
    def return_book(self):
        self.available = True  # Marca el libro como disponible
        print(f"El libro {self.title} ha sido devuelto")
        
# Definición de la clase Usuario
class User:
    def __init__(self, name, user_id):
        self.name = name  # Nombre del usuario
        self.user_id = user_id  # ID del usuario
        self.borrowed_books = []  # Lista de libros prestados
        
    # Método para que el usuario pida un libro en préstamo
    def borrow_book(self, book):
        if book.available:
            book.borrow()  # Llama al método borrow de la clase Book
            self.borrowed_books.append(book)  # Añade el libro a la lista de libros prestados
        else:
            print(f"El libro {book.title} no está disponible")
        
    # Método para que el usuario devuelva un libro
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()  # Llama al método return_book de la clase Book
            self.borrowed_books.remove(book)  # Elimina el libro de la lista de libros prestados
        else:
            print(f"El libro {book.title} no está en la lista de prestados")
    
# Definición de la clase Biblioteca
class Library:
    def __init__(self):
        self.books = []  # Lista de libros en la biblioteca
        self.users = []  # Lista de usuarios registrados
    
    # Método para añadir un libro a la biblioteca
    def add_book(self, book):
        self.books.append(book)  # Añade el libro a la lista de libros
        print(f"El libro {book.title} ha sido agregado")
    
    # Método para registrar un nuevo usuario
    def register_user(self, user):
        self.users.append(user)  # Añade el usuario a la lista de usuarios
        print(f"El usuario {user.name} ha sido registrado")

    # Método para mostrar los libros disponibles en la biblioteca
    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

# Crear instancias de libros
book1 = Book("La Sombra", "John Katzenbach")
book2 = Book("La Cólera", "Denis Marquet")
book3 = Book("El Psicoanalista", "John Katzenbach")
book4 = Book("La Historia del Loco", "John Katzenbach")

# Crear instancias de usuarios
user1 = User("Darla", "358")
user2 = User("Augusto", "912")
user3 = User("Victor D.", "187")
user4 = User("Victoria", "605")
user5 = User("Fransys", "239")
user6 = User("Victor", "741")
user7 = User("Banana", "583")

# Crear una instancia de la biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print("=" * 10)

# Registrar usuarios en la biblioteca
library.register_user(user1)
library.register_user(user2)
library.register_user(user3)
library.register_user(user4)
library.register_user(user5)
library.register_user(user6)
library.register_user(user7)

print("=" * 10)

# Interacción con el usuario para gestionar préstamos y devoluciones
while True:
    print("=" * 10)
    library.show_available_books()  # Muestra los libros disponibles
    print("=" * 10)
    usuario = input("¿Cuál es tu usuario? ").lower()
    
    # Verifica el usuario y da la bienvenida
    if usuario == "augusto":
        print("Bienvenido Augusto")
    elif usuario == "darla":
        print("Bienvenida Darla")
    elif usuario == "victor d.":
        print("Bienvenido Victor D.")
    elif usuario == "victoria":
        print("Bienvenida Victoria")
    elif usuario == "fransys":
        print("Bienvenida Fransys")
    elif usuario == "victor":
        print("Bienvenido Victor")
    else:
        print("Lo siento, no te reconozco")
    
    # Solicita la acción que desea realizar el usuario
    metodo = input("¿Qué quieres hacer? [Pedir préstamo/Regresar libro]: ").lower()
    
    if metodo == "pedir préstamo":
        libro = input("¿Qué libro deseas? ").title()
        # Llama al método de préstamo según el usuario y el libro seleccionado
        if usuario == "augusto":
            if libro == "La Sombra":
                user2.borrow_book(book1)
            elif libro == "La Cólera":
                user2.borrow_book(book2)
            elif libro == "El Psicoanalista":
                user2.borrow_book(book3)
            elif libro == "La Historia del Loco":
                user2.borrow_book(book4)
            else:
                print("Libro no disponible")
        elif usuario == "darla":
            if libro == "La Sombra":
                user1.borrow_book(book1)
            elif libro == "La Cólera":
                user1.borrow_book(book2)
            elif libro == "El Psicoanalista":
                user1.borrow_book(book3)
            elif libro == "La Historia del Loco":
                user1.borrow_book(book4)
            else:
                print("Libro no disponible")
        elif usuario == "victor d.":
            if libro == "La Sombra":
                user3.borrow_book(book1)
            elif libro == "La Cólera":
                user3.borrow_book(book2)
            elif libro == "El Psicoanalista":
                user3.borrow_book(book3)
            elif libro == "La Historia del Loco":
                user3.borrow_book(book4)
            else:
                print("Libro no disponible")
        elif usuario == "victoria":
            if libro == "La Sombra":
                user4.borrow_book(book1)
            elif libro == "La Cólera":
                user