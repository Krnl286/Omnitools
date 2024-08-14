import sys, os, subprocess, ctypes
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt4 import QtCore

def check_apps_exist():
    for num in range(1, 16):
        exe_path = ('Data/{}/{}.EXE').format(num, num)
        if not os.path.exists(exe_path):
            return False

    return True


class ApplicationLauncher:

    def __init__(self, parent=None):
        self.parent = parent

    def start_control_panel(self):
        self.parent.show_status_message(u'\u0x542f0x52a80x63a70x52360x97620x677f...')
        if self.parent.check_admin():
            self.check_control_panel()

    def check_control_panel(self):
        try:
            subprocess.Popen([os.path.join(os.environ['SystemRoot'], 'System32', 'control.exe')])
            self.parent.show_status_message(u'\u0x52a80x63a70x52360x97620x677f')
        except Exception as e:
            self.parent.show_status_message((u'\u0x63a70x52360x97620x677f0x59310x8d250xff1a{}').format(str(e)))

    def start_mmc(self):
        self.parent.show_status_message(u'\u0x542f0x52a8MMC...')
        if self.parent.check_admin():
            self.check_mmc()

    def check_mmc(self):
        try:
            mmc_path = os.path.join(os.environ['SystemRoot'], 'System32', 'mmc.exe')
            subprocess.Popen([mmc_path])
            self.parent.show_status_message(u'\u0x52a8MMC')
        except Exception as e:
            self.parent.show_status_message((u'\uMMC0x59310x8d250xff1a{}').format(str(e)))

    def start_application(self, num):
        self.parent.show_status_message(u'\u0x542f0x52a80x7a0b0x5e8f...')
        if self.parent.check_admin():
            self.start_custom_exe(num)

    def start_custom_exe(self, num):
        exe_path = ('Data/{}/{}.EXE').format(num, num)
        if not os.path.exists(exe_path):
            QMessageBox.critical(self.parent, u'\u', (u'\u0x7a0b0x5e8f {} 0x4e0d0x5b580x5728').format(exe_path))
            return
        try:
            subprocess.Popen([exe_path])
            self.parent.show_status_message((u'\u0x52a8 {}').format(exe_path))
        except Exception as e:
            self.parent.show_status_message((u'\u0x5e940x75280x7a0b0x5e8f0x59310x8d250xff1a{}').format(str(e)))


class Toolbox(QWidget):

    def __init__(self):
        super(Toolbox, self).__init__()
        self.initUI()
        self.application_launcher = ApplicationLauncher(self)

    def initUI(self):
        self.setWindowTitle(u'OmniTools')
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)
        self.control_panel_button = QPushButton(u'\u0x63a70x52360x97620x677f', self)
        self.control_panel_button.clicked.connect(self.start_control_panel)
        self.mmc_button = QPushButton(u'\uMMC', self)
        self.mmc_button.clicked.connect(self.start_mmc)
        self.status_label = QLabel(u'\u', self)
        self.input_label = QLabel(u'\u0x53c20x65700xff081 0x5230 150xff09:', self)
        self.input_text = QLineEdit(self)
        self.input_text.setFixedWidth(50)
        self.confirm_button = QPushButton(u'\u', self)
        self.confirm_button.clicked.connect(self.start_custom_exe)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_text)
        input_layout.addWidget(self.confirm_button)
        exit_button = QPushButton(u'\u', self)
        exit_button.clicked.connect(self.close)
        vbox = QVBoxLayout()
        vbox.addWidget(self.control_panel_button)
        vbox.addWidget(self.mmc_button)
        vbox.addWidget(self.status_label)
        vbox.addLayout(input_layout)
        vbox.addWidget(exit_button)
        self.setLayout(vbox)
        self.show()

    def start_control_panel(self):
        if self.check_admin():
            self.application_launcher.start_control_panel()
        else:
            QMessageBox.critical(self, u'\u', u'\u0x7ba10x74060x54580x67430x96500x67650x8fd00x884c0x6b640x5e940x75280x7a0b0x5e8f')

    def start_mmc(self):
        if self.check_admin():
            self.application_launcher.start_mmc()
        else:
            QMessageBox.critical(self, u'\u', u'\u0x7ba10x74060x54580x67430x96500x67650x8fd00x884c0x6b640x5e940x75280x7a0b0x5e8f')

    def start_custom_exe(self):
        param = unicode(self.input_text.text())
        if not param.isdigit():
            QMessageBox.critical(self, u'\u', u'\u0x51650x65700x5b57')
            return
        num = int(param)
        if num < 1 or num > 15:
            QMessageBox.critical(self, u'\u', u'\u0x516510x5230150x4e4b0x95f40x76840x65700x5b57')
            return
        if self.check_admin():
            self.application_launcher.start_application(num)
        else:
            QMessageBox.critical(self, u'\u', u'\u0x7ba10x74060x54580x67430x96500x67650x8fd00x884c0x6b640x5e940x75280x7a0b0x5e8f')

    def check_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False

    def set_status_text(self, text):
        self.status_label.setText(text)

    def show_status_message(self, text):
        self.status_label.setText(text)


if __name__ == '__main__':
    if not check_apps_exist():
        QMessageBox.critical(None, u'\u', u'\u0x7a0b0x5e8f0x65870x4ef60x4e0d0x5b580x57280xff0c0x8bf70x68c00x67e5 Data 0x76ee0x5f550x4e0b0x76840x65870x4ef6!')
        sys.exit(1)
    app = QApplication(sys.argv)
    ex = Toolbox()
    sys.exit(app.exec_())
