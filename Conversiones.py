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