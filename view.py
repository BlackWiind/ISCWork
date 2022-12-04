import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget, QRadioButton, \
    QTextBrowser
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphWindow(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.initUI()
        self.controller = controller

    def initUI(self):
        self.resize(640, 480)
        self.setWindowTitle('Проверка!!!')

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
        self.text_label.setText("Здесь будет текст")
        self.text_container.addWidget(self.text_label)
        self.text_view.setFixedSize(150,200)
        self.text_view.setText("тексттексттекст0")
        self.text_container.addWidget(self.text_view)

        # Контейнер для матрицы: лейбл для названия и для вывода матрицы
        self.matrix_label = QLabel(self)
        self.matrix_view = QTextBrowser(self)
        self.matrix_label.setFixedSize(120, 40)
        self.matrix_label.setText("Здесь будет матрица")
        self.matrix_container.addWidget(self.matrix_label)
        self.matrix_view.setFixedSize(150,200)
        self.matrix_view.setText("матрицаматрицаматрица")
        self.matrix_container.addWidget(self.matrix_view)

        # Контейнер для графа: лейбл для названия и канвас из для графа
        self.graph_label = QLabel(self)
        self.graph_label.setFixedSize(120, 40)
        self.graph_label.setText("Здесь будет граф")
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

        self.matrix_radio = QRadioButton("Матрица смежности")
        self.matrix_radio.setCheckable(False)
        self.matrix_radio.toggled.connect(self.radio_changed)
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio)

        self.matrix_radio = QRadioButton("Гамильтонов цикл")
        self.matrix_radio.setCheckable(False)
        self.matrix_radio.toggled.connect(self.radio_changed)
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio)

        self.matrix_radio = QRadioButton("Гамильтонов цикл")
        self.matrix_radio.setCheckable(False)
        self.matrix_radio.toggled.connect(self.radio_changed)
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio)

        self.matrix_radio = QRadioButton("Гамильтонов цикл")
        self.matrix_radio.setCheckable(False)
        self.matrix_radio.toggled.connect(self.radio_changed)
        self.basic_horizontal_container_bot.addWidget(self.matrix_radio)





    def radio_changed(self):
        pass

    def button_clicked(self):
        #self.matrix_radio.setCheckable(True)
        self.text_view.setText(self.controller.verification())