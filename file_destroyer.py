from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_file():
    global filenames
    filenames,_ = QFileDialog.getOpenFileName(window,'Select files')
    print (filenames)
    

def destroy_file():
    for filename in filenames:
        path = Path(filename)
        with open(path,'wb')as file:
            file.write(b'')
        path.unlink()

app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destoyer')

layout = QVBoxLayout()

descrption = QLabel('Select the file you want permentaly want to destroy. The files will be <font color="red">permenatly</font> deleted')
layout.addWidget(descrption)

open_button = QPushButton('Open file')
open_button.setToolTip('Open file')
open_button.setFixedWidth(100)
layout.addWidget(open_button,alignment=Qt.AlignmentFlag.AlignCenter)
open_button.clicked.connect(open_file)

destroy_button = QPushButton('Destroy file')
destroy_button.setFixedWidth(100)
layout.addWidget(destroy_button,alignment=Qt.AlignmentFlag.AlignCenter)
destroy_button.clicked.connect(destroy_file)

window.setLayout(layout)
window.show()
app.exec()