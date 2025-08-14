"""
Módulo FizzBuzz - Implementación del Clásico Problema de Programación

Este módulo implementa el famoso problema FizzBuzz, un ejercicio común en
entrevistas de programación y aprendizaje de lógica condicional.

Reglas de FizzBuzz:
- Para números del 1 al n:
  * Si es múltiplo de 3: imprime "Fizz"
  * Si es múltiplo de 5: imprime "Buzz"
  * Si es múltiplo de ambos (3 y 5): imprime "FizzBuzz"
  * En otro caso: imprime el número

Funciones disponibles:
- fizzbuzz(n): Ejecuta FizzBuzz e imprime los resultados
- fizzbuzz_lista(n): Retorna una lista con los resultados

Autor: Desarrollador Python RazorZ7X
Versión: 1.0
"""

def fizzbuzz(n):
    """
    Ejecuta el algoritmo FizzBuzz del 1 al número especificado.
    
    Esta función implementa la lógica clásica de FizzBuzz:
    - Itera desde 1 hasta n (inclusive)
    - Aplica las reglas de FizzBuzz para cada número
    - Imprime directamente los resultados en la consola
    
    Args:
        n (int): Número hasta el cual ejecutar FizzBuzz (inclusive)
    
    Returns:
        None: La función solo imprime los resultados
        
    Ejemplos:
        >>> fizzbuzz(15)
        1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
        
    Notas:
        - n debe ser un entero positivo
        - La función imprime directamente en la consola
        - No retorna ningún valor
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
    Versión de FizzBuzz que retorna una lista con los resultados.
    
    Similar a fizzbuzz(), pero en lugar de imprimir los resultados,
    los almacena en una lista y la retorna. Esto es útil para:
    - Procesamiento posterior de los resultados
    - Análisis de patrones
    - Integración con otros algoritmos
    
    Args:
        n (int): Número hasta el cual ejecutar FizzBuzz (inclusive)
    
    Returns:
        list: Lista con los resultados de FizzBuzz del 1 al n
        
    Ejemplos:
        >>> fizzbuzz_lista(10)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
        
        >>> fizzbuzz_lista(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        
    Notas:
        - n debe ser un entero positivo
        - Los números se convierten a string para mantener consistencia con "Fizz", "Buzz", "FizzBuzz"
        - La función no imprime nada en la consola
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
    """
    Bloque principal de ejecución del módulo.
    
    Cuando se ejecuta este archivo directamente (no como módulo importado),
    se ejecuta automáticamente FizzBuzz del 1 al 50 y se muestra
    una demostración de la versión con lista.
    """
    print("=== FIZZBUZZ ===")
    print("Ejecutando FizzBuzz del 1 al 50:")
    print("-" * 30)
    
    # Ejecutar FizzBuzz del 1 al 50
    fizzbuzz(50)
    
    print("\n" + "=" * 30)
    print("Versión con lista (primeros 15 elementos):")
    print(fizzbuzz_lista(15))
