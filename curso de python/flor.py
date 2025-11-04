import tkinter as tk
import math

# Configuración general
BG_COLOR = "#e0f7fa"
TEXT_COLOR = "#00695c"
FONT = ("Comic Sans MS", 16, "bold")

# Mensaje para mostrar
mensaje = "🌼 ¡Hola! Que tengas un día tan hermoso como esta flor 🌸"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("🌼 Buen Día 🌼")
ventana.configure(bg=BG_COLOR)
ventana.geometry("600x600")

# Canvas para dibujar la flor
canvas = tk.Canvas(ventana, width=500, height=400, bg=BG_COLOR, highlightthickness=0)
canvas.pack(pady=10)

# Función para dibujar una flor con pétalos en forma circular
def dibujar_flor():
    center_x, center_y = 250, 200
    radio_petalo = 60
    petalos = 8

    # Dibujar pétalos
    for i in range(petalos):
        angle = (2 * math.pi / petalos) * i
        x = center_x + math.cos(angle) * 80
        y = center_y + math.sin(angle) * 80
        canvas.create_oval(
            x - radio_petalo,
            y - radio_petalo,
            x + radio_petalo,
            y + radio_petalo,
            fill="#ff80ab",
            outline="#d81b60"
        )

    # Centro de la flor
    canvas.create_oval(
        center_x - 40,
        center_y - 40,
        center_x + 40,
        center_y + 40,
        fill="#ffeb3b",
        outline="#fbc02d"
    )

    # Tallo
    canvas.create_line(center_x, center_y + 40, center_x, 400, fill="#388e3c", width=8)

    # Hojas
    canvas.create_oval(center_x - 80, 300, center_x - 20, 360, fill="#66bb6a", outline="#388e3c")
    canvas.create_oval(center_x + 20, 300, center_x + 80, 360, fill="#66bb6a", outline="#388e3c")

# Mostrar la flor
dibujar_flor()

# Etiqueta del mensaje
label_mensaje = tk.Label(ventana, text="", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, justify="center", wraplength=550)
label_mensaje.pack(pady=20)

# Animación de mensaje
def animar_mensaje(index=0):
    if index <= len(mensaje):
        label_mensaje.config(text=mensaje[:index])
        ventana.after(50, animar_mensaje, index + 1)

animar_mensaje()

# Ejecutar ventana
ventana.mainloop()