import sys, os
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget
from main_window import Ui_mainwindow
from pars import get_data
basedir = os.path.dirname(__file__)
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.mainform = Ui_mainwindow()
        self.mainform.setupUi(self)
        
        self.mainform.btn_1.clicked.connect(self.update_data)

    def update_data(self):
        data = get_data()
        self.mainform.num_1.setText(f"Я на {data[0][1]} месте из {data[0][2]} участников")
        self.mainform.num_2.setText(f"Я на {data[1][1]} месте из {data[1][2]} участников")
        self.mainform.num_3.setText(f"Я на {data[2][1]} месте из {data[2][2]} участников")
        if len(data) != 4:
            self.mainform.num_4.setText(f"Меня ещё нет в списках :(")            
        elif len(data) == 4:
            self.mainform.num_4.setText(f"Я на {data[3][1]} месте из {data[3][2]} участников")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Main()
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
    login_window.show()
    sys.exit(app.exec())

# pyinstaller --windowed --icon=icon.ico app.py