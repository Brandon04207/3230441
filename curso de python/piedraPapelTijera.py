import random as r 
import tkinter as tk 
from tkinter import messagebox

# Configuración general
BG_COLOR = "#f2f2f2"
TEXT_COLOR = "#000000"
FONT = ("Comic Sans MS", 16, "bold")

# puntaje de jugador y pc
puntaje_jugador = 0
puntaje_pc = 0

def jugar(opcion_usuario):
    global puntaje_jugador, puntaje_pc
    
    # Generar elección de la computadora
    numeroAleatorio = r.randint(1, 3)
    
    # Asignar nombres a las opciones
    opciones = {1: "piedra", 2: "papel", 3: "tijera"}
    opcion_pc = opciones[numeroAleatorio]
    
    # Determinar resultado
    if opcion_usuario == opcion_pc:
        resultado = "¡Empate!"
    elif (opcion_usuario == "piedra" and opcion_pc == "tijera") or \
         (opcion_usuario == "papel" and opcion_pc == "piedra") or \
         (opcion_usuario == "tijera" and opcion_pc == "papel"):
        resultado = "¡Ganaste!"
        puntaje_jugador += 1
    else:
        resultado = "Perdiste :("
        puntaje_pc += 1
    
    # Actualizar la etiqueta de puntaje
    actualizar_puntaje()
    
    # Ventana emergente más grande con letras más grandes
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("400x200")  # Más grande
    ventana_resultado.configure(bg=BG_COLOR)
    
    # Mensaje con resultado y puntaje actual
    mensaje = f"Tú: {opcion_usuario}\nPC: {opcion_pc}\n\n{resultado}\n\nPuntaje: {puntaje_jugador} - {puntaje_pc}"
    tk.Label(ventana_resultado, text=mensaje, 
             font=("Helvetica", 18, "bold"),  # Letras más grandes
             bg=BG_COLOR, fg=TEXT_COLOR,
             justify="center").pack(expand=True)

def actualizar_puntaje():
    """Actualiza la etiqueta de puntaje en la ventana principal"""
    texto_puntaje.config(text=f"Puntaje: Jugador {puntaje_jugador} - PC {puntaje_pc}")
    
def mostrar_resultado_final():
    """Muestra el resultado final cuando se cierra la ventana"""
    if puntaje_jugador > puntaje_pc:
        mensaje_final = f"¡FELICIDADES! Ganaste el juego\nPuntaje Final: {puntaje_jugador} - {puntaje_pc}"
    elif puntaje_jugador < puntaje_pc:
        mensaje_final = f"La computadora ganó el juego\nPuntaje Final: {puntaje_jugador} - {puntaje_pc}"
    else:
        mensaje_final = f"El juego terminó en empate\nPuntaje Final: {puntaje_jugador} - {puntaje_pc}"
    
    messagebox.showinfo("Resultado Final", mensaje_final)
    ventana.destroy()

def on_cerrar():
    """Función que se ejecuta al intentar cerrar la ventana"""
    mostrar_resultado_final()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.configure(bg=BG_COLOR)
ventana.geometry("800x450")

# Título
titulo = tk.Label(ventana, text="Elige tu opción:", 
    font=("Helvetica", 24, "bold"), 
    bg=BG_COLOR, fg=TEXT_COLOR)
titulo.pack(pady=20)

# Etiqueta de puntaje
texto_puntaje = tk.Label(ventana, 
    text=f"Puntaje: Jugador {puntaje_jugador} - PC {puntaje_pc}",
    font=("Helvetica", 20, "bold"), 
    bg=BG_COLOR, fg="#FF0000")  # Color rojo para destacar
texto_puntaje.pack(pady=10)

# Frame para botones
frame = tk.Frame(ventana)
frame.pack(pady=20)

# Botones
boton_piedra = tk.Button(frame, text="PIEDRA", font=("Helvetica", 30, "bold"), 
     bg="#333333", fg="#ffffff", width=8,
     command=lambda: jugar("piedra"))
boton_piedra.pack(side="left", padx=10)

boton_papel = tk.Button(frame, text="PAPEL", font=("Helvetica", 30, "bold"), 
    bg="#333333", fg="#ffffff", width=8,
    command=lambda: jugar("papel"))
boton_papel.pack(side="left", padx=10)

boton_tijera = tk.Button(frame, text="TIJERA", font=("Helvetica", 30, "bold"), 
    bg="#333333", fg="#ffffff", width=8,
    command=lambda: jugar("tijera"))
boton_tijera.pack(side="left", padx=10)

# Etiqueta para instrucciones
instrucciones = tk.Label(ventana, 
    text="Haz clic en cualquier opción para jugar contra la computadora",
    font=("Helvetica", 14), 
    bg=BG_COLOR, fg=TEXT_COLOR)
instrucciones.pack(pady=30)

# Botón para cerrar
boton_cerrar = tk.Button(ventana, text="Cerrar Juego", 
    font=("Helvetica", 16, "bold"), 
    bg="#000000", fg="#ffffff",
    command=on_cerrar)
boton_cerrar.pack(pady=20)


ventana.mainloop()

