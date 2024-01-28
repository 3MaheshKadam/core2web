# import sys
# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
# from PyQt5.QtCore import Qt

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Main window")
#         self.setGeometry(500, 300, 500, 300)

#         self.mainLayout = QVBoxLayout(self)

#         self.labelUI()
#         self.addButton()


#     def labelUI(self):
#         self.label = QLabel("Enter your name")
#         self.mainLayout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)


#     def addButton(self):
#         self.Button1 = QPushButton("Submit..")
#         # self.Button1.clicked.connect(lambda:
#         #                              self.label1.setText("Hello from Sir" if self.label1.text() == "Hello from Mahesh" else "yeta ka kai zopa kadty"))
#         self.mainLayout.addWidget(self.Button1, alignment=Qt.AlignCenter)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_Window = MainWindow()
#     main_Window.show()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Field Example")
        self.setGeometry(500, 100, 400, 200)

        # Create the main layout
        main_layout = QVBoxLayout()

        # Create the input field
        self.input_field = QLineEdit(self)
        main_layout.addWidget(self.input_field)

        # Create the submit button
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.show_prompt)
        main_layout.addWidget(submit_button)

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def show_prompt(self):
        input_text = self.input_field.text()
        QMessageBox.information(self, "Prompt", f"You submitted: {input_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
