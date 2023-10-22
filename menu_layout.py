from PyQt5.QtCorei import *
from PyQt5.QtWidgets import *

txt_question = QLineEdit()
txt_answer = QLineEdit()
txt_wrong1 = QLineEdit()
txt_wrong2 = QLineEdit()
txt_wrong3 = QLineEdit()

form_layout = QFormLayout()


form_layout.addRow('Вопрос:',txt_question)
from_layout.addRow("Ответ:", txt_answer)
form_layout.addRow("Неправільній 1:", txt_wrong1)
form_layout.addRow("Неправільній 2:", txt_wrong2)
form_layout.addRow("Неправільній 3:", txt_wrong3)