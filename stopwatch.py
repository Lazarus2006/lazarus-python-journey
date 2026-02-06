import sys
from PyQt5.QtWidgets import QWidget  , QApplication , QLabel , QPushButton , QVBoxLayout , QHBoxLayout
from PyQt5.QtCore import Qt , QTimer , QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("stopwatch")
        self.time = QTime(0 , 0 , 0 , 0)
        self.time_label = QLabel("00:00:00.00" , self)
        self.start_button = QPushButton("Start" , self)
        self.stop_button = QPushButton("Stop" , self)
        self.reset_button = QPushButton("Reset" , self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)


        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        

        self.setStyleSheet("""
            QPushButton,QLabel{font-family:calibri;
                        font-weight:bold;
                        }
            QPushButton{font-size:40px;
                        color:#0718db;
                        border:2px solid lime;
                        border-radius:20px;
                        text-align:center;
                        background-color:teal;
                        }
            QLabel{font-size:100px;
                        }
            QPushButton:hover{background-color:0;}

        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0 , 0 , 0 , 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())