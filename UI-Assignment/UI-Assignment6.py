import sys
from PyQt5.QtWidgets import QApplication , QWidget , QVBoxLayout , QRadioButton ,QLabel

class RadioBajao(QWidget):
    def __init__(self):
        super().__init__()

        self.radoiUI()

    def radoiUI(self):
            
        self.setWindowTitle("Radio btn app")
        self.setGeometry(500,250,500,400)


        layout =QVBoxLayout()

        self.rad1=QRadioButton("Python" ,self)
        self.rad2=QRadioButton("JAVA" ,self)
        self.rad3=QRadioButton("React" ,self)
        self.rad4=QRadioButton("mongo-DB" ,self)

        layout.addWidget(self.rad1)
        layout.addWidget(self.rad2)
        layout.addWidget(self.rad3)
        layout.addWidget(self.rad4)

        self.select_radi =QLabel("Select option :None" ,self)
        layout.addWidget(self.select_radi)

        self.rad1.toggled.connect(lambda:
                                    self.update_select_radi("python"))
        self.rad2.toggled.connect(lambda:
                                    self.update_select_radi("JAVA"))
            
        self.rad3.toggled.connect(lambda:
                                    self.update_select_radi("React"))
            
        self.rad4.toggled.connect(lambda:
                                    self.update_select_radi("mongo-DB"))
            
        self.setLayout(layout)


    def update_select_radi(self ,option):
        if option:
            self.select_radi.setText(f"Selected option is : {option}")

            
if __name__ =="__main__":
    app =QApplication(sys.argv)
    ow=RadioBajao()
    ow.show()
    # ow.radoiUI()
    sys.exit(app.exec_())








