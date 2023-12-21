###########################################################
#     _              _ ____  _ _           __  __         #
#    / \   _ __   __| / ___|(_) | ___ _ __ \ \/ /___ _ __ #
#   / _ \ | '_ \ / _` \___ \| | |/ _ \ '_ \ \  // _ \ '__|#
#  / ___ \| | | | (_| |___) | | |  __/ | | |/  \  __/ |   #
# /_/   \_\_| |_|\__,_|____/|_|_|\___|_| |_/_/\_\___|_|   #
###########################################################
############### 2023/12/20 ######### Build 1.0 ############                                        
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class OverlayApp(QWidget):
    def __init__(self):
        super().__init__()

        # OVERLAY
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SIZE OVERLAY
        self.setGeometry(QApplication.desktop().screenGeometry())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # LINES CONFIGURATION
        pen = QPen(Qt.white)
        pen.setWidth(2)
        painter.setPen(pen)

        # HORIZONTAL LINES
        for i in range(1, 3):
            y = i * self.height() // 3
            painter.drawLine(0, y, self.width(), y)

        # VERTICAL LINES
        for i in range(1, 3):
            x = i * self.width() // 3
            painter.drawLine(x, 0, x, self.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayApp()
    overlay.show()
    sys.exit(app.exec_())
