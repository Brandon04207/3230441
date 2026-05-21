import tkinter as tk
import math

# Configuración
BG_COLOR = "#e0f7fa"
TEXT_COLOR = "#00695c"
FONT = ("Comic Sans MS", 16, "bold")
MENSAJE = "🌼 ¡Hola! Que tengas un día tan hermoso como esta flor 🌸"

# Crear ventana
ventana = tk.Tk()
ventana.title("🌼 Buen Día 🌼")
ventana.configure(bg=BG_COLOR)
ventana.geometry("600x600")

# Canvas para dibujar
canvas = tk.Canvas(ventana, width=500, height=400, bg=BG_COLOR, highlightthickness=0)
canvas.pack(pady=10)

# Variables para la animación
parte_actual = 0
animacion_en_curso = True

# Función para dibujar un pétalo
def dibujar_petalo(numero_petalo):
    centro_x, centro_y = 250, 200
    radio = 60
    
    # Calcular posición del pétalo
    angulo = (2 * math.pi / 8) * numero_petalo
    x = centro_x + math.cos(angulo) * 80
    y = centro_y + math.sin(angulo) * 80
    
    # Dibujar pétalo
    canvas.create_oval(
        x - radio, y - radio,
        x + radio, y + radio,
        fill="#ff80ab", outline="#d81b60", width=2
    )

# Función para dibujar el centro
def dibujar_centro():
    centro_x, centro_y = 250, 200
    canvas.create_oval(
        centro_x - 40, centro_y - 40,
        centro_x + 40, centro_y + 40,
        fill="#ffeb3b", outline="#fbc02d", width=2
    )

# Función para dibujar tallo y hojas
def dibujar_tallo_hojas():
    centro_x, centro_y = 250, 200
    
    # Tallo
    canvas.create_line(centro_x, centro_y + 40, centro_x, 400, fill="#388e3c", width=8)
    
    # Hojas
    canvas.create_oval(centro_x - 80, 300, centro_x - 20, 360, fill="#66bb6a", outline="#388e3c")
    canvas.create_oval(centro_x + 20, 300, centro_x + 80, 360, fill="#66bb6a", outline="#388e3c")

# Función para reiniciar la animación
def reiniciar_animacion():
    global parte_actual, animacion_en_curso
    
    # Detener cualquier animación en curso
    animacion_en_curso = False
    
    # Limpiar el canvas
    canvas.delete("all")
    
    # Restablecer variables
    parte_actual = 0
    animacion_en_curso = True
    
    # Limpiar el texto
    label_mensaje.config(text="")
    
    # Esperar un momento y comenzar de nuevo
    ventana.after(300, comenzar_animacion)

# Función para iniciar la animación
def comenzar_animacion():
    global animacion_en_curso
    animacion_en_curso = True
    animar_flor()

# Animación paso a paso
def animar_flor():
    global parte_actual
    
    # Verificar si la animación está activa
    if not animacion_en_curso:
        return
    
    if parte_actual == 0:
        # Primer paso: tallo y hojas
        dibujar_tallo_hojas()
        
    elif parte_actual <= 8:
        # Siguientes 8 pasos: pétalos uno por uno
        dibujar_petalo(parte_actual - 1)
        
    elif parte_actual == 9:
        # Último paso: centro de la flor
        dibujar_centro()
        # Iniciar animación del texto después de un momento
        ventana.after(500, animar_texto, 0)
        return
    
    parte_actual += 1
    
    # Solo continuar si la animación sigue activa
    if animacion_en_curso and parte_actual <= 9:
        ventana.after(200, animar_flor)

# Animación del texto
def animar_texto(indice=0):
    if indice <= len(MENSAJE) and animacion_en_curso:
        label_mensaje.config(text=MENSAJE[:indice])
        
        # Solo continuar si la animación sigue activa
        if animacion_en_curso:
            ventana.after(50, animar_texto, indice + 1)

# Etiqueta para el mensaje
label_mensaje = tk.Label(
    ventana, text="", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR,
    justify="center", wraplength=550
)
label_mensaje.pack(pady=20)

# Botón para reiniciar
boton = tk.Button(ventana, text=" otra vez :D ", font=("Comic Sans MS", 16, "bold"), 
                 bg="#73e3f2", fg="#00695c", width=11,
                 command=reiniciar_animacion)
boton.pack()

# Iniciar animación después de 1 segundo
ventana.after(1000, comenzar_animacion)

# Ejecutar
ventana.mainloop()