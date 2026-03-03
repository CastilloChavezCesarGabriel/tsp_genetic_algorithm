from model.visitors.evolution_visitor import EvolutionVisitor

class SummaryVisitor(EvolutionVisitor):
    def __init__(self, view):
        self._view = view

    def visit_statistics(self, generation, best_distance):
        self._view.summarize(generation, best_distance)

    def visit_best_route(self, route):
        pass