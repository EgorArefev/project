import sys
import csv

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.Qt import QWidget, QLineEdit, QPushButton, QApplication, QLabel, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from PyQt5.QtWidgets import QMessageBox


class Display(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ГЛавный экран")
        self.setStyleSheet('background-color : rgb(255,255,255);')
        self.setWindowTitle('MainWindow1')
        self.setGeometry(300, 300, 500, 200)

        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(255,0,0); color: #fff')
        self.pushButton.setText('Подсчёт ИМТ')
        self.pushButton.clicked.connect(self.A)

        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(255,0,0); color: #fff')
        self.pushButton.setText('Рацион калорий')
        self.pushButton.clicked.connect(self.A_2)
        self.pushButton.setGeometry(0, 31, 100, 30)

    def A(self):
        self.cams = Calculator()
        self.cams.show()
        self.close()

    def A_2(self):
        self.cams = MyWidget()
        self.cams.show()
        self.close()


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("untitled.ui", self)

        self.setWindowTitle("Подсчёт ИМТ")
        self.setWindowTitle('MainWindow2')
        self.params = {}

        self.pushButton1 = QPushButton(self)
        self.pushButton1.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton1.setText('Вернуться на главную')
        self.pushButton1.setGeometry(0, 0, 150, 36)
        self.pushButton1.clicked.connect(self.B)

        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.run)

    def calculate(self):
        self.IMT.setText(f"{float(self.weight.text()) / (float(self.height1.text()) / 100) ** 2: .2f}")

    def run(self):
        self.IMT.setText(f"{float(self.weight.text()) / (float(self.height1.text()) / 100) ** 2: .2f}")
        if float(self.IMT.text()) < 18.5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Дефицит массы тела ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()


        elif float(self.IMT.text()) >= 18.5 and float(self.IMT.text()) <= 24.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Нормальная масса тела ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()


        elif float(self.IMT.text()) >= 25 and float(self.IMT.text()) <= 29.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Увеличение массы тела ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()


        elif float(self.IMT.text()) >= 30 and float(self.IMT.text()) <= 34.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Ожирение 1 степени ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()


        elif float(self.IMT.text()) >= 35 and float(self.IMT.text()) <= 39.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Ожирение 2 степени ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()


        elif float(self.IMT.text()) >= 40:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText(" Ожирение 3 степени ")

            # setting Message box window title
            msg.setWindowTitle("Information MessageBox")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # start the app
            retval = msg.exec_()

    def B(self):
        self.cams = Display()
        self.cams.show()
        self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('task3.ui', self)
        self.load_table('kalorii.csv')

        self.tableWidget.itemChanged.connect(self.update_check)
        self.setWindowTitle("Рацион калорий")
        self.setWindowTitle('MainWindow2')

        self.pushButton1 = QPushButton(self)
        self.pushButton1.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton1.setText('Вернуться на главную')
        self.pushButton1.setGeometry(0, 520, 150, 36)
        self.pushButton1.clicked.connect(self.B_2)

    def load_table(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title) + 1)
            self.tableWidget.setHorizontalHeaderLabels(title + ["Количество, г"])
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)
            self.tableWidget.setRowCount(0)

            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
                self.tableWidget.setItem(i, j + 1, QTableWidgetItem('0'))
            self.tableWidget.resizeColumnsToContents()

    def update_check(self):
        price = [float(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
        count = [float(self.tableWidget.item(i, 2).text()) if self.tableWidget.item(i, 2).text() != ''
                 else 0 for i in range(self.tableWidget.rowCount())]
        sum_of = 0
        sum_gr = 0
        for i in range(len(price)):
            sum_of += price[i] * count[i] / 100
            sum_gr = sum_of / 7700
        self.lineEdit.setText(str(sum_of))
        self.lineEdit_2.setText(str(round(sum_gr, 2)))

    def B_2(self):
        self.cams = Display()
        self.cams.show()
        self.close()


def exception_hook(cls, exception, traceback):
    sys.exception_hook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Display()
    w.show()
    ex = MyWidget()
    ex.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
