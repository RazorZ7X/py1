def fizzbuzz(n):
    """
    Implementación del clásico problema FizzBuzz
    Para números del 1 al n:
    - Si es múltiplo de 3: imprime "Fizz"
    - Si es múltiplo de 5: imprime "Buzz"  
    - Si es múltiplo de ambos: imprime "FizzBuzz"
    - En otro caso: imprime el número
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzbuzz_lista(n):
    """
    Versión que retorna una lista en lugar de imprimir
    """
    resultado = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado

if __name__ == "__main__":
    print("=== FIZZBUZZ ===")
    print("Ejecutando FizzBuzz del 1 al 50:")
    print("-" * 30)
    
    # Ejecutar FizzBuzz del 1 al 50
    fizzbuzz(50)
    
    print("\n" + "=" * 30)
    print("Versión con lista (primeros 15 elementos):")
    print(fizzbuzz_lista(15))
