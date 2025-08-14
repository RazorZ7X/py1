# 🐍 Proyecto Python - Herramientas de Programación

Un conjunto de herramientas y scripts útiles en Python, incluyendo una calculadora interactiva, análisis de archivos CSV, implementación de FizzBuzz y más.

## 📋 Descripción

Este proyecto contiene varios módulos y scripts de Python diseñados para diferentes propósitos:

- **`index.py`** - Calculadora interactiva con operaciones matemáticas básicas
- **`analisis.py`** - Analizador de archivos CSV con funcionalidades básicas y avanzadas
- **`fizzbuzz.py`** - Implementación del clásico problema de programación FizzBuzz

## 🚀 Características

### Calculadora (`index.py`)
- Operaciones básicas: suma, resta, multiplicación, división y potencia
- Bucle infinito hasta que el usuario escriba "salir"
- Manejo de errores robusto
- Interfaz amigable con emojis

### Analizador CSV (`analisis.py`)
- Lectura de archivos CSV usando bibliotecas estándar de Python
- Análisis avanzado con pandas (opcional)
- Creación automática de archivos CSV de ejemplo
- Estadísticas descriptivas y visualización de datos

### FizzBuzz (`fizzbuzz.py`)
- Implementación clásica del problema FizzBuzz
- Dos versiones: impresión directa y retorno de lista
- Código limpio y bien documentado
- Fácil de importar y usar en otros proyectos

## 📋 Requisitos

- **Python 3.11+** (probado con Python 3.11.2544.0)
- **Bibliotecas estándar**: `csv`, `datetime`, `os`
- **Opcional**: `pandas` para análisis avanzado de CSV

## 🛠️ Instalación

### 1. Clonar o descargar el proyecto
```bash
git clone <url-del-repositorio>
cd py1
```

### 2. Crear entorno virtual (recomendado)
```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. Instalar dependencias opcionales
```bash
# Instalar pandas para análisis avanzado de CSV
pip install pandas
```

## 🎯 Uso

### Calculadora
```bash
python index.py
```
La calculadora te guiará a través de las operaciones disponibles.

### Analizador CSV
```bash
python analisis.py
```
El analizador buscará un archivo CSV o te permitirá crear uno de ejemplo.

### FizzBuzz
```bash
python fizzbuzz.py
```
Ejecuta FizzBuzz del 1 al 50 y muestra los primeros 15 elementos como lista.

### Uso como módulo
```python
# Importar funciones de FizzBuzz
from fizzbuzz import fizzbuzz, fizzbuzz_lista

# Ejecutar FizzBuzz del 1 al 20
fizzbuzz(20)

# Obtener lista de resultados
resultados = fizzbuzz_lista(20)
```

## 📁 Estructura del Proyecto

```
py1/
├── README.md           # Este archivo
├── index.py            # Calculadora interactiva
├── analisis.py         # Analizador de archivos CSV
├── fizzbuzz.py         # Implementación de FizzBuzz
└── .venv/              # Entorno virtual (creado automáticamente)
```

## 🔧 Configuración del Entorno

### Variables de Entorno
No se requieren variables de entorno especiales.

### Configuración del Linter
Si usas VS Code o Cursor, asegúrate de que el intérprete de Python apunte al entorno virtual:
- `Ctrl+Shift+P` → "Python: Select Interpreter"
- Selecciona el intérprete de `.venv`

## 📊 Ejemplos de Uso

### Ejemplo de Salida de la Calculadora
```
=== CALCULADORA PYTHON ===
Operaciones disponibles: +, -, *, /, ** (potencia)
Escribe 'salir' como operación para terminar
----------------------------------------

¿Qué operación quieres realizar? (+, -, *, /, **, salir): +
Ingresa el primer número: 15
Ingresa el segundo número: 25

📊 RESULTADO: 15.0 + 25.0 = 40.0
```

### Ejemplo de Salida de FizzBuzz
```
=== FIZZBUZZ ===
Ejecutando FizzBuzz del 1 al 50:
------------------------------
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
...
```

## 🐛 Solución de Problemas

### Error: "Could not find import of pandas"
- **Solución**: Instalar pandas en el entorno virtual activo
- **Comando**: `pip install pandas`

### Error: "No module named 'csv'"
- **Solución**: Asegúrate de usar Python 3.11+ (csv es parte de la biblioteca estándar)

### Linter no reconoce módulos
- **Solución**: Activa el entorno virtual y selecciona el intérprete correcto en tu editor

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje de Python.

## 📞 Soporte

Si tienes preguntas o problemas:
- Revisa la sección de "Solución de Problemas"
- Abre un issue en el repositorio
- Contacta al desarrollador

---

**¡Disfruta programando con Python! 🐍✨**
