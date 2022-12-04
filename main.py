import sys
from  person import Person
from controller import Controller
from PyQt5 import QtWidgets

def main():

    app = QtWidgets.QApplication(sys.argv)
    person_a = Person()
    controller = Controller(person_a)

    app.exec_()


if __name__ == '__main__':
    sys.exit(main())



