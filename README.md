# TSP - Genetic Algorithm in Python

> Translations: [Español](README_spanish.md)

This GUI program solves the Traveling Salesman Problem (TSP) and offers a visual, interactive genetic algorithm
application with intuitive controls for configuring the number of cities.

The application generates a set of random cities on a canvas and evolves a population of candidate routes across 500
generations to find a near-optimal tour. Each generation applies tournament selection to choose the fittest parents,
Order Crossover (OX) to combine their city sequences into children, and swap mutation to introduce diversity by
exchanging two random cities with a 5% probability. An elitism strategy preserves the best route found so far,
ensuring the solution quality never degrades across generations.

## MVC Structure

- **Model**: Manages the genetic algorithm engine, domain objects (cities and routes) and handles the evolution process including selection, crossover and mutation.
- **View**: Includes all UI components such as buttons, spinners, labels and a canvas to ensure a responsive and attractive user experience.
- **Controller**: Processes user inputs, updates the model and view, manages animation scheduling and application flow.

## Python Libraries Used

- **tkinter.Tk**: Provides the main application window for the GUI.
- **tkinter.Canvas**: Renders cities and route connections on a drawable surface.
- **tkinter.Button**: Creates interactive buttons that trigger callbacks when clicked.
- **tkinter.Spinbox**: Allows the user to select a numeric value within a bounded range.
- **tkinter.Label**: Displays text such as generation count and best distance.
- **tkinter.Frame**: Groups and organizes widgets into layout sections.
- **tkinter.messagebox**: Shows error and validation dialogs to the user.
- **abc.ABC**: Defines abstract base classes for visitor and observer interfaces.
- **abc.abstractmethod**: Marks methods that must be implemented by concrete subclasses.
- **random.uniform**: Generates random floating-point city coordinates within bounds.
- **random.shuffle**: Randomizes city order to create initial route populations.
- **random.randint**: Selects random indices for crossover and mutation operations.
- **random.sample**: Picks random candidates for tournament selection.
- **random.random**: Generates a probability value to decide whether mutation occurs.

## Dependencies

- Python 3.10+
- Tkinter (included with standard Python installations)

## Features

- Real-time visualization of the best route on a canvas
- Animated evolution across 500 generations
- Configurable city count (5 to 30) via spinner input
- Start, Stop and Reset controls for managing the evolution
- Input validation with visual error dialogs
- Elitism strategy preserving the best route each generation
- Tournament selection, Order Crossover (OX) and swap mutation

## Algorithm

| Parameter        | Value                |
|------------------|----------------------|
| Population size  | 10                   |
| Generation limit | 500                  |
| Selection        | Tournament (size 3)  |
| Crossover        | Order Crossover (OX) |
| Mutation         | Swap (5% rate)       |
| Elitism          | Best route preserved |

## Architecture

```
tsp_genetic_algorithm/
├── main.py
├── model/
│   ├── city.py                          # City with coordinates and distance calculation
│   ├── route.py                         # Route with crossover, mutation, and evaluation
│   ├── evolution_model.py               # Genetic algorithm engine
│   ├── factories/
│   │   ├── city_factory.py              # Creates cities at random positions
│   │   └── route_factory.py             # Creates shuffled route populations
│   ├── observers/
│   │   └── evolution_observer.py        # Observer interface for evolution events
│   └── visitors/
│       ├── city_visitor.py              # Visitor interface for city coordinates
│       ├── route_visitor.py             # Visitor interface for route segments
│       └── evolution_visitor.py         # Visitor interface for statistics and best route
├── view/
│   ├── view.py                          # Main view orchestrator
│   ├── control_panel.py                 # Spinner and buttons
│   ├── map_canvas.py                    # Canvas for rendering cities and routes
│   └── factories/
│       └── widget_abstract_factory.py   # Styled Tkinter widget creation
├── controller/
│   ├── controller.py                    # MVC orchestrator
│   └── route_renderer.py               # Renders route segments on canvas
├── validation/
│   └── input_parser.py                  # Bounded integer parsing
└── tests/
    ├── test_city.py
    ├── test_route.py
    ├── test_evolution_model.py
    └── (mock visitors, verifiers, collectors)
```

## Design Patterns

| Pattern              | Usage                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Observer**         | Model notifies Controller of generation evolution and completion                                                              |
| **Visitor**          | City and Route expose data through visitor interfaces without exposing state directly (It always assures behavior over state) |
| **Abstract Factory** | `WidgetAbstractFactory` creates a family of related styled widgets (labels, buttons, spinners)                                |
| **Factory Method**   | `CityFactory` creates cities at random positions; `RouteFactory` creates shuffled route populations                           |

## Program Flow

The application starts by creating the Model, View and Controller in `main.py`. The Controller retrieves the canvas dimensions from the View and passes them to the Model, which initializes the CityFactory with the available drawing area.

When the user sets a city count and clicks Start, the Controller validates the input through the InputParser. If the input is invalid, a dialog warns the user. Otherwise, the Model generates random cities and creates an initial population of shuffled routes.

The Controller begins an animation loop that calls the Model's `step` method every 50 milliseconds. Each step evolves the population by preserving the best route, selecting parents through tournament selection, producing children via Order Crossover and applying swap mutation with a 5% probability. The population is then ranked by total distance.

After each generation, the Model notifies the Controller through the Observer pattern. The Controller re-renders the canvas using the Visitor pattern: the RouteRenderer draws route segments between cities, and the Controller draws city dots at each coordinate.

If the user clicks Stop, the animation loop pauses and the evolution can be resumed by clicking Start again with the same city count. Changing the city count after starting requires pressing Reset first, which generates a fresh set of cities and a new population.

After 500 generations, the Model notifies completion. The Controller stops the animation loop and the View disables the Start and Stop buttons, leaving only Reset available to begin a new run.

## Setting up on Mac

Before running the project, make sure you have the following installed:

1. **Python 3.10+**: [Python Downloads](https://www.python.org/downloads/)
2. **Tkinter**: Included with standard Python installations on macOS

### Steps

1. Verify Python is installed:
   ```bash
   python3 --version
   ```
2. Verify Tkinter is available:
   ```bash
   python3 -c "import tkinter; print('Tkinter is available')"
   ```
3. Clone the repository and create a working branch:
   ```bash
   git clone <repository-url>
   cd tsp_genetic_algorithm
   git checkout -b <branch-name>
   ```
   Avoid working directly on `main`. Always create a branch for your changes.
4. Run the application:
   ```bash
   python3 main.py
   ```
5. Run the tests:
   ```bash
   python3 -m unittest discover tests/ -v
   ```

## Setting up on Windows

Before running the project, make sure you have the following installed:

1. **Python 3.10+**: [Python Downloads](https://www.python.org/downloads/)
2. **Tkinter**: Included with the standard Python installer. During installation, make sure the **tcl/tk and IDLE** checkbox is selected.

### Steps

1. Verify Python is installed (open Command Prompt or PowerShell):
   ```cmd
   python --version
   ```
   If `python` is not recognized, add Python to your system PATH. The default installation path is:
   ```
   C:\Users\<username>\AppData\Local\Programs\Python\Python3xx\
   ```
2. Verify Tkinter is available:
   ```cmd
   python -c "import tkinter; print('Tkinter is available')"
   ```
   If Tkinter is missing, reinstall Python and check the **tcl/tk and IDLE** option in the installer.
3. Clone the repository and create a working branch:
   ```cmd
   git clone <repository-url>
   cd tsp_genetic_algorithm
   git checkout -b <branch-name>
   ```
   Avoid working directly on `main`. Always create a branch for your changes.
4. Run the application:
   ```cmd
   python main.py
   ```
5. Run the tests:
   ```cmd
   python -m unittest discover tests/ -v
   ```

## License

Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Acknowledgements

This project was created as an educational example for demonstrating the Model-View-Controller (MVC) design pattern
in Python with Tkinter.
