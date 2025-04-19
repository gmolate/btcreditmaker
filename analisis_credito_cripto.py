# analisis_credito_cripto.py

import csv

def calcular_costo_credito(monto_credito, cae):
    return monto_credito * cae

def calcular_ganancia_potencial(monto_credito, porcentaje):
    return monto_credito * porcentaje

def analizar_credito(archivo_csv, precio_btc, tipo_cambio):
    resultados = []
    with open(archivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nombre_banco = row['nombre del banco']
            cae = float(row['CAE'])
            interes_vigente = float(row['interes vigente'])
            
            costo_credito = calcular_costo_credito(monto_credito, cae)
            ganancia_potencial = calcular_ganancia_potencial(monto_credito, porcentaje_simulado)
            ganancia_neta = ganancia_potencial - costo_credito
            
            resultado = {
                'Banco': nombre_banco,
                'Costo del Crédito': costo_credito,
                'Ganancia Potencial': ganancia_potencial,
                'Ganancia Neta': ganancia_neta,
                'Veredicto': '✅' if ganancia_neta > 0 else '❌'
            }
            resultados.append(resultado)
    return resultados

if __name__ == "__main__":
    monto_credito = float(input("Ingrese el monto del crédito: "))
    porcentaje_simulado = float(input("Ingrese el porcentaje de ganancia/pérdida esperado (en decimal): "))
    archivo_csv = input("Ingrese el nombre del archivo CSV: ")
    precio_btc = float(input("Ingrese el precio actual del Bitcoin en USD: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio CLP/USD: "))
    
    resultados = analizar_credito(archivo_csv, precio_btc, tipo_cambio)
    
    for resultado in resultados:
        print(f"Banco: {resultado['Banco']}, Costo del Crédito: {resultado['Costo del Crédito']}, "
              f"Gananacia Potencial: {resultado['Ganancia Potencial']}, "
              f"Gananacia Neta: {resultado['Ganancia Neta']}, Veredicto: {resultado['Veredicto']}")