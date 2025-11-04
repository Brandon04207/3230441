import tkinter as tk
from tkinter import messagebox
import pyodbc
from abc import ABC, abstractmethod

# ---------------------------
# CONEXIÓN A SQL SERVER
# ---------------------------
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'          # Cambia si tu servidor es distinto
    'DATABASE=biblioteca;'
    'Trusted_Connection=yes;'
)
cursor = conexion.cursor()

# ---------------------------
# BACKEND: USUARIOS, LIBROS, PRESTAMOS
# ---------------------------
class Usuario:
    def __init__(self, id, nombre, correo, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def iniciar_sesion(self, correo, contraseña):
        return self.correo == correo and self.contraseña == contraseña

class Libro:
    def __init__(self, id, titulo, autor, categoria, estado="Disponible"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.estado = estado
        self.observers = []

    def agregar_observer(self, observer):
        self.observers.append(observer)

    def notificar_observers(self, mensaje):
        for obs in self.observers:
            obs.update(mensaje)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        cursor.execute("UPDATE Libros SET estado=? WHERE id=?", (nuevo_estado, self.id))
        conexion.commit()
        if self.estado == "Disponible":
            self.notificar_observers(f"El libro '{self.titulo}' está disponible.")

class Prestamo:
    def __init__(self, usuario, libro, estado="Activo"):
        self.usuario = usuario
        self.libro = libro
        self.estado = estado

    def registrar_prestamo(self):
        if self.libro.estado == "Disponible":
            self.libro.cambiar_estado("Prestado")
            cursor.execute("INSERT INTO Prestamos (usuario_id, libro_id, estado) VALUES (?, ?, ?)",
                           (self.usuario.id, self.libro.id, "Activo"))
            conexion.commit()
            return f"{self.usuario.nombre} tomó '{self.libro.titulo}'."
        return f"El libro '{self.libro.titulo}' no está disponible."

    def registrar_devolucion(self):
        if self.estado == "Activo":
            self.libro.cambiar_estado("Disponible")
            cursor.execute("UPDATE Prestamos SET estado=? WHERE libro_id=? AND usuario_id=? AND estado='Activo'",
                           ("Devuelto", self.libro.id, self.usuario.id))
            conexion.commit()
            self.estado = "Devuelto"
            return f"'{self.libro.titulo}' devuelto por {self.usuario.nombre}."
        return "Este préstamo ya fue cerrado."

# ---------------------------
# OBSERVER
# ---------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, mensaje):
        pass

class UserNotifier(Observer):
    def __init__(self, usuario, app):
        self.usuario = usuario
        self.app = app

    def update(self, mensaje):
        self.app.mostrar_notificacion(f"[{self.usuario.nombre}] {mensaje}")

# ---------------------------
# STRATEGY: BÚSQUEDAS
# ---------------------------
class EstrategiaBusqueda(ABC):
    @abstractmethod
    def buscar(self, libros, criterio):
        pass

class BusquedaPorTitulo(EstrategiaBusqueda):
    def buscar(self, libros, criterio):
        return [libro for libro in libros if criterio.lower() in libro.titulo.lower()]

class BusquedaPorAutor(EstrategiaBusqueda):
    def buscar(self, libros, criterio):
        return [libro for libro in libros if criterio.lower() in libro.autor.lower()]

class BusquedaPorCategoria(EstrategiaBusqueda):
    def buscar(self, libros, criterio):
        return [libro for libro in libros if criterio.lower() in libro.categoria.lower()]

class Catalogo:
    def __init__(self, libros):
        self.libros = libros
        self.estrategia = None

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def buscar_libros(self, criterio):
        if not self.estrategia:
            return []
        return self.estrategia.buscar(self.libros, criterio)

# ---------------------------
# FRONTEND (Tkinter)
# ---------------------------
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Virtual")
        self.usuario_actual = None
        self.prestamos = []

        self.cargar_usuarios()
        self.cargar_libros()
        self.catalogo = Catalogo(self.libros)

        self.pantalla_login()

    # ---------------- Cargar datos desde SQL ----------------
    def cargar_usuarios(self):
        cursor.execute("SELECT id, nombre, correo, contraseña FROM Usuarios")
        self.usuarios = [Usuario(*fila) for fila in cursor.fetchall()]

    def cargar_libros(self):
        cursor.execute("SELECT id, titulo, autor, categoria, estado FROM Libros")
        self.libros = [Libro(*fila) for fila in cursor.fetchall()]

    def cargar_prestamos_usuario(self):
        self.prestamos = []
        cursor.execute("""
            SELECT p.id, l.id, l.titulo, l.autor, l.categoria, l.estado
            FROM Prestamos p
            JOIN Libros l ON p.libro_id = l.id
            WHERE p.usuario_id = ? AND p.estado = 'Activo'
        """, (self.usuario_actual.id,))
        for fila in cursor.fetchall():
            libro = Libro(fila[1], fila[2], fila[3], fila[4], fila[5])
            prestamo = Prestamo(self.usuario_actual, libro, "Activo")
            self.prestamos.append(prestamo)

    # ---------------- Login ----------------
    def pantalla_login(self):
        self.limpiar_pantalla()
        tk.Label(root, text="Bienvenido a la biblioteca Virtual",  font=("Arial", 20, "bold"), bg="#d0e7ff", fg="#003366").pack()

        tk.Label(self.root, text="Correo:", bg= "#e6f2ff",fg="#003366", font=("Arial Black",20,"bold")).pack(pady=20)
        self.entry_correo = tk.Entry(self.root, font=("Arial Black",16,"bold"))
        self.entry_correo.pack()

        tk.Label(self.root, text="Contraseña:", bg="#e6f2ff",fg="#003366", font=("Arial Black",20,"bold")).pack(pady=20)
        self.entry_clave = tk.Entry(self.root, show="*", font=("Arial Black",16,"bold"))
        self.entry_clave.pack()

        tk.Button(self.root, text="Iniciar Sesión",font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.iniciar_sesion).pack(pady=20)
        tk.Button(self.root, text="Registrarse", font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff",command=self.pantalla_registro).pack()

    def iniciar_sesion(self):
        correo = self.entry_correo.get()
        clave = self.entry_clave.get()
        for u in self.usuarios:
            if u.iniciar_sesion(correo, clave):
                self.usuario_actual = u
                self.cargar_prestamos_usuario()  #  Cargar préstamos desde SQL
                messagebox.showinfo("Bienvenido", f"Hola {u.nombre}")
                self.pantalla_catalogo()
                return
        messagebox.showerror("Error", "Credenciales incorrectas")

    # ---------------- Registro ----------------
    def pantalla_registro(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Nombre:",bg= "#e6f2ff",fg="#003366", font=("Arial Black",20,"bold")).pack(pady=20)
        self.entry_nombre = tk.Entry(self.root, font=("Arial Black",16,"bold"))
        self.entry_nombre.pack()

        tk.Label(self.root, text="Correo:",bg= "#e6f2ff",fg="#003366", font=("Arial Black",20,"bold")).pack(pady=20)
        self.entry_correo_reg = tk.Entry(self.root, font=("Arial Black",16,"bold"))
        self.entry_correo_reg.pack()

        tk.Label(self.root, text="Contraseña:",bg= "#e6f2ff",fg="#003366", font=("Arial Black",20,"bold")).pack(pady=20)
        self.entry_clave_reg = tk.Entry(self.root, show="*", font=("Arial Black",16,"bold"))
        self.entry_clave_reg.pack()

        tk.Button(self.root, text="Crear cuenta",font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff",command=self.registrar_usuario).pack(pady=20)
        tk.Button(self.root, text="Volver",font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.pantalla_login).pack()

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo_reg.get()
        clave = self.entry_clave_reg.get()

        cursor.execute("INSERT INTO Usuarios (nombre, correo, contraseña) VALUES (?, ?, ?)",
                       (nombre, correo, clave))
        conexion.commit()
        self.cargar_usuarios()
        messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        self.pantalla_login()

    # ---------------- Catálogo ----------------
    def pantalla_catalogo(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text=f"Bienvenido {self.usuario_actual.nombre}",  font=("Arial", 30, "bold"), bg="#d0e7ff", fg="#003366").pack()

        # Campo de búsqueda con Strategy
        opciones = ["Título", "Autor", "Categoría"]
        self.var_opcion = tk.StringVar(value="Título")
        menu = tk.OptionMenu(self.root, self.var_opcion, *opciones)
        menu.config(font=("Arial", 20, "bold"), bg="#d0e7ff", fg="#003366")
        menu["menu"].config(font=("Arial", 12), bg="#f0f8ff", fg="#000000")
        menu.pack()

        self.entry_busqueda = tk.Entry(self.root)
        self.entry_busqueda.pack()
        tk.Button(self.root, text="Buscar", font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.buscar_libros).pack()

        self.lista_libros = tk.Listbox(self.root, width=50)
        self.lista_libros.pack()
        self.actualizar_lista_libros()

        tk.Button(self.root, text="Prestar",font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.prestar_libro).pack()
        tk.Button(self.root, text="Devolver",font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff", command=self.devolver_libro).pack()
        tk.Button(self.root, text="Suscribirse", font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff",command=self.suscribirse_libro).pack()
        tk.Button(self.root, text="Agregar Libro", font=("Helvetica", 14, "bold"), bg="#0066cc", fg="#ffffff",command=self.agregar_libro).pack()

        tk.Label(self.root, text="Notificaciones:").pack()
        self.texto_notificaciones = tk.Text(self.root, height=5, width=50)
        self.texto_notificaciones.pack()

    def actualizar_lista_libros(self, lista=None):
        self.lista_libros.delete(0, tk.END)
        if lista is None:
            self.cargar_libros()
            lista = self.libros
        for l in lista:
            self.lista_libros.insert(tk.END, f"{l.titulo} - {l.estado}")

    def buscar_libros(self):
        criterio = self.entry_busqueda.get()
        opcion = self.var_opcion.get()
        if opcion == "Título":
            self.catalogo.set_estrategia(BusquedaPorTitulo())
        elif opcion == "Autor":
            self.catalogo.set_estrategia(BusquedaPorAutor())
        else:
            self.catalogo.set_estrategia(BusquedaPorCategoria())
        resultados = self.catalogo.buscar_libros(criterio)
        self.actualizar_lista_libros(resultados)

    # ---------------- Acciones ----------------
    def prestar_libro(self):
        idx = self.lista_libros.curselection()
        if not idx: return
        libro = self.libros[idx[0]]
        prestamo = Prestamo(self.usuario_actual, libro)
        msg = prestamo.registrar_prestamo()
        self.prestamos.append(prestamo)
        messagebox.showinfo("Préstamo", msg)
        self.actualizar_lista_libros()

    def devolver_libro(self):
        idx = self.lista_libros.curselection()
        if not idx: return
        libro = self.libros[idx[0]]
        for p in self.prestamos:
            if p.libro.id == libro.id and p.estado == "Activo":
                msg = p.registrar_devolucion()
                messagebox.showinfo("Devolución", msg)
                self.actualizar_lista_libros()
                self.cargar_prestamos_usuario()  # Refrescar préstamos desde SQL
                return
        messagebox.showwarning("Aviso", "No tienes este libro en préstamo.")

    def suscribirse_libro(self):
        idx = self.lista_libros.curselection()
        if not idx: return
        libro = self.libros[idx[0]]
        libro.agregar_observer(UserNotifier(self.usuario_actual, self))
        messagebox.showinfo("Suscripción", f"Te suscribiste a '{libro.titulo}'.")

    def agregar_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar libro")

        tk.Label(ventana, text="Título:").pack()
        self.entry_titulo = tk.Entry(ventana)
        self.entry_titulo.pack()

        tk.Label(ventana, text="Autor:").pack()
        self.entry_autor = tk.Entry(ventana)
        self.entry_autor.pack()

        tk.Label(ventana, text="Categoría:").pack()
        self.entry_categoria = tk.Entry(ventana)
        self.entry_categoria.pack()

        tk.Button(ventana, text="Guardar", command=lambda: self.registrar_libro(ventana)).pack()

    def registrar_libro(self, ventana):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        categoria = self.entry_categoria.get()

        cursor.execute("INSERT INTO Libros (titulo, autor, categoria, estado) VALUES (?, ?, ?, ?)",
                       (titulo, autor, categoria, "Disponible"))
        conexion.commit()

        self.actualizar_lista_libros()
        messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado.")
        ventana.destroy()

    # ---------------- Notificaciones ----------------
    def mostrar_notificacion(self, mensaje):
        self.texto_notificaciones.insert(tk.END, mensaje + "\n")

    # ---------------- Utilidad ----------------
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ---------------------------
# Ejecutar app
# ---------------------------
root = tk.Tk()
root.geometry("800x600")  
root.configure(bg="#e6f2ff")

app = BibliotecaApp(root)
root.mainloop()

