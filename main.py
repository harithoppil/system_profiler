import sys
import subprocess
from PyQt6 import QtWidgets, QtCore

class SystemProfiler(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('System Profiler')

        self.textEdit = QtWidgets.QTextEdit(self)
        self.runButton = QtWidgets.QPushButton('Run', self)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.textEdit)
        vbox.addWidget(self.runButton)

        self.runButton.clicked.connect(self.run_profiler)

    def run_profiler(self):
        cmd = ['system_profiler']
        result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        self.textEdit.setText(result.stdout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = SystemProfiler()
    ex.show()
    sys.exit(app.exec())
