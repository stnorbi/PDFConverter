from PySide.QtGui import QApplication, QWidget, QLayout, QHBoxLayout, QVBoxLayout,QMainWindow, QIcon
import sys
from Utilities import fileUtils


class PDFConverter(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Contract Converter v1.0")
        self.setWindowIcon(QIcon(fileUtils.getIcon()["barIcon"]))
        self.resize(1350, 900)

        centralWidget = QWidget()
        centralWidget.setLayout(QVBoxLayout())
        centralWidget.layout().setContentsMargins(0,0,0,0)
        self.setCentralWidget(centralWidget)

        viewLayout = QHBoxLayout()
        centralWidget.layout().addLayout(viewLayout)


        # TODO:keszits 2 inner layout-ot a viewlayout-nak







app = QApplication(sys.argv)
window = PDFConverter()
window.show()
app.exec_()