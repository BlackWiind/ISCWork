import networkx as nx
import numpy as np

import model
from view import GraphWindow
import utils
import random


class Controller:

    def __init__(self, model):
        self.model = model
        self.view = GraphWindow(self)

        self.view.show()

    def verification(self):
        self.view.text_view.clear()
        self.view.text_view.append("Начата верификация:")
        first_question_count: int = 0
        second_question_count: int = 0
        is_verificated = True
        for _ in range(random.randint(1, 20)):
            if random.randint(0, 1) > 0:
                first_question_count += 1
                if not utils.question_one(self.model.all_matrixs(), self.model.rules, self.model.open_key):
                    is_verificated = False
            else:
                second_question_count += 1
                if not utils.question_two():
                    is_verificated = False
        self.view.text_view.append(f"было задано {first_question_count} первых и\n"
                                   f"{second_question_count} вторых вопросов.")
        self.view.text_view.append(f"Верификация пройдена успешно") if is_verificated else self.view.text_view.append(
            f"Верификация провалена")

    def radio_change(self, button):
        matrix: dict = self.model.all_matrixs()[button]
        m_string: str = ""
        for row_index, row in enumerate(matrix):
            m_string += str(matrix[row_index])
            m_string += "\n"
        self.view.matrix_view.setText(m_string)

    def draw_graph(self):
        G = nx.DiGraph(np.matrix(self.model.h_matrix))
        nx.draw(G, with_labels=True, node_size=300, arrows=False)
        self.view.canvas.draw()
