import sys
from PyQt5.QtWidgets import(
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        self.setGeometry(300,400,400,200)
        layout =QHBoxLayout()
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("center"),1)
        layout.addWidget(QPushButton("right"),2)

        self.setLayout(layout)
        print(self.children())
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())