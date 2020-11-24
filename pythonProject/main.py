import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.loadTable('Data.csv')

    def loadTable(self, table_name):
        data = [{
            'ID': 1,
            'SORT': 'Капучино',
            'LEVEL': 'Хорошо обжарено',
            'TIPE': 'Молотый',
            'TASTY': 'Карамельный',
            'PRICE': 30,
            'V': 10
        }, {
            'ID': 2,
            'SORT': 'Капучино',
            'LEVEL': 'Хорошо обжарено',
            'TIPE': 'Зерновой',
            'TASTY': 'С корицей',
            'PRICE': 67,
            'V': 15
        }, {
            'ID': 3,
            'SORT': 'Капучино',
            'LEVEL': 'Мало обжарено',
            'TIPE': 'Зерновой',
            'TASTY': 'С молоком',
            'PRICE': 50,
            'V': 13
        }]

        with open('dictwriter.csv', 'w', newline='') as f:
            writer = csv.DictWriter(
                f, fieldnames=list(data[0].keys()),
                delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in data:
                writer.writerow(d)

        with open('dictwriter.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())