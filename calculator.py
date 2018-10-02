from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys
import time
def button0_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=0
        mainlabel.setText(str(first_number))
        
    else:
        second_number*=10
        second_number+=0
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button1_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=1
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=1
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button2_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=2
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=2
        mainlabel.setText(str(first_number)+znak+str(second_number))


def button3_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=3
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=3
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button4_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=4
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=4
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button5_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=5
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=5
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button6_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=6
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=6
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button7_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=7
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=7
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button8_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=8
        mainlabel.setText(str(first_number))
        
    else:
        second_number*=10
        second_number+=8
        mainlabel.setText(str(first_number)+znak+str(second_number))

def button9_clicked():
    global first_number
    global second_number
    global free
    global mainlabel
    if free==0:
        first_number*=10
        first_number+=9
        mainlabel.setText(str(first_number))
    else:
        second_number*=10
        second_number+=9
        mainlabel.setText(str(first_number)+znak+str(second_number))

def buttonplus_clicked():
    global first_number
    global second_number
    global free
    global znak
    global mainlabel
    
    free+=1
    znak='+'
    

def buttonminus_clicked():
    global first_number
    global second_number
    global free
    global znak
    global mainlabel
    
    free+=1
    znak='-'

def buttondelete_clicked():
    global first_number
    global second_number
    global free
    global znak
    global mainlabel
    
    free+=1
    znak='/'

def buttonumno_clicked():
    global first_number
    global second_number
    global free
    global znak
    global mainlabel
    
    free+=1
    znak='*'

def buttonravno_clicked():
    global first_number
    global second_number
    global znak
    global mainlabel
    summa=0
    

    if znak=='+':
        summa=first_number+second_number
    if znak=='-':
        summa=first_number-second_number
    if znak=='*':
        summa=first_number*second_number
    if znak=='/':
        summa=first_number/second_number
    mainlabel.setText(str(first_number)+znak+str(second_number)+'='+str(summa))
def buttonudalit_clicked():
    global first_number
    global second_number
    global znak
    global mainlabel
    global free
    first_number=0
    second_number=0
    free=0
    mainlabel.setText('0')
    
    
    
    

app = QApplication([])
window = QWidget()
window.resize(400, 300)
layout = QVBoxLayout()
app.setStyleSheet("QLabel { margin: 10ex; }")
button0 = QPushButton('0')
button1 = QPushButton('1')
mainlabel=QLabel('ty luchshiy')
layout.addWidget(mainlabel)
layout.addWidget(button0)
layout.addWidget(button1)

button2 = QPushButton('2')
button3 = QPushButton('3')
layout.addWidget(button2)
layout.addWidget(button3)

button4 = QPushButton('4')
button5 = QPushButton('5')
layout.addWidget(button4)
layout.addWidget(button5)

button6 = QPushButton('6')
button7 = QPushButton('7')
layout.addWidget(button6)
layout.addWidget(button7)

button8 = QPushButton('8')
button9 = QPushButton('9')
layout.addWidget(button8)
layout.addWidget(button9)
window.setLayout(layout)

buttonplus = QPushButton('+')
buttonminus = QPushButton('-')
layout.addWidget(buttonplus)
layout.addWidget(buttonminus)
window.setLayout(layout)

buttondelete = QPushButton('/')
buttonumno = QPushButton('*')
buttonravno = QPushButton('=')
buttonudalit = QPushButton('delete')
layout.addWidget(buttondelete)
layout.addWidget(buttonumno)
layout.addWidget(buttonravno)
layout.addWidget(buttonudalit)
window.setLayout(layout)



first_number=0
second_number=0
free=0
znak=0



button1.clicked.connect(button1_clicked)
button2.clicked.connect(button2_clicked)
button3.clicked.connect(button3_clicked)
button4.clicked.connect(button4_clicked)
button5.clicked.connect(button5_clicked)
button6.clicked.connect(button6_clicked)
button7.clicked.connect(button7_clicked)
button8.clicked.connect(button8_clicked)
button9.clicked.connect(button9_clicked)
button0.clicked.connect(button0_clicked)

buttonplus.clicked.connect(buttonplus_clicked)
buttonminus.clicked.connect(buttonminus_clicked)
buttondelete.clicked.connect(buttondelete_clicked)
buttonumno.clicked.connect(buttonumno_clicked)
buttonravno.clicked.connect(buttonravno_clicked)
buttonudalit.clicked.connect(buttonudalit_clicked)


window.show()
app.exec_()
print (first_number)




