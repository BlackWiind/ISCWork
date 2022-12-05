import sys
from model import Model
from controller import Controller
from PyQt5 import QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    model = Model()
    controller = Controller(model)

    app.exec_()


if __name__ == '__main__':
    sys.exit(main())



