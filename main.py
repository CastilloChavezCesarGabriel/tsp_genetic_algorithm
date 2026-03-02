import tkinter as tk
from model.evolution_model import EvolutionModel
from view.view import View
from controller.controller import Controller


def main():
    root = tk.Tk()
    model = EvolutionModel()
    view = View(root)
    controller = Controller(model, view)
    root.after(100, controller.initialize)
    root.mainloop()


if __name__ == "__main__":
    main()
