"""
Calculadora Interactiva en Python

Este módulo proporciona una calculadora interactiva que permite realizar operaciones
matemáticas básicas en un bucle continuo hasta que el usuario decida salir.

Operaciones disponibles:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Potencia (**)

Autor: Desarrollador Python RazorZ7X
Versión: 1.0
"""

def calculadora():
    """
    Calculadora interactiva que permite realizar operaciones matemáticas básicas.
    
    Esta función implementa un bucle infinito que:
    1. Solicita al usuario la operación a realizar
    2. Valida que la operación sea válida
    3. Solicita dos números para la operación
    4. Ejecuta la operación y muestra el resultado
    5. Continúa hasta que el usuario escriba 'salir'
    
    Operaciones soportadas:
        + : Suma de dos números
        - : Resta de dos números
        * : Multiplicación de dos números
        / : División de dos números (con validación de división por cero)
        ** : Potencia (primer número elevado al segundo)
    
    Manejo de errores:
        - Valida que la operación sea válida
        - Previene división por cero
        - Maneja entradas no numéricas
        - Captura errores inesperados
    
    Ejemplo de uso:
        >>> calculadora()
        === CALCULADORA PYTHON ===
        Operaciones disponibles: +, -, *, /, ** (potencia)
        Escribe 'salir' como operación para terminar
        ----------------------------------------
        
        ¿Qué operación quieres realizar? (+, -, *, /, **, salir): +
        Ingresa el primer número: 10
        Ingresa el segundo número: 5
        
        📊 RESULTADO: 10.0 + 5.0 = 15.0
    """
    print("=== CALCULADORA PYTHON ===")
    print("Operaciones disponibles: +, -, *, /, ** (potencia)")
    print("Escribe 'salir' como operación para terminar")
    print("-" * 40)
    
    while True:
        try:
            # Preguntar la operación
            operacion = input("\n¿Qué operación quieres realizar? (+, -, *, /, **, salir): ").strip().lower()
            
            # Verificar si el usuario quiere salir
            if operacion == "salir":
                print("\n¡Gracias por usar la calculadora! ¡Hasta luego!")
                break
            
            # Verificar que la operación sea válida
            if operacion not in ['+', '-', '*', '/', '**']:
                print("❌ Operación no válida. Usa: +, -, *, /, **")
                continue
            
            # Preguntar los números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Realizar la operación
            resultado = None
            
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    print("❌ Error: No se puede dividir por cero")
                    continue
                resultado = num1 / num2
            elif operacion == '**':
                resultado = num1 ** num2
            
            # Mostrar el resultado
            print(f"\n📊 RESULTADO: {num1} {operacion} {num2} = {resultado}")
            
        except ValueError:
            print("❌ Error: Por favor ingresa números válidos")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        print("-" * 40)

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()


