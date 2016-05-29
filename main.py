# eflag: FileType = Python3

from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow

def main():
    import sys
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()