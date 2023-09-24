from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel
from random import randint
app = QApplication([])
win = QWidget()
win.setWindowTitle('Хто переможець?')
win.resize(400, 200)
win.move(100, 100)

text = QLabel(win)
text.setText("Натисніть, щоб визначити переможця")
text.move(70, 10)

text2 = QLabel(win)
text2.setText('?')
text2.move(190, 70)

text3 = QLabel(win)
text3.setText('?')
text3.move(210, 70)

button = QPushButton(win)
button.setText("Згенерувати")
button.move(250, 70)


def show_win():
    number = randint(9,20)
    number1 = randint(1, 9)
    text2.setText(str(number))
    text3.setText(str(number1))
    text.setText('Переможець:')


button.clicked.connect(show_win)

win.show()
app.exec_()

