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
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QEvent, QRect, QSize

class OverlayApp(QWidget):
    def __init__(self):
        super().__init__()

        # OVERLAY
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SIZE OVERLAY
        self.setGeometry(QApplication.desktop().screenGeometry())

        # OVERLAY VISIBILITY PARAMETERS / FLAGS
        self.overlay_visible = True
        self.draw_lines = True

        # WATERMARK IMAGE
        self.watermark_image = QPixmap("watermark.png")

        # SET SIZE IMAGE HERE
        self.watermark_size = QSize(100, 100)
        # SET MARGIN IMAGE HERE
        self.watermark_margin = 80

    # METHOD TO DRAW LINES
    def paintEvent(self, event):
        if self.overlay_visible:
            # LINES
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            if self.draw_lines:
                pen = QPen(Qt.white)
                pen.setWidth(2)
                painter.setPen(pen)

                for i in range(1, 3):
                    y = i * self.height() // 3
                    painter.drawLine(0, y, self.width(), y)

                for i in range(1, 3):
                    x = i * self.width() // 3
                    painter.drawLine(x, 0, x, self.height())

            # WATERMARK
            watermark_rect = QRect(self.width() - self.watermark_size.width() - self.watermark_margin,
                                   self.height() - self.watermark_size.height() - self.watermark_margin,
                                   self.watermark_size.width(),
                                   self.watermark_size.height())
            painter.drawPixmap(watermark_rect, self.watermark_image.scaled(self.watermark_size, Qt.KeepAspectRatio))

    # KEY PRESS EVENTS
    def keyPressEvent(self, event):
        # ESCAPE BUTTON
        if event.key() == Qt.Key_Escape:
            self.close()
        # DRAW
        elif event.key() == Qt.Key_O and event.modifiers() == Qt.ControlModifier:
            self.draw_lines = True
            self.update()
        # HIDE
        elif event.key() == Qt.Key_P and event.modifiers() == Qt.ControlModifier:
            self.draw_lines = False
            self.update()

    # EVENT HANDLER METHOD
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_O:
                self.draw_lines = True
                self.update()
                return False
            elif event.key() == Qt.Key_P:
                self.draw_lines = False
                self.update()
                return False

        return super().eventFilter(obj, event)

# INITIATION
if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayApp()
    app.installEventFilter(overlay)
    overlay.show()
    
    # JUST IN CASE ANY ERRORS SHOW UP....
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An exception occurred: {e}")
