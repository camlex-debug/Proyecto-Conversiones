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
            resultante = valor * 0.453592
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
            resultante = valor / 24
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
        tk.Button(ventana, text="Metros a kilómetros", command=lambda: conversion_de_longitud('m_km', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Pulgadas a metros", command=lambda: conversion_de_longitud('in_m', entrada, resultado)).pack(pady=2)
    elif tipo == 'Masa':
        tk.Button(ventana, text="Kg a gramos", command=lambda: conversion_de_masa('kg_g', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Libras a kg", command=lambda: conversion_de_masa('lb_kg', entrada, resultado)).pack(pady=2)
    elif tipo == 'Tiempo':
        tk.Button(ventana, text="Segundos a minutos", command=lambda: conversion_de_tiempo('s_min', entrada, resultado)).pack(pady=2)
        tk.Button(ventana, text="Horas a días", command=lambda: conversion_de_tiempo('h_d', entrada, resultado)).pack(pady=2)

root = tk.Tk()
root.title("Mi conversor de unidades")
root.geometry("300x300")
root.configure(bg="Pink")

label_titulo = tk.Label(root, text="Escoge la opción que desees", bg="HotPink", font=("Verdana", 14))
label_titulo.pack(pady=15)

btn_longitud = tk.Button(root, text="Longitud", bg="LightYellow", font=("Verdana", 12), command=lambda: ventana_conversion('Longitud'))
btn_longitud.pack(pady=5)

btn_masa = tk.Button(root, text="Masa", bg="LightYellow", font=("Verdana", 12), command=lambda: ventana_conversion('Masa'))
btn_masa.pack(pady=5)

btn_tiempo = tk.Button(root, text="Tiempo", bg="LightYellow", font=("Verdana", 12), command=lambda: ventana_conversion('Tiempo'))
btn_tiempo.pack(pady=5)

root.mainloop()
