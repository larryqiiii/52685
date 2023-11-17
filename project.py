# This is a sample Python script.
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
import math


class MyWidgets(QDialog):
    def __init__(self):
        super(MyWidgets, self).__init__()
        self.parseData()
        uic.loadUi("main.ui", self)
        self.comboBox.addItems(self.name)
        self.pushButton.clicked.connect(self.onClick1)
        self.pushButton_2.clicked.connect(self.onClick2)
        print("0")

    def onClick1(self):
        name = self.comboBox.currentText().split(",")[0]
        if name == "Haymarket":
            data = self.data1
        elif name == "Zetland":
            data = self.data2
        elif name == "Burwood":
            data = self.data3
        data = sorted(data)
        mean = sum(data) // len(data)
        self.textBrowser.setText("The average of the renting price in {} suburb is ${} per week.\nThe lowest three renting price is ${}, ${}, ${}, per week".format(name, mean, data[0], data[1], data[2]))

    def onClick2(self):
        self.textBrowser.setText("")

    def parseData(self):
        self.data1 = []
        self.data2 = []
        self.data3 = []
        with open("data.txt", "r") as F:
            for i, line in enumerate(F.readlines()):
                if i==0:
                    self.name = line.split()
                else:
                    tmp = [x[1:-3] for x in line.split()]
                    self.data1.append(int(tmp[0]))
                    self.data2.append(int(tmp[1]))
                    self.data3.append(int(tmp[2]))

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWidgets()
    ui.show()
    sys.exit(app.exec())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
