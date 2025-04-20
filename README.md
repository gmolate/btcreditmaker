# Calculadora de Viabilidad: Crédito pa' Comprar Criptos 📊💸🇨🇱

¡Wena cabros! Este proyecto es una pequeña herramienta hecha en Python pa' ayudarte a **cachar** si te conviene o no endeudarte (onda, pedir un crédito o usar la tarjeta) pa' meterle unas **lucas** al trading de criptomonedas, como el Bitcoin.

La idea es simple: comparar **cuánto te saldría el chiste del crédito** (usando el famoso CAE) con **cuánto *podrías* ganar o perder** si el precio de la cripto se mueve. ¡Ojo! Esto es una simulación nomás, las criptos son más volátiles que el tolueno, así que no te confíes ciegamente.

## ¿Qué Hace Este Programa? 🤔

*   **Calcula el Costo del Crédito:** Toma el monto que quieres pedir y el **CAE (%)** que te cobra el banco o la institución financiera pa' darte una idea del costo total anual.
*   **Simula la Ganancia/Pérdida en Cripto:** Tú le dices qué porcentaje crees que va a subir (o bajar) el Bitcoin (o la cripto que sea) después de comprarla con la plata del crédito.
*   **Te Tira el Veredicto:** Compara el costo del crédito con tu posible ganancia o pérdida del trading y te dice si, en ese escenario específico, **saldrías pa' adelante (✅) o pa' atrás (❌)**.
*   **Dos Modos de Uso:**
    1.  **A la antigua (Consola):** Usando un script (`analisis_credito_cripto.py`) que lee los datos de los bancos (CAE, etc.) desde un archivo `.csv`. Ideal si quieres comparar varios bancos de una.
    2.  **Más Pituco (Interfaz Gráfica):** Usando un script (`INICIO.py` o el ejecutable `INICIO.exe`) que abre unas **ventanitas** donde metes todos los datos a mano (monto, precio BTC, dólar, CAE, y el % de ganancia/pérdida que quieres probar con una barra). ¡Más fácil y al toque!

## ¡Échale un Vistazo! (Interfaz Gráfica - `INICIO.py` o el ejecutable `INICIO.exe`) 🖼️

![Interfaz Gráfica](captura%20pantalla.png)


## Requisitos pa' que Corra Filete ✔️

*   **Python 3:** Ojalá una versión más o menos nueva (onda 3.7 pa' arriba).
*   **Tkinter:** Pa' la versión gráfica (`INICIO.py` o el ejecutable `INICIO.exe`). Casi siempre viene instalado con Python. Si por alguna razón rara no lo tienes, quizás tengas que instalarlo (busca cómo hacerlo pa' tu sistema operativo, ej. `sudo apt-get install python3-tk` en Linux tipo Debian/Ubuntu).
*   **(Opcional pero bacán):** Tener configurada la "localización" chilena (`es_CL`) en tu compu. Así los montos en pesos chilenos (CLP) se ven con el signo `$` y los puntos como separadores de miles, como debe ser. Si no la tienes, igual funca, pero se ve menos pro.

## ¿Cómo lo Echo a Andar? ▶️

Tienes dos formas, elige la que más te tinca:

### Opción 1: A la Antigua (Consola con `analisis_credito_cripto.py`)

1.  **Prepara tu archivo CSV:** Necesitas un archivo `.csv` (puedes usar o modificar el `ejemplo.csv` de ejemplo). Asegúrate que tenga estas columnas (puede ser con otros nombres, pero que estén): `nombre del banco`, `CAE`, `interes vigente`.
    *   **¡Importante!** El valor del CAE en el CSV debe estar en **formato decimal**. Por ejemplo, si el CAE es 37.29%, en el CSV pones `0.3729`. La tasa de interés vigente también.
2.  **Abre tu Terminal:** Anda a la carpeta donde guardaste los archivos del proyecto.
3.  **Ejecuta el Script:** Tipea esto y dale Enter:
    ```bash
    python analisis_credito_cripto.py
    ```
4.  **Ingresa los Datos:** El programa te pedirá la info en este formato:
    ```
    [ btc=PRECIO_EN_USD ; NOMBRE_TU_ARCHIVO.csv ; $=TIPO_CAMBIO_CLP ]
    ```
    *   **Ejemplo:**
        ```
        [ btc=68500.50 ; ejemplo.csv ; $=955.20 ]
        ```
5.  **Revisa los Resultados:** Te mostrará el análisis de viabilidad pa' cada banco que tengas en tu CSV, comparando el costo del crédito con escenarios de ganancia del 10%, 30% y 50%.

### Opción 2: La Más Pinta (Interfaz Gráfica con `INICIO.py` o el ejecutable `INICIO.exe` o el ejecutable `INICIO.exe` )

1.  **Abre tu Terminal:** De nuevo, anda a la carpeta donde guardaste los archivos.
2.  **Ejecuta el Script:** Tipea esto y dale Enter:
    ```bash
    python INICIO.py
    ```
3.  **¡Listo! Se abrirá la Ventana:**
    *   **Rellena los Campos:** Mete los datos que te pide: Monto del Crédito (por defecto parte en $1.000.000), Precio actual del Bitcoin en dólares, a cuántas lucas está el Dólar ($/USD), y el CAE (%) del crédito que te ofrecen. El "Interés Vigente" es más de referencia si ya pusiste el CAE.
    *   **Elige el Escenario:** Mueve la **barra deslizante** de abajo pa' escoger qué porcentaje de ganancia (¡o pérdida! desde -30%) quieres simular en tu jugada con las criptos. El número exacto se ve arriba de la barra.
    *   **¡Calcula!** Dale clic al botón verde **"Calcular Viabilidad"**.
    *   **Mira el Resultado:** En el cuadro grande de abajo te aparecerá el desglose: el costo del crédito, cuánto ganarías/perderías en el trading según el porcentaje que elegiste, y la conclusión final (si es negocio ✅ o no ❌).

## ¿Cómo Funca por Debajo? ⚙️ (La Lógica Simple)

1.  **Costo del Crédito:** Usa el CAE porque es la métrica que *debería* incluir todos los gastos del crédito en un año (intereses, seguros, impuestos, etc.). La fórmula es fácil: `Costo Anual = Monto del Crédito * CAE (en decimal)`.
2.  **Ganancia/Pérdida Trading:** Calcula la posible ganancia o pérdida basado en el porcentaje que tú elegiste simular: `Resultado Trading = Monto del Crédito * Porcentaje Elegido (en decimal)`.
3.  **La Resta Clave (Ganancia Neta):** `Ganancia NETA = Resultado Trading - Costo Anual del Crédito`.
4.  **El Veredicto:** Si la `Ganancia NETA` es mayor que cero, ¡pulento! (✅). Si es menor o igual a cero, ¡ucha, pa'l gato! (❌).

## Archivos del Proyecto 📁

*   `README.md`: Esta misma explicación ¡que estás leyendo ahora!
*   `analisis_credito_cripto.py`: El código pa' correr el análisis desde la consola (usa el CSV).
*   `INICIO.py` o el ejecutable `INICIO.exe`: El código que crea la interfaz gráfica bonita (mete los datos a mano).
*   `ejemplo.csv`: Un archivo CSV de **ejemplo** con datos (ficticios o desactualizados) de algunos bancos chilenos. **¡OJO! Si usas la versión de consola, actualiza este archivo con datos reales y vigentes.**

## ⚠️ ¡¡OJO PELAO!! - Advertencia Importante ⚠️

Este código es una herramienta educativa y de simulación. **NO ES ASESORAMIENTO FINANCIERO NI UNA RECOMENDACIÓN PARA INVERTIR O ENDEUDARSE.**

Invertir en criptomonedas es **ALTAMENTE RIESGOSO Y VOLÁTIL**. Usar plata prestada (crédito) para invertir **aumenta exponencialmente el riesgo**. Puedes perder mucho más que tu inversión inicial y quedar con una deuda gigante.

**Los cálculos aquí son estimaciones.** El CAE real puede variar, y el precio de las criptomonedas puede irse a las pailas (o al cielo) en cualquier momento.

**Antes de meterte en algo así:**
*   **Investiga un montón.**
*   **Entiende BIEN los riesgos.**
*   **NUNCA inviertas plata que no estás dispuesto a perder.**
*   **Considera hablar con un asesor financiero profesional.**

¡No te mandí ningún condoro financiero por culpa de un script! Usa esta herramienta con cabeza fría. 😉

---
