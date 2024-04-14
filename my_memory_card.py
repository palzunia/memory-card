#создай приложение для запоминания информации

from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(
        self, question, right_answer, 
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

total = 0
right = 0
questions = []
questions.append(Question('В каком году был создан канал EdisonPTS?', 
                        '2013',
                        '2005',
                        '2011',
                        '2015'))
questions.append(Question('Какого моба дабавили в версии 1.20?',
                        'Варден', 
                        'Жёлтая корова', 
                        'Спрут', 
                        'Грибная корова'))
questions.append(Question('Сколько лет Heralegent в команде у Эда ?', 
                        '5', 
                        '3', 
                        '9', 
                        '7'))
questions.append(Question('Сколько лет назад была рубрика наконале EdisonPTS тролинг с Жекой ?', 
                        '6',
                        '3',
                        '7', 
                        '2'))
questions.append(Question('Сколько лет назад Chpunk ушёл из команды н.п. ?', 
                        '3',
                        '5',
                        '7',
                        '2'))
questions.append(Question('сколько лет я играю в Maincraft ?',
                        '7',
                        '10',
                        '5',
                        '3'))
questions.append(Question('Сколько лет назад был создан мир Боги майнкрафта у Эда ?',
                        '3',
                        '5',
                        '7',
                        '2'))
questions.append(Question('На сколько блоков уровень океана понизился на версии 1.13 ?',
                        'на 1',
                        'на 2',
                        'на 3',
                        'на 4'))
questions.append(Question('когда вышел официальный релиз Mainkraft ?',
                        '2011',
                        '2009',
                        '2013',
                        '2010'))

 
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(600, 300)
box = QGroupBox()
box_answer = QGroupBox()
layout_box = QVBoxLayout()
answer_text = QLabel('Прав ты или нет!')
layout_box.addWidget(answer_text, alignment=Qt.AlignCenter)
box_answer.setLayout(layout_box)
question = QLabel('В каком году был создан Mainkraft ?')
group_btn = QButtonGroup()
btn_answer1 = QRadioButton('2009')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2011')
btn_answer4 = QRadioButton('2005')
group_btn.addButton(btn_answer1)
group_btn.addButton(btn_answer2)
group_btn.addButton(btn_answer3)
group_btn.addButton(btn_answer4)
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutV1 = QVBoxLayout()
layoutV1.addLayout(layoutH2)
layoutV1.addLayout(layoutH3)
box.setLayout(layoutV1)
btn = QPushButton('Ответить')
layout_main.addLayout(layoutH1)
layout_main.addStretch(1)
layout_main.addWidget(box)
layout_main.addWidget(box_answer)
box_answer.hide()
layout_main.addStretch(1)
layout_main.addWidget(btn)
main_win.setLayout(layout_main)
 
def show_answer():
    box.hide()
    box_answer.show()
    btn.setText('Следующий вопрос')
    
def show_question():
    box.show()
    box_answer.hide()
    btn.setText('Ответить')
    group_btn.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    group_btn.setExclusive(True)
 
btn_list = [btn_answer1, btn_answer2,
            btn_answer3, btn_answer4]
def ask(q: Question):
    shuffle(btn_list)
    btn_list[0].setText(q.right_answer)
    btn_list[1].setText(q.wrong1)
    btn_list[2].setText(q.wrong2)
    btn_list[3].setText(q.wrong3)
    answer_text.setText(q.right_answer)
    question.setText(q.question)
    show_question()
 
def show_result(result):
    answer_text.setText(result)
    show_answer()
 
def check_answer():
    global right
    if btn_list[0].isChecked():
        show_result('Правильно!')
        right = right + 1

    else:
        if btn_list[1].isChecked() or btn_list[2].isChecked() or btn_list[3].isChecked():
            show_result('Неверно!')
current_q = 0
def next_question():
    global current_q, total
    current_q += 1
    total = total + 1
    print('Статистика/Statistic')
    print('Всего вопросов:',total)
    print('Правильных ответов:',right)
    print('рейтинг: ', (right/total)*100,'%')
    if current_q >= len(questions):
        current_q = 0
    q = questions[current_q]
    ask(q)
def change():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
 
btn.clicked.connect(change)
main_win.show()
app.exec_()
 