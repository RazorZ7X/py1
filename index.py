def calculadora():
    """
    Calculadora que permite realizar operaciones básicas
    y se mantiene en bucle hasta que el usuario escriba 'salir'
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


