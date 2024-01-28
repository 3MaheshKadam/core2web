import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main window")
        self.setGeometry(500, 300, 500, 300)

        self.mainLayout = QVBoxLayout(self)

        self.labelUI()

    def labelUI(self):
        self.label = QLabel("Hello Core2web")
        self.mainLayout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())
