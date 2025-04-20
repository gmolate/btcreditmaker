import tkinter as tk
from tkinter import ttk  # Para usar el Scale (slider)
from tkinter import messagebox # Para mostrar errores
import locale
import platform # Para intentar configurar la localización

# --- Constantes ---
DEFAULT_MONTO_CREDITO_CLP = 1000000

# --- Configuración de Localización para Moneda Chilena ---
# Intenta configurar para español de Chile, si no, español de España o inglés US como fallback
locales_to_try = ['es_CL.UTF-8', 'es_CL', 'es_ES.UTF-8', 'es_ES', 'en_US.UTF-8', 'en_US']
if platform.system() == "Windows":
    locales_to_try = ['Chilean Spanish_Chile', 'Spanish_Chile', 'Spanish_Spain', 'English_United States'] # Nombres en Windows

locale_set = False
for loc in locales_to_try:
    try:
        locale.setlocale(locale.LC_ALL, loc)
        locale_set = True
        # print(f"Localización configurada a: {loc}") # Para depuración
        break
    except locale.Error:
        continue

if not locale_set:
    print("Advertencia: No se pudo configurar una localización regional adecuada para formatear moneda (CLP). Se usará formato numérico simple.")

def format_clp(amount):
    """Formatea un número como Peso Chileno (CLP)."""
    try:
        # Intenta usar el formato de moneda local si está configurado
        if locale_set and locale.getlocale(locale.LC_ALL)[0] is not None:
             # Asegura que no haya decimales para CLP, que es lo común
            return locale.currency(amount, symbol=' $', grouping=True, international=False).split(locale.localeconv()['decimal_point'])[0]
        else:
            # Fallback a formato simple si locale no se pudo configurar
            return f"${int(round(amount)):,} CLP".replace(",", ".")
    except Exception:
         # Fallback más robusto si todo falla
         return f"${int(round(amount)):,} CLP".replace(",", ".")


# --- Funciones de la Aplicación ---

def update_slider_label(value):
    """Actualiza la etiqueta que muestra el valor actual del slider."""
    try:
        # Intenta formatear con un decimal
        val_float = float(value)
        slider_value_label.config(text=f"{val_float:.1f}%")
    except ValueError:
        # Si hay error (poco probable con el slider), muestra el valor directo
        slider_value_label.config(text=f"{value}%")


def calcular_viabilidad_gui():
    """Obtiene los datos de la GUI, calcula la viabilidad y muestra los resultados."""
    try:
        # 1. Obtener valores de los campos de entrada
        monto_credito = float(monto_credito_var.get())
        btc_price_usd = float(btc_price_var.get())
        exchange_rate_usd_clp = float(exchange_rate_var.get())
        cae_percent = float(cae_percent_var.get())
        # interes_vigente_percent = float(interes_percent_var.get()) # Obtenido pero no usado activamente si usamos CAE
        profit_target_percent = float(profit_percent_var.get())

        # Validación básica de valores
        if not (monto_credito > 0 and btc_price_usd > 0 and exchange_rate_usd_clp > 0 and cae_percent >= 0):
             raise ValueError("Los valores de monto, precio BTC, tipo de cambio y CAE deben ser positivos.")

        # 2. Calcular Costo Total del Crédito Anual basado en CAE
        cae_decimal = cae_percent / 100.0
        costo_total_credito_clp = monto_credito * cae_decimal

        # 3. Calcular Ganancia Bruta del Trading para el escenario seleccionado
        profit_decimal = profit_target_percent / 100.0
        ganancia_bruta_trading_clp = monto_credito * profit_decimal

        # 4. Calcular Ganancia Neta
        ganancia_neta_clp = ganancia_bruta_trading_clp - costo_total_credito_clp

        # 5. Formatear resultados
        results_str = f"--- Análisis de Viabilidad ---\n\n"
        results_str += f"Monto del Crédito: {format_clp(monto_credito)}\n"
        results_str += f"Costo Anual Estimado del Crédito (CAE {cae_percent:.2f}%): {format_clp(costo_total_credito_clp)}\n"
        results_str += f"\n--- Escenario: Ganancia del {profit_target_percent:.1f}% en Bitcoin ---\n"
        results_str += f"Ganancia Bruta Estimada (Trading): {format_clp(ganancia_bruta_trading_clp)}\n"
        results_str += f"Ganancia NETA Estimada (Después Costo Crédito): {format_clp(ganancia_neta_clp)}\n\n"
        results_str += f"--- Evaluación ---\n"

        if ganancia_neta_clp > 0:
            results_str += "POSITIVA ✅ - La ganancia potencial del trading SUPERA el costo anual estimado del crédito."
        elif ganancia_neta_clp == 0:
             results_str += "NEUTRAL 😐 - La ganancia potencial del trading CUBRE EXACTAMENTE el costo anual estimado del crédito."
        else:
            results_str += "NEGATIVA ❌ - La ganancia potencial del trading NO CUBRE el costo anual estimado del crédito.\n"
            perdida_necesaria_compensar = abs(ganancia_neta_clp)
            results_str += f"(Se perderían {format_clp(perdida_necesaria_compensar)} en este escenario)."

        # 6. Mostrar resultados en el cuadro de texto
        results_text.config(state='normal') # Habilitar escritura
        results_text.delete('1.0', tk.END)   # Borrar contenido anterior
        results_text.insert(tk.END, results_str)
        results_text.config(state='disabled') # Deshabilitar escritura

    except ValueError as e:
        messagebox.showerror("Error de Entrada", f"Por favor, ingrese valores numéricos válidos.\nDetalle: {e}")
    except Exception as e:
         messagebox.showerror("Error Inesperado", f"Ocurrió un error durante el cálculo:\n{e}")


# --- Configuración de la Ventana Principal (GUI) ---
root = tk.Tk()
root.title("Analizador de Viabilidad Crédito-Cripto")
root.geometry("600x650") # Tamaño inicial de la ventana

# --- Variables de Tkinter ---
# Usar DoubleVar para permitir decimales
monto_credito_var = tk.StringVar(value=str(DEFAULT_MONTO_CREDITO_CLP)) # Empezar como string para mostrar bien el millón
btc_price_var = tk.DoubleVar(value=65000.0)
exchange_rate_var = tk.DoubleVar(value=950.0)
cae_percent_var = tk.DoubleVar(value=37.29)
interes_percent_var = tk.DoubleVar(value=2.61)
profit_percent_var = tk.DoubleVar(value=10.0) # Valor inicial del slider

# --- Creación de Widgets ---

# Frame para las entradas principales
input_frame = ttk.LabelFrame(root, text="Datos de Entrada", padding=(10, 10))
input_frame.pack(padx=10, pady=10, fill='x')

# Entradas de texto y etiquetas
ttk.Label(input_frame, text="Monto Crédito (CLP):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
monto_entry = ttk.Entry(input_frame, textvariable=monto_credito_var, width=15)
monto_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew') # sticky='ew' para que se expanda

ttk.Label(input_frame, text="Precio Bitcoin (USD):").grid(row=1, column=0, padx=5, pady=5, sticky='w')
btc_entry = ttk.Entry(input_frame, textvariable=btc_price_var, width=15)
btc_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

ttk.Label(input_frame, text="Tipo de Cambio (CLP/USD):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
exchange_entry = ttk.Entry(input_frame, textvariable=exchange_rate_var, width=15)
exchange_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

ttk.Label(input_frame, text="CAE (% Anual):").grid(row=3, column=0, padx=5, pady=5, sticky='w')
cae_entry = ttk.Entry(input_frame, textvariable=cae_percent_var, width=15)
cae_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
ttk.Label(input_frame, text="(Costo total usado para cálculo)").grid(row=3, column=2, padx=5, pady=5, sticky='w', columnspan=2)

ttk.Label(input_frame, text="Interés Vigente (% Mensual):").grid(row=4, column=0, padx=5, pady=5, sticky='w')
interes_entry = ttk.Entry(input_frame, textvariable=interes_percent_var, width=15)
interes_entry.grid(row=4, column=1, padx=5, pady=5, sticky='ew')
ttk.Label(input_frame, text="(Sólo informativo, no usado si se usa CAE)").grid(row=4, column=2, padx=5, pady=5, sticky='w', columnspan=2)


# Frame para el slider de porcentaje de ganancia
slider_frame = ttk.LabelFrame(root, text="Escenario de Ganancia/Pérdida (%) en Trading", padding=(10, 10))
slider_frame.pack(padx=10, pady=10, fill='x')

# Slider (Scale)
profit_slider = ttk.Scale(
    slider_frame,
    from_=-30.0,  # Desde -30%
    to=1000.0,  # Hasta 1000%
    orient='horizontal',
    variable=profit_percent_var,
    command=update_slider_label, # Llama a update_slider_label cada vez que cambia
    length=550 # Ancho del slider
)
profit_slider.pack(fill='x', padx=5, pady=5)

# Etiqueta para mostrar el valor del slider
slider_value_label = ttk.Label(slider_frame, text="10.0%", font=('Arial', 12))
slider_value_label.pack(pady=5)
update_slider_label(profit_percent_var.get()) # Actualizar valor inicial


# Botón Calcular
calculate_button = tk.Button(
    root,
    text="Calcular Viabilidad",
    command=calcular_viabilidad_gui, # Llama a la función de cálculo al hacer click
    bg="green",         # Color de fondo verde
    fg="white",         # Color de texto blanco
    font=('Arial', 12, 'bold'),
    width=20,
    pady=8
)
calculate_button.pack(pady=20)


# Cuadro de texto para resultados
results_frame = ttk.LabelFrame(root, text="Resultados", padding=(10, 10))
results_frame.pack(padx=10, pady=10, fill='both', expand=True)

results_text = tk.Text(
    results_frame,
    height=15, # Altura del cuadro de texto
    width=70,  # Ancho del cuadro de texto
    wrap='word', # Ajuste de línea automático
    state='disabled', # Empezar deshabilitado (no editable)
    font=('Consolas', 10) # Fuente monoespaciada para mejor alineación
)
results_text.pack(fill='both', expand=True)

# --- Iniciar el Bucle Principal de la GUI ---
root.mainloop()