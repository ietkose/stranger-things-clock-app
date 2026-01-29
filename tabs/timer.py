from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

import settings 

class TimerTab(QWidget):
    def __init__(self, font_name):
        super().__init__()
        self.font_name = font_name
        self.total_seconds = 0
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def initUI(self):
        vbox = QVBoxLayout()

        # the biggest screen that shows remain time
        self.display_label = QLabel("00:00", self)
        self.display_label.setAlignment(Qt.AlignCenter)
        self.display_label.setObjectName("timer_display") # CSS için ID

        # for selecting duration
        input_layout = QHBoxLayout()
        
        # minute selector
        self.min_input = QSpinBox(self)
        self.min_input.setRange(0, 120) # max 120 minutes
        self.min_input.setValue(25)     # default Pomodoro time 
        self.min_input.setSuffix(" dk") 
        self.min_input.setObjectName("spin_input")

        # second selector
        self.sec_input = QSpinBox(self)
        self.sec_input.setRange(0, 59)
        self.sec_input.setSuffix(" sn")
        self.sec_input.setObjectName("spin_input")

        input_layout.addWidget(self.min_input)
        input_layout.addWidget(self.sec_input)

        # start / stop buttons
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Focus", self)
        self.start_btn.clicked.connect(self.start_timer)
        self.start_btn.setObjectName("btn_start")

        self.cancel_btn = QPushButton("Cancel", self)
        self.cancel_btn.clicked.connect(self.cancel_timer)
        self.cancel_btn.setObjectName("btn_cancel")

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.cancel_btn)

        # fit the screen
        vbox.addStretch()
        vbox.addWidget(self.display_label)
        vbox.addLayout(input_layout)
        vbox.addLayout(btn_layout)
        vbox.addStretch()

        self.setLayout(vbox)

        # font and stills
        if self.font_name:
            self.display_label.setFont(QFont(self.font_name, 70))
            self.start_btn.setFont(QFont(self.font_name, 20))
            self.cancel_btn.setFont(QFont(self.font_name, 20))
            self.min_input.setFont(QFont(self.font_name, 20))
            self.sec_input.setFont(QFont(self.font_name, 20))

    def start_timer(self):
        # if timer works already, stop it 
        if self.timer.isActive():
            self.timer.stop()
            self.start_btn.setText("Continue")
            return

        # if timer will start at the first time, set for start at 00:00
        if self.total_seconds == 0:
            minutes = self.min_input.value()
            seconds = self.sec_input.value()
            self.total_seconds = (minutes * 60) + seconds
        
        if self.total_seconds > 0:
            self.timer.start(1000) # work once per a second
            self.start_btn.setText("Pause")
            self.min_input.setEnabled(False) # do not let to change the duration
            self.sec_input.setEnabled(False)

    def cancel_timer(self):
        self.timer.stop()
        self.total_seconds = 0
        self.display_label.setText("00:00")
        self.display_label.setStyleSheet("color: #ff1515;") 
        self.start_btn.setText("Focus")
        self.min_input.setEnabled(True)
        self.sec_input.setEnabled(True)

    def update_timer(self):
        self.total_seconds -= 1

        # calculate the minutes and seconds
        m, s = divmod(self.total_seconds, 60)
        self.display_label.setText(f"{m:02d}:{s:02d}")

        if self.total_seconds <= 0:
            self.timer.stop()
            self.display_label.setText("Time is Over!")
            self.start_btn.setText("FOCUS")
            self.min_input.setEnabled(True)
            self.sec_input.setEnabled(True)
            
            QMessageBox.information(self, "Time is Up", "The lesson is over. You can exit through the Upside Down.")