import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
'''
basic onclick event that changes text present a label
'''
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(500, 300, 500, 300)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

        self.label1 = QLabel("Hello from Mahesh")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFixedSize(500 ,30)
        self.mainLayout.addWidget(self.label1 , alignment=Qt.AlignmentFlag.AlignCenter)

        self.addButton()

    def addButton(self):
        self.Button1 = QPushButton("Text Change")
        self.Button1.clicked.connect(lambda:
                                     self.label1.setText("Hello from Sir" if self.label1.text() == "Hello from Mahesh" else "yeta ka kai zopa kadty"))
        self.mainLayout.addWidget(self.Button1, alignment=Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())
