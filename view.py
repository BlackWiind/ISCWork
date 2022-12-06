import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget, QRadioButton, \
    QTextBrowser, QButtonGroup
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.initUI()
        self.controller = controller

    def initUI(self):
        self.resize(640, 480)
        self.setWindowTitle('Контрольная работа')

        # Основной вертикальный контейнер
        self.basic_vertical_container = QVBoxLayout(self)

        self.basic_vertical_container.setAlignment(Qt.AlignTop)

        # Основные горизонтальные контейнеры
        self.basic_vertical_container.setContentsMargins(10, 10, 10, 10)
        self.basic_horizontal_container_top = QHBoxLayout(self)
        self.basic_horizontal_container_bot = QHBoxLayout(self)
        self.basic_vertical_container.addLayout(self.basic_horizontal_container_top)
        self.basic_vertical_container.addLayout(self.basic_horizontal_container_bot)

        # Заполнение верхнего контейнера: контейнер для текста, для матрицы и для графа
        self.text_container = QVBoxLayout(self)
        self.matrix_container = QVBoxLayout(self)
        self.graph_container = QVBoxLayout(self)
        self.basic_horizontal_container_top.addLayout(self.text_container)
        self.basic_horizontal_container_top.addLayout(self.matrix_container)
        self.basic_horizontal_container_top.addLayout(self.graph_container)

        widget = QWidget(self)
        widget.setLayout(self.basic_vertical_container)
        self.setCentralWidget(widget)

        # Контейнер для текста: лейбл для названия и лейбл для самого текста
        self.text_label = QLabel(self)
        self.text_view = QTextBrowser(self)
        self.text_label.setFixedSize(120, 40)
        self.text_label.setText("Текст")
        self.text_container.addWidget(self.text_label)
        self.text_view.setFixedSize(150, 200)
        self.text_view.setText("Тут появится количество и типы вопросов,"
                               "а так-же результат верификации")
        self.text_container.addWidget(self.text_view)

        # Контейнер для матрицы: лейбл для названия и для вывода матрицы
        self.matrix_label = QLabel(self)
        self.matrix_view = QTextBrowser(self)
        self.matrix_label.setFixedSize(120, 40)
        self.matrix_label.setText("Матрица")
        self.matrix_container.addWidget(self.matrix_label)
        self.matrix_view.setFixedSize(150, 200)
        self.matrix_view.setText("Тут будет выведена выбранная матрица")
        self.matrix_container.addWidget(self.matrix_view)

        # Контейнер для графа: лейбл для названия и канвас из для графа
        self.graph_label = QLabel(self)
        self.graph_label.setFixedSize(120, 40)
        self.graph_label.setText("Граф")
        self.graph_container.addWidget(self.graph_label)
        self.fig = plt.figure(figsize=(2, 2))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.graph_container.addWidget(self.canvas)

        # Заполнение нижнего контейнера: кнопка и radiobuttom
        self.run_button = QPushButton()
        self.run_button.setText("Сделать работу")
        self.run_button.clicked.connect(self.button_clicked)
        self.basic_horizontal_container_bot.addWidget(self.run_button)

        self.matrix_radio_1 = QRadioButton("Матрица смежности")
        self.matrix_radio_1.matrix = "h_matrix"
        self.matrix_radio_1.setCheckable(False)
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio_1)

        self.matrix_radio_2 = QRadioButton("Гамильтонов цикл")
        self.matrix_radio_2.setCheckable(False)
        self.matrix_radio_2.matrix = "cycle"
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio_2)

        self.matrix_radio_3 = QRadioButton("Закодированная матрица")
        self.matrix_radio_3.setCheckable(False)
        self.matrix_radio_3.matrix = "f_matrix"
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio_3)

        self.matrix_radio_4 = QRadioButton("Зашифрованная матрица")
        self.matrix_radio_4.setCheckable(False)
        self.matrix_radio_4.matrix = "tilda_matrix"
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio_4)

        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.matrix_radio_1)
        self.radio_group.addButton(self.matrix_radio_2)
        self.radio_group.addButton(self.matrix_radio_3)
        self.radio_group.addButton(self.matrix_radio_4)
        self.radio_group.buttonClicked.connect(self.radio_changed)

    def radio_changed(self, button):
        self.controller.radio_change(button.matrix)

    def button_clicked(self):
        self.matrix_radio_1.setCheckable(True)
        self.matrix_radio_2.setCheckable(True)
        self.matrix_radio_3.setCheckable(True)
        self.matrix_radio_4.setCheckable(True)
        self.controller.verification()
        self.controller.draw_graph()


