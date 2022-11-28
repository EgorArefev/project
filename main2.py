import sqlite3
import sys
import csv
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.Qt import QWidget, QLineEdit, QPushButton, QApplication, QLabel, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidget
from PyQt5.QtWidgets import QMessageBox


# Главное окно
class Display(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главный экран")
        self.setStyleSheet('background-color : #FFFFE0;')
        self.setWindowTitle('Приложение для поддержания здорового тела')
        self.setGeometry(300, 300, 500, 550)

        # Создаю gif-фото
        self.label = QLabel(self)
        movie = QMovie("PyQt5.gif")
        gif_size = (400, 252)
        movie.setScaledSize(QSize(*gif_size))
        self.label.resize(*gif_size)
        self.label.setMovie(movie)
        self.label.move(40, 50)
        movie.start()

        # Создаю кнопки на главном экране и задаю им размеры и стили
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : red;"
                                      "}"
                                      )
        self.pushButton.setText('Подсчёт ИМТ')
        self.pushButton.setGeometry(40, 310, 400, 40)
        # Делаю навигацию для кнопок
        self.pushButton.clicked.connect(self.window_A1)

        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : red;"
                                      "}"
                                      )
        self.pushButton.setText('Рацион калорий')
        self.pushButton.clicked.connect(self.window_A2)
        self.pushButton.setGeometry(40, 355, 400, 40)

        # Создаю кнопки на главном экране и задаю им размеры и стили
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : red;"
                                      "}"
                                      )
        self.pushButton.setText('Рацион калорий')
        self.pushButton.setGeometry(40, 400, 400, 40)
        # Делаю навигацию для кнопок
        self.pushButton.clicked.connect(self.window_A3)

    # Навигация в другие окна
    def window_A1(self):
        self.cams = Calculator()
        self.cams.show()
        self.close()

    def window_A2(self):
        self.cams = CaloricContent()
        self.cams.show()
        self.close()

    def window_A3(self):
        self.cams = Searching()
        self.cams.show()
        self.close()


# Подсчет ИМТ(индекс массы тела)
class Calculator(QMainWindow):
    """
        Подсчет ИМТ(индекс массы тела)
        """
    def __init__(self):
        super().__init__()

        uic.loadUi("untitled.ui", self)

        self.setWindowTitle("Подсчёт ИМТ")
        self.params = {"Муж": "man", "Жен": "woman"}
        self.comboBox.addItems(list(self.params.keys()))

        # Создаю кнопку, делаю ей размер
        self.pushButton1 = QPushButton(self)
        self.pushButton1.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : lightblue;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "}"
                                       )
        self.pushButton1.setText('Вернуться на главную')
        self.pushButton1.setGeometry(0, 0, 150, 36)
        self.pushButton1.clicked.connect(self.window_B1)

        # Кнопкам, импортируемым из uic - файла делаем стили
        # При нажатии на кнопку идет подсчет ИМТ по введённым данным, и вывод в LineEdit
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : lightblue;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : red;"
                                      "}"
                                      )
        # При нажатии на кнопку результат из LineEdit определяет состояние тела
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_2.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : lightblue;"
                                        "}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color : red;"
                                        "}"
                                        )

    # Подсчет ИМТ
    def calculate(self):
        # Подсчет минимального веса в пределах нормы
        calc_normal_weight_min = 18.5 * ((float(self.height1.text()) / 100) ** 2)
        # Подсчет максимального веса в пределах нормы
        calc_normal_weight_max = 24.9 * ((float(self.height1.text()) / 100) ** 2)
        print(self.comboBox.currentText() == "Муж")

        if self.comboBox.currentText() == "Муж":
            calc_ideal_weight = 23 * ((float(self.height1.text()) / 100) ** 2)
        else:
            calc_ideal_weight = 21.5 * ((float(self.height1.text()) / 100) ** 2)

        # Формула подсчета ИМТ
        self.IMT.setText(f"{float(self.weight.text()) / (float(self.height1.text()) / 100) ** 2: .2f}")
        # Вывод нужного веса в пределах нормы
        self.medicine.setText(f"{calc_normal_weight_min: .0f} - {calc_normal_weight_max: .0f} кг")
        self.ideal.setText(f"{calc_ideal_weight: .0f}")

    # Определение, в какой физической форме находится пользователь
    def run(self):
        self.IMT.setText(f"{float(self.weight.text()) / (float(self.height1.text()) / 100) ** 2: .2f}")
        if float(self.IMT.text()) < 18.5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # настройка сообщения для окна сообщений
            msg.setText(" Дефицит массы тела ")

            # настройка заголовка окна сообщения
            msg.setWindowTitle("Information MessageBox")

            # объявление кнопок в окне сообщения
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            # запуск приложения
            retval = msg.exec_()


        elif not float(self.IMT.text()) < 18.5 and float(self.IMT.text()) <= 24.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText(" Нормальная масса тела ")

            msg.setWindowTitle("Information MessageBox")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = msg.exec_()


        elif 25 <= float(self.IMT.text()) <= 29.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText(" Увеличение массы тела ")

            msg.setWindowTitle("Information MessageBox")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = msg.exec_()


        elif 30 <= float(self.IMT.text()) <= 34.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText(" Ожирение 1 степени ")

            msg.setWindowTitle("Information MessageBox")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = msg.exec_()


        elif 35 <= float(self.IMT.text()) <= 39.9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText(" Ожирение 2 степени ")

            msg.setWindowTitle("Information MessageBox")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = msg.exec_()


        elif float(self.IMT.text()) >= 40:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText(" Ожирение 3 степени ")

            msg.setWindowTitle("Information MessageBox")

            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retval = msg.exec_()

    def window_B1(self):
        self.cams = Display()
        self.cams.show()
        self.close()


# Таблица с калорийностью продуктов
# Подсчет калорийности всех продуктов, которые выбрал пользователь
# Перевод калорийности продуктов в Кг человеческого жира
class CaloricContent(QMainWindow):
    """
    Таблица с калорийностью продуктов
    Подсчет калорийности всех продуктов, которые выбрал пользователь
    Перевод калорийности продуктов в Кг человеческого жира
    """

    def __init__(self):
        super().__init__()

        uic.loadUi('task3.ui', self)
        # Импортируем svg-файл с продуктами
        self.load_table('kalorii.csv')

        self.tableWidget.itemChanged.connect(self.update_check)
        self.setWindowTitle("Рацион калорий")

        # Создаем кнопку и задаем силь и размер и координаты
        self.pushButton1 = QPushButton(self)

        self.pushButton1.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : lightblue;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "}"
                                       )
        self.pushButton1.setText('Вернуться на главную')
        self.pushButton1.setGeometry(0, 520, 150, 36)
        self.pushButton1.clicked.connect(self.window_B2)

    # Чтение svg-файла, создание столбца для ввода пользователем кол-ва продукта
    # Заполнение всех строк столбца нулевым показателем
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

    # Подсчет всех данных пользователем
    # Перевод данных в калории
    # Перевод калорий в человеческий жир
    def update_check(self):
        price = [float(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
        count = [float(self.tableWidget.item(i, 2).text()) if self.tableWidget.item(i, 2).text() != ''
                 else 0 for i in range(self.tableWidget.rowCount())]
        sum_of = 0
        sum_gr = 0
        for i in range(len(price)):
            sum_of += price[i] * count[i] / 100
            sum_gr = sum_of / 7700
        self.lineEdit.setText(str(round(sum_of, 2)))
        self.lineEdit_2.setText(str(round(sum_gr, 2)))

    def window_B2(self):
        self.cams = Display()
        self.cams.show()
        self.close()



class Searching(QWidget):
    """
    Класс ищет в базе данных продукты, которые ввел пользователь
    Класс может найти продукты с нужным кол-вом калорий,
    которые ввел пользователь
    """
    def __init__(self):
        super().__init__()
        self.initUI()

        # Создаю кнопку, делаю ей размер
        self.pushButton1 = QPushButton(self)
        self.pushButton1.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : lightblue;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "}"
                                       )
        self.pushButton1.setText('Вернуться на главную')
        self.pushButton1.setGeometry(20, 295, 150, 36)
        self.pushButton1.clicked.connect(self.window_B3)

    # Создаю визуал
    def initUI(self):
        self.setWindowTitle("Рацион калорий")
        self.setFont(QFont('Arial', 10))
        self.calor = QLabel("Калории", self)
        self.calor_query = QLineEdit(self)
        self.calor.move(10, 10)
        self.calor_query.move(10, 55)
        self.calor.resize(250, 35)
        self.calor_query.resize(250, 35)

        self.product = QLabel("Продукт", self)
        self.product_query = QLineEdit(self)
        self.product.move(10, 100)
        self.product_query.move(10, 145)
        self.product.resize(250, 35)
        self.product_query.resize(250, 35)

        self.button = QPushButton("Пуск", self)
        self.button.clicked.connect(self.search)
        self.button.move(60, 200)
        self.button.resize(150, 40)

        self.table = QTableWidget(self)
        self.table.resize(660, 335)
        self.table.move(270, 10)
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(["Продукты", "Белки", "Жиры", "Углеводы", "Калории"])
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

    def search(self):
        con = sqlite3.connect("nutrients.db")
        cur = con.cursor()
        calories, product = self.calor_query.text(), self.product_query.text()
        query = ""
        if any((calories, product)):
            query = f"""WHERE {' AND '.join(el for el in (f'calories <= {calories}' if calories else "", 
                                             f'product LIKE "{product.lower().capitalize()[:-1]}%"' if product else "") if el)}"""
        result = cur.execute(f"""SELECT * FROM nutrients {query}""").fetchall()
        self.table.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, obj in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(obj)))
        self.table.resizeColumnsToContents()


    def window_B3(self):
        self.cams = Display()
        self.cams.show()
        self.close()


def exception_hook(cls, exception, traceback):
    sys.exception_hook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Display()
    w.show()
    sys.excepthook = exception_hook
    sys.exit(app.exec_())
