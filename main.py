# ***********************import all module*********************

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# **************************call gui class*********************


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 350, 200)
        self.setWindowTitle('BMI Calculator')
        self.setWindowIcon(QIcon('./unnamed.png'))
        # ******************create layout**********************
        self.boxlayout = QVBoxLayout()
        # *****************add font from file***************
        QFontDatabase().addApplicationFont('./font.ttf')

        self.boxlayout.addWidget(
            QLabel(
                text='BMI Calculator',
                alignment=Qt.AlignHCenter,
                font=QFont(
                    'Victor Mono Medium',
                    pointSize=20,
                    italic=False
                )
            ),
            stretch=0
        )
        self.boxlayout.addWidget(
            QLabel(
                text='Weight(KG)',
                font=QFont(
                    'victor mono',
                    pointSize=15,
                    italic=True
                )
            ),
            stretch=0
        )

        self.weight = QLineEdit()
        self.weight.textChanged.connect(lambda: cheack())
        self.boxlayout.addWidget(self.weight, 5)
        self.boxlayout.addWidget(
            QLabel(
                text='Height(FT)',
                font=QFont(
                    'victor mono',
                    pointSize=15,
                    italic=True
                )
            ),
            stretch=0
        )

        self.height = QLineEdit()
        self.height.textChanged.connect(lambda: cheack())
        self.boxlayout.addWidget(self.height, 5)
        self.button = QPushButton(
            text='Start',
            font=QFont(
                'victor mono',
                pointSize=15,
                italic=True
            )
        )
        self.button.clicked.connect(
            lambda: all_func(
                self.weight.text(), self.height.text()
            )
        )
        self.button.setDisabled(True)
        # ********************button disable func********************

        def cheack():
            if self.weight.text() != '' and self.height.text() != '':
                self.button.setDisabled(False)

            else:
                self.button.setDisabled(True)

        self.boxlayout.addWidget(self.button, 0)
        global result
        result = QLabel(
            font=QFont(
                'victor mono',
                pointSize=15,
                italic=True
            )
        )
        result.setText(f'Result :')

        self.boxlayout.addWidget(result, 0)
        self.setLayout(self.boxlayout)

# ************ all process func*************************


class all_func():

    def __init__(self, weight, height):

        # ********weight & height values (int to float) or(float to int)*****

        if weight.__len__() > 1 or height.__len__() > 1:

            self.w = float(weight)

            self.h = float(height) * 0.3048

        else:
            self.w = int(weight)

            self.h = int(height) * 0.3048
        # **************bmi claculation****************
        bmi = self.w / (self.h * self.h)

        # *****************show results***********
        if bmi < 18.5:
            result.setText(f'Result : {str(bmi)[:5]} (Under Weight)')
        elif bmi > 18.5 and bmi <= 25:
            result.setText(f'Result : {str(bmi)[:5]} (Normal)')
        elif bmi > 25 and bmi <= 30:
            result.setText(f'Result : {str(bmi)[:5]} (Over Weight)')
        elif bmi > 30:
            result.setText(f'Result : {str(bmi)[:5]} (Obese)')


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # ***************call gui class****************
    win = MainWin()
    win.show()

    # ******************** exit app *********************
    sys.exit(
        app.exec_()
    )
