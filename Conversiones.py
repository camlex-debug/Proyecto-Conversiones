import tkinter as tk
from tkinter import messagebox

def conversion_de_longitud(opcion, entrada, resultado):
    try:
        valor = float(entrada.get())
        if opcion == 'm_km':
            resultante = valor / 1000
            resultado.config(text=f"{valor} metros = {resultante:.3f} kilómetros")
        elif opcion == 'in_m':
            resultante = valor * 0.0254
            resultado.config(text=f"{valor} pulgadas = {resultante:.3f} metros")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")

def conversion_de_masa(opcion, entrada, resultado):
    try:
        valor = float(entrada.get())
        if opcion == 'kg_g':
            resultante = valor * 1000
            resultado.config(text=f"{valor} kg = {resultante:.2f} gramos")
        elif opcion == 'lb_kg':
            res = valor * 0.453592
            resultado.config(text=f"{valor} lb = {resultante:.3f} kg")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")

def conversion_de_tiempo(opcion, entrada, resultado):
    try:
        valor = float(entrada.get())
        if opcion == 's_min':
            resultante = valor / 60
            resultado.config(text=f"{valor} segundos = {resultante:.2f} minutos")
        elif opcion == 'h_d':
            res = valor / 24
            resultado.config(text=f"{valor} horas = {resultante:.2f} días")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")

def ventana_conversion(tipo):
    ventana = tk.Toplevel()
    ventana.title(f"Conversión de {tipo}")

    entrada = tk.Entry(ventana, width=20)
    entrada.pack(pady=5)

    resultado = tk.Label(ventana, text="", fg="blue")
    resultado.pack(pady=5)

    if tipo == 'Longitud':
        tk.Button(ventana, text="Metros a Kilómetros", command=lambda: convertir_longitud('m_km', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Pulgadas a Metros", command=lambda: convertir_longitud('in_m', entrada, resultado)).pack(pady=2)
    elif tipo == 'Masa':
        tk.Button(ventana, text="Kg a Gramos", command=lambda: convertir_masa('kg_g', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Libras a Kg", command=lambda: convertir_masa('lb_kg', entrada, resultado)).pack(pady=2)
    elif tipo == 'Tiempo':
        tk.Button(ventana, text="Segundos a Minutos", command=lambda: convertir_tiempo('s_min', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Horas a Días", command=lambda: convertir_tiempo('h_d', entrada, resultado)).pack(pady=2)
