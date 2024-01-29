import sys
from PyQt5.QtWidgets import QApplication , QWidget , QVBoxLayout , QSlider ,QLabel
from PyQt5.QtCore import Qt

class slider(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("silder app")
        self.setGeometry(500 ,300,300,200)

        layout =QVBoxLayout()

        self.slider =QSlider(Qt.Horizontal,self)
        layout.addWidget(self.slider)

        self.label =QLabel("slider value : 0",self)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.slider.valueChanged.connect(self.update_label)  # Connect the valueChanged signal
        self.setLayout(layout)

    def update_label(self):
        value= self.slider.value()
        self.label.setText(f"slider valuu is : {value}")

if __name__ =="__main__":
    app =QApplication(sys.argv)
    ow=slider()
    ow.show()
    # ow.radoiUI()
    sys.exit(app.exec_())