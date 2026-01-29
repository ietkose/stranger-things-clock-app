from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

# we will use the features from settings class
import settings 

class StopwatchTab(QWidget):
    def __init__(self, font_name):
        super().__init__()
        self.time = QTime(0, 0, 0)
        self.font_name = font_name
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)

    def initUI(self):
        vbox = QVBoxLayout()
        self.time_label = QLabel("00 : 00 : 00", self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setObjectName("time_display")

        hbox = QHBoxLayout()
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        
        # object names for css
        self.start_button.setObjectName("btn_start")
        self.stop_button.setObjectName("btn_stop")
        self.reset_button.setObjectName("btn_reset")

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addStretch()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        vbox.addStretch()
        
        self.setLayout(vbox)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        if self.font_name:
            self.time_label.setFont(QFont(self.font_name, 60))
            btn_font = QFont(self.font_name, 20)
            self.start_button.setFont(btn_font)
            self.stop_button.setFont(btn_font)
            self.reset_button.setFont(btn_font)

    def start(self): self.timer.start(10)
    def stop(self): self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.time_label.setText("00 : 00 : 00")
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time.toString("hh : mm : ss"))