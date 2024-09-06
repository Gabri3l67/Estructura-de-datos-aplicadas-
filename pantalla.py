import tkinter as tk
from Rectangulo import Rectangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Triangulo import Triangulo 

# Funciones para calcular y mostrar resultados
def calcular():
    figura = figura_seleccionada.get()
    
    if figura == "Rectángulo":
        try:
            altura = float(entry1.get())
            base = float(entry2.get())
            rectangulo = Rectangulo(altura, base)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()
            resultado.set(f"Área: {round(area, 2)}, Perímetro: {round(perimetro, 2)}")
        except ValueError:
            resultado.set("Error: ingrese valores válidos")

    elif figura == "Círculo":
        try:
            radio = float(entry1.get())
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()
            resultado.set(f"Área: {round(area, 2)}, Perímetro: {round(perimetro, 2)}")
        except ValueError:
            resultado.set("Error: ingrese valores válidos")

    elif figura == "Cuadrado":
        try:
            lado = float(entry1.get())
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()
            resultado.set(f"Área: {round(area, 2)}, Perímetro: {round(perimetro, 2)}")
        except ValueError:
            resultado.set("Error: ingrese valores válidos")

    elif figura == "Triángulo":
        try:
            lado1 = float(entry1.get())
            lado2 = float(entry2.get())
            lado3 = float(entry3.get())
            triangulo = Triangulo(lado1, lado2, lado3)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            resultado.set(f"Área: {round(area, 2)}, Perímetro: {round(perimetro, 2)}")
        except ValueError:
            resultado.set("Error: ingrese valores válidos")
        except Exception as e:
            resultado.set(f"Error en cálculo: {str(e)}")

def actualizar_entradas():
    figura = figura_seleccionada.get()
    
    if figura == "Rectángulo":
        label1.config(text="Altura:")
        label2.config(text="Base:")
        entry2.pack(side=tk.LEFT, padx=5)
        label3.pack_forget()
        entry3.pack_forget()
        
    elif figura == "Círculo":
        label1.config(text="Radio:")
        label2.pack_forget()
        entry2.pack_forget()
        label3.pack_forget()
        entry3.pack_forget()

    elif figura == "Cuadrado":
        label1.config(text="Lado:")
        label2.pack_forget()
        entry2.pack_forget()
        label3.pack_forget()
        entry3.pack_forget()

    elif figura == "Triángulo":
        label1.config(text="Lado 1:")
        label2.config(text="Lado 2:")
        label3.pack(side=tk.LEFT)
        entry2.pack(side=tk.LEFT, padx=5)
        label3.config(text="Lado 3:")
        label3.pack(side=tk.LEFT)
        entry3.pack(side=tk.LEFT, padx=5)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")

# Selección de figura
figura_seleccionada = tk.StringVar()
figura_seleccionada.set("Rectángulo")

tk.Label(ventana, text="Seleccione una figura:").pack()

figuras = ["Rectángulo", "Círculo", "Cuadrado", "Triángulo"]
tk.OptionMenu(ventana, figura_seleccionada, *figuras, command=lambda _: actualizar_entradas()).pack()

# Entrada de datos
frame = tk.Frame(ventana)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Altura:")
label1.pack(side=tk.LEFT)

entry1 = tk.Entry(frame)
entry1.pack(side=tk.LEFT, padx=5)

label2 = tk.Label(frame, text="Base:")
label2.pack(side=tk.LEFT)

entry2 = tk.Entry(frame)
entry2.pack(side=tk.LEFT, padx=5)

label3 = tk.Label(frame, text="Lado 3:")
entry3 = tk.Entry(frame)

# Botón para calcular
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Etiqueta para mostrar resultados
resultado = tk.StringVar()
resultado.set("Área y perímetro aparecerán aquí")
resultado_label = tk.Label(ventana, textvariable=resultado)
resultado_label.pack(pady=10)

# Iniciar el loop de la ventana
ventana.mainloop()
