# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import csv

# Function to calculate viability
def calcular_viabilidad():
    try:
        monto_credito = float(entry_monto.get())
        precio_btc = float(entry_precio_btc.get())
        tipo_cambio = float(entry_tipo_cambio.get())
        cae = float(entry_cae.get()) / 100  # Convertir a decimal
        porcentaje_simulacion = float(scale_porcentaje.get()) / 100  # Convertir a decimal

        # Cálculo del costo del crédito
        costo_anual = monto_credito * cae

        # Cálculo de la ganancia/pérdida en trading
        resultado_trading = monto_credito * porcentaje_simulacion

        # Cálculo de la ganancia neta
        ganancia_neta = resultado_trading - costo_anual

        # Mostrar resultados
        if ganancia_neta > 0:
            resultado = "¡Pulento! (✅) Saldrías pa' adelante."
        else:
            resultado = "¡Ucha, pa'l gato! (❌) No es negocio."

        messagebox.showinfo("Resultados", f"Costo del Crédito: ${costo_anual:.2f}\n"
                                            f"Resultado Trading: ${resultado_trading:.2f}\n"
                                            f"Ganancia NETA: ${ganancia_neta:.2f}\n"
                                            f"{resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Viabilidad: Crédito pa' Comprar Criptos 📊💸🇨🇱")

# Crear y colocar los widgets
tk.Label(ventana, text="Monto del Crédito ($):").grid(row=0, column=0)
entry_monto = tk.Entry(ventana)
entry_monto.grid(row=0, column=1)

tk.Label(ventana, text="Precio actual del Bitcoin (USD):").grid(row=1, column=0)
entry_precio_btc = tk.Entry(ventana)
entry_precio_btc.grid(row=1, column=1)

tk.Label(ventana, text="Tipo de Cambio ($/USD):").grid(row=2, column=0)
entry_tipo_cambio = tk.Entry(ventana)
entry_tipo_cambio.grid(row=2, column=1)

tk.Label(ventana, text="CAE (%):").grid(row=3, column=0)
entry_cae = tk.Entry(ventana)
entry_cae.grid(row=3, column=1)

tk.Label(ventana, text="Porcentaje de Ganancia/Pérdida:").grid(row=4, column=0)
scale_porcentaje = tk.Scale(ventana, from_=-30, to=50, orient=tk.HORIZONTAL)
scale_porcentaje.grid(row=4, column=1)

# Botón para calcular viabilidad
btn_calcular = tk.Button(ventana, text="Calcular Viabilidad", command=calcular_viabilidad)
btn_calcular.grid(row=5, columnspan=2)

# Iniciar el bucle principal
ventana.mainloop()