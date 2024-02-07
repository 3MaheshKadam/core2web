import sys
from PyQt5 import QtWidgets ,QtGui ,QtCore
from PyQt5.QtCore import Qt

'''
NotImplementedError: QAbstractTableModel.rowCount() is abstract and must be overridden

note : 
In Python, whether you call a method within the arguments of __init__ 
or in the body of __init__ depends on the design and requirements of your class.
 Both approaches are valid, but they serve different purposes.

Calling in Arguments:

If a method is meant to initialize an attribute or perform some essential
 setup for the class instance, it is common to pass the necessary values as
arguments to __init__ and call the method within the arguments.
This ensures that the method is called during object creation, and any required setup is done right away.

class MyClass:
    def __init__(self, value):
        self.initialize(value)

    def initialize(self, value):
        # Do some initialization with the provided value
        self._data = value

        

Calling in Body:
If a method is optional and doesn't directly affect the initialization
 or setup of the object, you can call it in the body of __init__. This
 can be useful for organizing your code or making certain functionalities available to be called later.

Example:
class MyClass:
    def __init__(self, value):
        self._data = value
        self.setup()

    def setup(self):
        # Perform additional setup or optional initialization
        pass

        
# 3rd way is calling by obj.methoName  
'''
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [4, 9, 2],
            [4, 9, 2],
            [4, 9, 2],
            [4, 9, 2],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
