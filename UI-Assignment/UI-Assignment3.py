import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow , QMenuBar , QAction ,QMessageBox
"""
task 1 : recall use of argv in arguments
task 2 : write a code to call a fun in other fun 
         before its decleration
"""
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyqt menu bar ")
        self.setGeometry(500 ,100,500,300)

        # self.create_menus()

    def create_menus(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        
        open_action =QAction("open" ,self)
        open_action.triggered.connect(self.show_message_open)
        file_menu.addAction(open_action)


        exit_action =QAction("Exit",self)
        exit_action.triggered.connect(self.show_message_exit)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")
        
        cut_action =QAction("Cut",self)
        cut_action.triggered.connect(self.show_message_cut)
        edit_menu.addAction(cut_action)




        file_menu = menubar.addMenu("copy")
        copy_action =QAction("Copy",self)
        copy_action.triggered.connect(self.show_message_copy)
        edit_menu.addAction(copy_action)

    def show_message_open(self):
        QMessageBox.information(self ,"open Action" ,"open action trigged")


    def show_message_exit(self):
        QMessageBox.information(self ,"exit Action" ,"exit action trigged")


    def show_message_cut(self):
        QMessageBox.information(self ,"cut Action" ,"cut action trigged")


    def show_message_copy(self):
        QMessageBox.information(self ,"copy Action" ,"copy action trigged")



if __name__ =="__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()

    main_window.create_menus()


    sys.exit(app.exec_())



