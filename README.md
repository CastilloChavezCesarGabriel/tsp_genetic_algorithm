# TSP - Genetic Algorithm in Python

> Translations: [Español](README_spanish.md)

This GUI program solves the Traveling Salesman Problem (TSP) by generating a set of random cities on a canvas and
evolving a population of candidate routes across 500 generations to find a near-optimal tour. Each generation applies
tournament selection to choose the fittest parents, Order Crossover (OX) to combine their city sequences into children,
and swap mutation to introduce diversity between two random cities with a 5% probability. An elitism strategy
preserves the best route found so far, ensuring the solution quality never gets lost across generations.

## MVC Structure

- **Model**: Manages the genetic algorithm engine, domain objects (cities and routes) and handles the evolution process including selection, crossover and mutation.
- **View**: Includes all UI components such as buttons, spinners, labels and a canvas to ensure a responsive and attractive user experience.
- **Controller**: Processes user inputs, updates the model and view, manages animation scheduling and application flow.

## Python Libraries Used

- **tkinter.Tk**: Provides the main application window for the GUI.
- **tkinter.Canvas**: Renders cities and route connections on a drawable surface.
- **tkinter.Label**: Displays text such as generation count and best distance.
- **tkinter.Frame**: Groups and organizes widgets into layout sections.
- **tkinter.messagebox**: Shows error and validation dialogs to the user.
- **tkinter.ttk.Style**: Configures themed widget styles with custom colors and hover states.
- **tkinter.ttk.Button**: Creates styled, themed buttons with color variants (Start, Stop, Reset).
- **tkinter.ttk.Spinbox**: Provides a themed numeric selector with dark styling.
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

- Real-time visualization of the best route on a bordered canvas
- Animated evolution across 500 generations
- Configurable city count (5 to 30) via themed spinner input
- Color-coded Start (green), Stop (red) and Reset (gray) buttons with hover states
- Themed dark UI with consistent typography hierarchy
- Completion summary displaying the near-optimal distance found
- Input validation with visual error dialogs
- Elitism strategy preserving the best route each generation
- Tournament selection, Order Crossover (OX) and swap mutation

## Algorithm

| Parameter        | Value                |
|------------------|----------------------|
| Distance         | Euclidean (2D)       |
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
│   ├── route_renderer.py               # Renders route segments on canvas
│   └── summary_visitor.py              # Displays completion summary
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

1. The application sets up the `Model`, `View` and `Controller` in `main.py`, so the Controller can retrieve the canvas dimensions from the View, forward them to the Model and initialize the CityFactory with the available drawing area.

2. Once the user picks a city count and clicks Start, the Controller runs the input through the InputParser. If the value is invalid, a warning dialog is shown. Otherwise, the Model scatters random cities and builds an initial population of equally random routes.

3. The Controller kicks off an animation loop that calls the Model's `step` method every 50 milliseconds, incrementally evolving the population by preserving the best route, picking parents through tournament selection, breeding children via Order Crossover and applying swap mutation with a 5% probability. The population is then ranked by total distance.

4. After each generation, the Model notifies the Controller through the Observer pattern, which in turn redraws the canvas through the Visitor pattern.

5. After 500 generations, the Model signals completion, the Controller halts the animation loop and a `SummaryVisitor` displays the near-optimal distance found. By the way, the View disables the Start and Stop buttons as it leaves only the Reset button available to kick off a fresh run.

## Setting up on Mac

Before running the project, make sure you have the following installed:

1. **Python 3.10+**: [Python Downloads](https://www.python.org/downloads/)
2. **Tkinter**: Included with standard Python installations on macOS

### Steps

1. Check that Python is installed:
   ```bash
   python3 --version
   ```
2. Check that Tkinter is available:
   ```bash
   python3 -c "import tkinter; print('Tkinter is available')"
   ```
3. Clone the repository and create a new working branch (since the **main** branch is reserved for production code only):
   ```bash
   git clone <repository-url>
   cd tsp_genetic_algorithm
   git checkout -b <branch-name>
   ```
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

1. Check that Python is installed (open Command Prompt or PowerShell):
   ```cmd
   python --version
   ```
   If `python` is not recognized, add Python to your system PATH. The default installation path is:
   ```
   C:\Users\<username>\AppData\Local\Programs\Python\Python3xx\
   ```
2. Check that Tkinter is available:
   ```cmd
   python -c "import tkinter; print('Tkinter is available')"
   ```
   If not, reinstall Python and check the **tcl/tk and IDLE** option in the installer.
3. Clone the repository and create a new working branch (since the **main** branch is reserved for production code only):
   ```cmd
   git clone <repository-url>
   cd tsp_genetic_algorithm
   git checkout -b <branch-name>
   ```
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
