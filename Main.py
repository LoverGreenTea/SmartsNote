from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()

main_line = QHBoxLayout()
v2 = QHBoxLayout()
v3 = QHBoxLayout()

test = QLabel("Hello World")
wikno = QTextEdit("")


list_notes_lbl = QLabel("Список Змінок")
text = QLabel("1")
notes_list = QListWidget()
create_note_btn = QPushButton("створити")
delet_note_btn = QPushButton("видалити")
save_note_btn = QPushButton("зберегти")

#:D Hello
text1 = QLabel("2")
wikno2 = QTextEdit("")
edittext = QLineEdit("")
create_note1_btn = QPushButton("створити")
delet_note1_btn = QPushButton("видалити")
save_note_btn1 = QPushButton("зберегти")



main_line.addWidget(wikno)

v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
main_line.addLayout(v1)
v2.addWidget(create_note_btn)
v2.addWidget(delet_note_btn)
v1.addLayout(v2)
v1.addWidget(save_note_btn)

v1.addWidget(wikno2)
v1.addWidget(edittext)
v1.addLayout(v3)
v3.addWidget(create_note1_btn)
v3.addWidget(delet_note1_btn)
v1.addWidget(save_note_btn1)


window.setLayout(main_line)
window.show()
app.exec()