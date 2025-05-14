import tkinter as tk
from tkinter import messagebox

def conversion_de longitud(opcion, entrada, resultado):
    try:
        valor = float(entrada.get())
        if opcion == 'm_km':
            res = valor / 1000
            resultado.config(text=f"{valor} metros = {res:.3f} kilómetros")
        elif opcion == 'in_m':
            res = valor * 0.0254
            resultado.config(text=f"{valor} pulgadas = {res:.3f} metros")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")