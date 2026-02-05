import sys
from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QLabel
from PyQt5.QtCore import Qt , QTimer , QTime
from PyQt5.QtGui import QFontDatabase , QFont

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.time_label = QLabel("Dhruv" , self)
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('DIgital clock')
        self.setGeometry(400 , 350 , 300 , 100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:100px;"
                                    "color: green")

        font_id = QFontDatabase.addApplicationFont("python/Technology-Bold.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family , 100)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.setLayout(vbox)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())