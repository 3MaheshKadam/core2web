import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QHBoxLayout, QComboBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Window')
        self.setGeometry(250, 300, 400, 450 ) 
        self.setStyleSheet("background-color: skyblue;")

        label = QLabel('Hello Core2web',self)
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)

        change_button = QPushButton('Text Change')
        change_button.clicked.connect(self.on_change_button_clicked)
        change_button.setStyleSheet("font-size:16px")

        python_radio = QRadioButton('Python')
        java_radio = QRadioButton('Java')
        cpp_radio = QRadioButton('C++')

        python_radio.setStyleSheet("font-size: 14px;")
        java_radio.setStyleSheet("font-size: 14px;")
        cpp_radio.setStyleSheet("font-size: 14px;")

        color_combobox = QComboBox(self)
        color_combobox.addItem("Blue")
        color_combobox.addItem("Red")
        color_combobox.addItem("Green")
        color_combobox.addItem("Yellow")
        color_combobox.addItem("Orange")

        color_combobox.setFixedWidth(600)
        color_combobox.setFixedHeight(30)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        
        layout.addSpacing(10)
        layout.addWidget(change_button, alignment=Qt.AlignCenter)

        layout.addSpacing(10)

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(python_radio)
        radio_layout.addWidget(java_radio)
        radio_layout.addWidget(cpp_radio)
        layout.addLayout(radio_layout)

        layout.addSpacing(10)

        layout.addWidget(color_combobox, alignment=Qt.AlignCenter)

        layout.addStretch()

        layout.addSpacing(10)

    def on_change_button_clicked(self):
        print("Test Change button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
