import csv
import pandas as pd
from datetime import datetime
import os

def leer_csv_basico(nombre_archivo):
    """
    Lee un archivo CSV usando la biblioteca csv estándar de Python
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

def leer_csv_pandas(nombre_archivo):
    """
    Lee un archivo CSV usando pandas para análisis más avanzado
    """
    try:
        df = pd.read_csv(nombre_archivo)
        print(f"\n🐼 Análisis con Pandas:")
        print(f"📊 Forma del DataFrame: {df.shape}")
        print(f"📋 Información del DataFrame:")
        print(df.info())
        print(f"\n📈 Primeras filas:")
        print(df.head())
        print(f"\n📊 Estadísticas descriptivas:")
        print(df.describe())
        
        return df
        
    except Exception as e:
        print(f"❌ Error al leer con pandas: {e}")
        return None

def crear_csv_ejemplo():
    """
    Crea un archivo CSV de ejemplo con datos de ventas
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
    Función principal para analizar un archivo CSV
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
        # Leer con pandas si está disponible
        try:
            df = leer_csv_pandas(nombre_archivo)
        except ImportError:
            print("⚠️  Pandas no está disponible. Instálalo con: pip install pandas")
    
    print("\n" + "=" * 50)
    print("✅ Análisis completado")

if __name__ == "__main__":
    # Puedes cambiar el nombre del archivo aquí
    archivo_csv = "ventas_ejemplo.csv"
    
    # Ejecutar el análisis
    analizar_csv(archivo_csv)
