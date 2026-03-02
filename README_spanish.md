# TSP - Algoritmo Genético en Python

> Traducciones: [English](README.md)

Este programa con interfaz gráfica resuelve el Problema del Viajante de Comercio (TSP) tras generar un conjunto de
ciudades aleatorias sobre un lienzo y evolucionar una población de rutas candidatas a lo largo de 500 generaciones para
encontrar el recorrido más óptimo. Cada generación aplica selección por torneo para elegir los padres más aptos,
Cruce de Orden (OX) para combinar sus secuencias de ciudades en hijos, y mutación por intercambio para introducir
diversidad entre dos ciudades aleatorias con un 5% de probabilidad. Una estrategia de elitismo preserva
la mejor ruta encontrada hasta el momento, asegurando que la calidad de la solución nunca se degrade a lo largo de
las generaciones.

## Estructura MVC

- **Modelo**: Gestiona el motor del algoritmo genético, los objetos del dominio (ciudades y rutas) y maneja el proceso de evolución incluyendo selección, cruce y mutación.
- **Vista**: Incluye todos los componentes de interfaz como botones, selectores numéricos, etiquetas y un lienzo para asegurar una experiencia de usuario atractiva y responsiva.
- **Controlador**: Procesa las entradas del usuario, actualiza el modelo y la vista, gestiona la programación de animaciones y el flujo de la aplicación.

## Bibliotecas de Python Utilizadas

- **tkinter.Tk**: Proporciona la ventana principal de la aplicación para la interfaz gráfica.
- **tkinter.Canvas**: Renderiza las ciudades y conexiones de rutas sobre una superficie dibujable.
- **tkinter.Button**: Crea botones interactivos que ejecutan callbacks al ser pulsados.
- **tkinter.Spinbox**: Permite al usuario seleccionar un valor numérico dentro de un rango limitado.
- **tkinter.Label**: Muestra texto como el conteo de generaciones y la mejor distancia.
- **tkinter.Frame**: Agrupa y organiza widgets en secciones de diseño.
- **tkinter.messagebox**: Muestra diálogos de error y validación al usuario.
- **abc.ABC**: Define clases base abstractas para las interfaces de visitante y observador.
- **abc.abstractmethod**: Marca métodos que deben ser implementados por las subclases concretas.
- **random.uniform**: Genera coordenadas aleatorias de punto flotante para las ciudades dentro de los límites.
- **random.shuffle**: Aleatoriza el orden de las ciudades para crear las poblaciones iniciales de rutas.
- **random.randint**: Selecciona índices aleatorios para las operaciones de cruce y mutación.
- **random.sample**: Escoge candidatos aleatorios para la selección por torneo.
- **random.random**: Genera un valor de probabilidad para decidir si ocurre una mutación.

## Dependencias

- Python 3.10+
- Tkinter (incluido con las instalaciones estándar de Python)

## Características

- Visualización en tiempo real de la mejor ruta sobre un mapa predefinido
- Evolución animada a lo largo de las 500 generaciones generadas
- Configuración de ciudades mediante selectores numéricos
- Controles de **Inicio**, **Pausa** y **Reinicio** para gestionar la evolución de las rutas
- Validación de entrada con diálogos visuales de error
- Estrategia de elitismo que preserva la mejor ruta en cada generación
- Selección por torneo, Cruce de Orden (OX) y mutación por intercambio

## Algoritmo (Configuración predefinida)

| Parámetro              | Valor                     |
|------------------------|---------------------------|
| Tamaño de población    | 10                        |
| Límite de generaciones | 500                       |
| Selección              | Torneo (tamaño 3)         |
| Cruce                  | Cruce de Orden (OX)       |
| Mutación               | Intercambio (tasa del 5%) |
| Elitismo               | Mejor ruta preservada     |

## Arquitectura y patrón arquitectónico

```
tsp_genetic_algorithm/
├── main.py
├── model/
│   ├── city.py                          # Ciudad con coordenadas y cálculo de distancia
│   ├── route.py                         # Ruta con cruce, mutación y evaluación
│   ├── evolution_model.py               # Motor del algoritmo genético
│   ├── factories/
│   │   ├── city_factory.py              # Crea ciudades en posiciones aleatorias
│   │   └── route_factory.py             # Crea poblaciones de rutas aleatorias
│   ├── observers/
│   │   └── evolution_observer.py        # Interfaz que observa los eventos de evolución
│   └── visitors/
│       ├── city_visitor.py              # Interfaz que visita las coordenadas de una ciudad
│       ├── route_visitor.py             # Interfaz que visita segmentos de ruta
│       └── evolution_visitor.py         # Interfaz que visita las estadísticas y la mejor ruta
├── view/
│   ├── view.py                          # Orquestador principal de la vista
│   ├── control_panel.py                 # Selector numérico y botones
│   ├── map_canvas.py                    # Lienzo (mapa) para renderizar ciudades y rutas
│   └── factories/
│       └── widget_abstract_factory.py   # Creación de widgets Tkinter con estilo
├── controller/
│   ├── controller.py                    # Orquestador MVC
│   └── route_renderer.py               # Renderiza segmentos de ruta en el mapa
├── validation/
│   └── input_parser.py                  # Análisis de enteros con límites
└── tests/
    ├── test_city.py
    ├── test_route.py
    ├── test_evolution_model.py
    └── (visitantes mock, verificadores, recolectores)
```

## Patrones de Diseño

| Patrón               | Uso                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| **Observer**         | El `Modelo` notifica al `Controlador` sobre la evolución de generaciones y su finalización                    |
| **Visitor**          | Las clases `Ciudad` y `Ruta` exponen datos a través de interfaces sin exponer su estado directamente          |
| **Abstract Factory** | `WidgetAbstractFactory` crea una familia de widgets con estilos relacionados (etiquetas, botones, selectores) |
| **Factory Method**   | `CityFactory` crea ciudades en posiciones aleatorias; `RouteFactory` crea poblaciones de rutas aleatorias     |

## Flujo del Programa

1. La aplicación crea el `Modelo`, la `Vista` y el `Controlador` en `main.py`, para darle al Controlador las dimensiones del mapa de la Vista, pasarlas al Modelo e inicializar el CityFactory con el área de dibujo disponible.

2. Cuando el usuario establece una cantidad de ciudades y hace clic en Inicio, el Controlador valida la entrada a través del InputParser. Si la entrada es inválida, se muestra un diálogo que advierte al usuario. De lo contrario, el Modelo genera ciudades aleatorias y crea una población inicial de rutas igualmente aleatorias.

3. El Controlador inicia un ciclo de animación que llama al método `step` del Modelo cada 50 milisegundos, para evolucionar (por pasos) la población según sea la mejor ruta, seleccionar a los padres mediante selección por torneo, generar hijos mediante Cruce de Orden y aplicar mutación por intercambio con un 5% de probabilidad. La población se clasifica entonces por distancia total.

4. Después de cada generación, el Modelo notifica al Controlador a través del patrón Observer y este renderiza el lienzo o mapa usando el patrón Visitor.

5. Después de 500 generaciones, el Modelo notifica la finalización, el Controlador detiene los ciclos de animación y la Vista deshabilita los botones de Inicio y Pausa, dejando solamente el botón de Reinicio disponible para comenzar un nuevo caso.

## Configuración en Mac

Antes de ejecutar el proyecto, asegúrate de instalar lo siguiente:

1. **Python 3.10+**: [Descargas de Python](https://www.python.org/downloads/)
2. **Tkinter**: Incluido con las instalaciones estándar de Python en macOS

### Pasos

1. Verifica que Python esté instalado:
   ```bash
   python3 --version
   ```
2. Verifica que Tkinter esté disponible:
   ```bash
   python3 -c "import tkinter; print('Tkinter está disponible')"
   ```
3. Clona el repositorio y crea una nueva rama de trabajo (Ya que la rama **main** es solamente para el código en producción):
   ```bash
   git clone <url-del-repositorio>
   cd tsp_genetic_algorithm
   git checkout -b <nombre-de-rama>
   ```
4. Ejecuta la aplicación:
   ```bash
   python3 main.py
   ```
5. Ejecuta las pruebas:
   ```bash
   python3 -m unittest discover tests/ -v
   ```

## Configuración en Windows

Antes de ejecutar el proyecto, asegúrate de instalar lo siguiente:

1. **Python 3.10+**: [Descargas de Python](https://www.python.org/downloads/)
2. **Tkinter**: Incluido con el instalador estándar de Python. Durante la instalación, asegúrese de que la casilla **tcl/tk and IDLE** esté seleccionada.

### Pasos

1. Verifica que Python esté instalado (abre el Símbolo del Sistema o PowerShell):
   ```cmd
   python --version
   ```
   Si `python` no es reconocido, agrega Python a la variable PATH del sistema, en donde, la ruta de instalación por defecto es:
   ```
   C:\Users\<usuario>\AppData\Local\Programs\Python\Python3xx\
   ```
2. Verifica que Tkinter esté disponible:
   ```cmd
   python -c "import tkinter; print('Tkinter está disponible')"
   ```
   Si no, reinstala Python y marca la opción **tcl/tk and IDLE** en el instalador.
3. Clona el repositorio y crea una nueva rama de trabajo (Ya que la rama **main** es solamente para el código en producción):
   ```cmd
   git clone <url-del-repositorio>
   cd tsp_genetic_algorithm
   git checkout -b <nombre-de-rama>
   ```
4. Ejecuta la aplicación:
   ```cmd
   python main.py
   ```
5. Ejecuta las pruebas:
   ```cmd
   python -m unittest discover tests/ -v
   ```

## Licencia

Licencia Creative Commons Atribución 4.0 Internacional (CC BY 4.0).

## Agradecimientos

Este proyecto fue creado como un ejemplo educativo para demostrar el patrón de diseño Modelo-Vista-Controlador (MVC)
en Python con Tkinter y la aplicación de los algoritmos genéticos para la resolución de problemas cotidianos.
