import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtGui import QIcon, QFontDatabase, QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt

import settings 

# I called the tabs
try:
    from tabs.stopwatch import StopwatchTab
    from tabs.timer import TimerTab
except ImportError as e:
    print("ERROR: Files or class names could not be found.", e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vecna's Clock App")
        self.setGeometry(430, 110, 1100, 800)

        if settings.ICON_PATH: 
            self.setWindowIcon(QIcon(settings.ICON_PATH))

        self.custom_font_name = "Arial"
        if settings.FONT_PATH:
            font_id = QFontDatabase.addApplicationFont(settings.FONT_PATH)
            if font_id != -1:
                self.custom_font_name = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.tabs.addTab(StopwatchTab(self.custom_font_name), "STOPWATCH")
        self.tabs.addTab(TimerTab(self.custom_font_name), "TIMER") 

        # CSS
        self.apply_styles()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#1e0707")) 

        if settings.BG_PATH:
            pixmap = QPixmap(settings.BG_PATH)
            if not pixmap.isNull():
                painter.setOpacity(0.4) 
                scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
                
                x = (self.width() - scaled_pixmap.width()) // 2
                y = (self.height() - scaled_pixmap.height()) // 2
                painter.drawPixmap(x, y, scaled_pixmap)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #1e0707; }
            
            QTabWidget::pane { 
                border: 0; 
                background: transparent;
            }
            
            QTabBar::tab {
                background: #1e193c;
                color: white;
                padding: 15px 20px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                margin-right: 5px;
                font-weight: bold;
                font-size: 22px;
                min-width: 250px;
            }
            QTabBar::tab:selected {
                background: #ff1515;
                color: white;
            }

            QLabel#time_display, QLabel#timer_display {
                color: white;
                background-color: #1e193c; 
                padding: 20px 40px;        
                margin: 40px;            
                border: 1.5px solid gray;   
                border-radius: 10px; 
            }

            QPushButton {
                color: white;
                padding: 20px 40px;
                margin: 20px;
                border: 1.5px solid gray;
                border-radius: 10px; 
                font-size: 18px;
                background-color: #1e193c; 
            }

            QPushButton#btn_start {
                background-color: #073e1e;
            }
            QPushButton#btn_start:hover {
                background-color: #0a5c2d; 
                border-color: #0a5c2d;
            }

            QPushButton#btn_stop {
                background-color: #3a5fe5;
            }
            QPushButton#btn_stop:hover {
                background-color: #5b7af0;
            }

            QPushButton#btn_reset, QPushButton#btn_cancel {
                background-color: #ff1515;
            }
            QPushButton#btn_reset:hover {
                background-color: #ff4d4d;
            }

            /* input boxes for timer */
            QSpinBox {
                background-color: #1e193c;
                color: white;
                border: 2px solid white;
                padding: 10px;
                border-radius: 10px;
                font-size: 20px;
                margin: 10px;
                min-width: 80px;
                min-height: 40px;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    