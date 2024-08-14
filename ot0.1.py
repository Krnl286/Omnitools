import sys, os
from PyQt4 import QtGui, QtCore

class Toolbox(QtGui.QMainWindow):

    def __init__(self):
        super(Toolbox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('System Toolbox')
        self.setGeometry(100, 100, 300, 200)
        layout = QtGui.QVBoxLayout()
        self.addButton(layout, 'Open Command Prompt', self.openCmd)
        self.addButton(layout, 'Open MMC', self.openMMC)
        self.addButton(layout, 'Open Control Panel', self.openControlPanel)
        self.addButton(layout, 'Run Data/1.EXE', self.runExecutable)
        mainWidget = QtGui.QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

    def addButton(self, layout, text, slot):
        button = QtGui.QPushButton(text)
        button.clicked.connect(slot)
        layout.addWidget(button)

    def openCmd(self):
        os.system('start cmd')

    def openMMC(self):
        os.system('start mmc')

    def openControlPanel(self):
        os.system('control')

    def runExecutable(self):
        data_dir = 'Data'
        if not os.path.exists(data_dir):
            QtGui.QMessageBox.warning(self, 'Directory Not Found', ('Directory "{}" not found.').format(data_dir))
            return
        exe_path = os.path.join(data_dir, '1.EXE')
        if os.path.exists(exe_path):
            os.system(exe_path)
            QtGui.QMessageBox.information(self, 'Success', ('Executable "{}" successfully launched.').format(exe_path))
        else:
            QtGui.QMessageBox.warning(self, 'File Not Found', ('Executable file "{}" not found.').format(exe_path))


def main():
    app = QtGui.QApplication(sys.argv)
    tb = Toolbox()
    tb.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
