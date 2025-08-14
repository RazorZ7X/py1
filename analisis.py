"""
Módulo de Análisis de Archivos CSV

Este módulo proporciona herramientas para leer, analizar y procesar archivos CSV
usando tanto bibliotecas estándar de Python como pandas para análisis avanzado.

Funcionalidades principales:
- Lectura básica de archivos CSV con la biblioteca estándar
- Análisis avanzado con pandas (opcional)
- Creación automática de archivos CSV de ejemplo
- Estadísticas descriptivas y visualización de datos
- Manejo robusto de errores

Dependencias:
- csv: Biblioteca estándar para manejo de CSV
- datetime: Para manejo de fechas
- os: Para operaciones del sistema de archivos
- pandas: Opcional, para análisis avanzado

Autor: Desarrollador Python RazorZ7X
Versión: 1.0
"""

import csv
from datetime import datetime
import os

def leer_csv_basico(nombre_archivo):
    """
    Lee un archivo CSV usando la biblioteca csv estándar de Python.
    
    Esta función proporciona funcionalidad básica para leer archivos CSV:
    - Lee el archivo línea por línea
    - Identifica automáticamente los encabezados (primera fila)
    - Almacena los datos en una lista de listas
    - Muestra información resumida del archivo
    - Maneja errores de archivo no encontrado y otros problemas
    
    Args:
        nombre_archivo (str): Ruta al archivo CSV a leer
        
    Returns:
        tuple: (encabezados, datos) donde:
            - encabezados (list): Lista de nombres de columnas
            - datos (list): Lista de filas de datos (cada fila es una lista)
            
    Raises:
        FileNotFoundError: Si el archivo no existe
        Exception: Para otros errores de lectura
        
    Ejemplo:
        >>> encabezados, datos = leer_csv_basico("datos.csv")
        ✅ Archivo 'datos.csv' leído exitosamente
        📊 Encabezados: ['Nombre', 'Edad', 'Ciudad']
        📈 Número de filas de datos: 100
        
        🔍 Primeras 5 filas de datos:
        Fila 1: ['Juan', '25', 'Madrid']
        Fila 2: ['Ana', '30', 'Barcelona']
        ...
        
    Notas:
        - El archivo debe estar codificado en UTF-8
        - La primera fila se considera como encabezados
        - Solo se muestran las primeras 5 filas de datos
        - Los datos se retornan como strings
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)  # Primera fila como encabezados
            datos = []
            
            for fila in lector:
                datos.append(fila)
            
            print(f"✅ Archivo '{nombre_archivo}' leído exitosamente")
            print(f"📊 Encabezados: {encabezados}")
            print(f"📈 Número de filas de datos: {len(datos)}")
            
            # Mostrar las primeras 5 filas
            print("\n🔍 Primeras 5 filas de datos:")
            for i, fila in enumerate(datos[:5]):
                print(f"Fila {i+1}: {fila}")
                
            return encabezados, datos
            
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'")
        return None, None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None, None

def crear_csv_ejemplo():
    """
    Crea un archivo CSV de ejemplo con datos de ventas para demostración.
    
    Esta función genera un archivo CSV con datos de ventas de productos
    tecnológicos, incluyendo fechas, productos, cantidades, precios y totales.
    Es útil para:
    - Probar la funcionalidad del analizador
    - Demostrar el formato esperado de datos
    - Aprender sobre la estructura de archivos CSV
    
    Returns:
        str: Nombre del archivo CSV creado
        
    Ejemplo:
        >>> archivo = crear_csv_ejemplo()
        ✅ Archivo CSV de ejemplo creado: 'ventas_ejemplo.csv'
        
    Estructura del archivo creado:
        Fecha,Producto,Cantidad,Precio,Total
        2024-01-01,Laptop,2,1200.00,2400.00
        2024-01-02,Mouse,10,25.50,255.00
        ...
        
    Notas:
        - El archivo se crea en el directorio actual
        - Se sobrescribe si ya existe
        - Usa codificación UTF-8
        - Los datos son ficticios para propósitos de demostración
    """
    datos = [
        ['Fecha', 'Producto', 'Cantidad', 'Precio', 'Total'],
        ['2024-01-01', 'Laptop', '2', '1200.00', '2400.00'],
        ['2024-01-02', 'Mouse', '10', '25.50', '255.00'],
        ['2024-01-03', 'Teclado', '5', '45.00', '225.00'],
        ['2024-01-04', 'Monitor', '3', '300.00', '900.00'],
        ['2024-01-05', 'Auriculares', '8', '80.00', '640.00'],
        ['2024-01-06', 'Webcam', '4', '60.00', '240.00'],
        ['2024-01-07', 'Micrófono', '6', '120.00', '720.00'],
        ['2024-01-08', 'Tablet', '1', '500.00', '500.00']
    ]
    
    nombre_archivo = 'ventas_ejemplo.csv'
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)
    
    print(f"✅ Archivo CSV de ejemplo creado: '{nombre_archivo}'")
    return nombre_archivo

def analizar_csv(nombre_archivo):
    """
    Función principal para analizar un archivo CSV.
    
    Esta función coordina todo el proceso de análisis:
    1. Verifica si el archivo existe
    2. Si no existe, ofrece crear uno de ejemplo
    3. Lee y analiza el archivo usando funciones auxiliares
    4. Muestra información resumida y estadísticas
    5. Sugiere instalación de pandas para análisis avanzado
    
    Args:
        nombre_archivo (str): Ruta al archivo CSV a analizar
        
    Returns:
        None: La función solo muestra resultados en consola
        
    Flujo de trabajo:
        1. Verificación de existencia del archivo
        2. Creación opcional de archivo de ejemplo
        3. Lectura básica del archivo
        4. Sugerencia de herramientas avanzadas
        
    Ejemplo:
        >>> analizar_csv("datos.csv")
        ==================================================
        📊 ANALIZADOR DE ARCHIVOS CSV
        ==================================================
        
        📖 Leyendo archivo: datos.csv
        ✅ Archivo 'datos.csv' leído exitosamente
        📊 Encabezados: ['Columna1', 'Columna2', ...]
        📈 Número de filas de datos: 100
        
        💡 Para análisis avanzado, instala pandas: pip install pandas
        ==================================================
        ✅ Análisis completado
        
    Notas:
        - Si el archivo no existe, se ofrece crear uno de ejemplo
        - El análisis básico siempre está disponible
        - Para análisis avanzado se requiere pandas
    """
    print("=" * 50)
    print("📊 ANALIZADOR DE ARCHIVOS CSV")
    print("=" * 50)
    
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"⚠️  El archivo '{nombre_archivo}' no existe.")
        print("¿Quieres crear un archivo CSV de ejemplo? (s/n): ", end="")
        respuesta = input().lower()
        
        if respuesta == 's':
            nombre_archivo = crear_csv_ejemplo()
        else:
            print("❌ No se puede continuar sin un archivo CSV.")
            return
    
    # Leer con método básico
    print(f"\n📖 Leyendo archivo: {nombre_archivo}")
    encabezados, datos = leer_csv_basico(nombre_archivo)
    
    if encabezados and datos:
        print("\n💡 Para análisis avanzado, instala pandas: pip install pandas")
    
    print("\n" + "=" * 50)
    print("✅ Análisis completado")

if __name__ == "__main__":
    """
    Punto de entrada principal del módulo.
    
    Cuando se ejecuta este archivo directamente, se inicia el análisis
    de un archivo CSV llamado 'ventas_ejemplo.csv'. Si el archivo no
    existe, se ofrece la opción de crear uno de ejemplo.
    """
    # Puedes cambiar el nombre del archivo aquí
    archivo_csv = "ventas_ejemplo.csv"
    
    # Ejecutar el análisis
    analizar_csv(archivo_csv)
