import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QLineEdit , QHBoxLayout , QVBoxLayout , QLabel , QPushButton , QRadioButton , QStackedWidget , QWidget , QSpinBox
from PyQt5.QtCore import Qt , QTime , QTimer , QDate 
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import random
import pygame


class clock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.clock_label = QLabel("00:00:00 AP" , self)
        self.date_label = QLabel("DD:MM:YYYY")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        self.clock_UI()

    def clock_UI(self):
        vbox = QVBoxLayout()
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.clock_label)
        vbox.addWidget(self.date_label)
        self.setLayout(vbox)



        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.clock_label.setText(current_time)

        date = QDate.currentDate().toString("dd-MM-yyyy")
        self.date_label.setText(date)


    def resizeEvent(self, event):
        new_font_size = int(self.height() * 0.2) 
        self.clock_label.setStyleSheet(f"""
            font-size: {new_font_size}px;
            font-family: 'DejaVu Sans Mono', 'Monospace'; 
            font-weight: bold;
            color: #00FF00;
            margin-top:60px""")
        
        date_size = int(self.height() *0.1)
        self.date_label.setStyleSheet(f"""
            font-family:consolas;
            font-size : {date_size}px;
            color:lime;
            font-weight:bold;""")
        super().resizeEvent(event)





class alarm(QWidget):
    def __init__(self):
        super().__init__()
        self.alarm_label = QLabel("Alarm" , self)
        self.hour_input = QSpinBox()
        self.minute_input = QSpinBox()
        self.second_input = QSpinBox()
        self.set_button = QPushButton("Set Alarm")
        self.hour_label = QLabel("Hours" , self)
        self.minute_label = QLabel("Minutes" , self)
        self.second_label = QLabel("Seconds" , self)
        self.Question_label = QLabel("Question             " , self)
        self.answer_input = QLineEdit()
        self.submit_answer = QPushButton("Submit" , self)
        self.response_label = QLabel("")
        self.Alarm_UI()


    def Alarm_UI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.alarm_label)
        self.alarm_label.setAlignment(Qt.AlignHCenter)
        self.response_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.hour_label)
        hbox.addWidget(self.hour_input)
        hbox.addWidget(self.minute_label)
        hbox.addWidget(self.minute_input)
        hbox.addWidget(self.second_label)
        hbox.addWidget(self.second_input)


        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.Question_label)
        hbox2.addWidget(self.answer_input)
        hbox2.addWidget(self.submit_answer)
        self.submit_answer.setEnabled(False)
        self.answer_input.setEnabled(False)


        self.hour_label.setAlignment(Qt.AlignRight)
        self.minute_label.setAlignment(Qt.AlignRight)
        self.second_label.setAlignment(Qt.AlignRight)

        self.hour_input.setRange(0,23)
        self.minute_input.setRange(0,59)
        self.second_input.setRange(0,59)
    
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox)
        vbox2.addWidget(self.set_button)
        vbox.addLayout(vbox2)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.response_label)
        self.setLayout(vbox)


        self.set_button.clicked.connect(self.alarm_function)
        self.submit_answer.clicked.connect(self.stop_alarm)

    def question_function(self):
        first_number = random.randint(-99,99)
        second_number = random.randint(-99,99)
        while second_number == 0:
            second_number = random.randint(-99,99)
        option = ("+" , "-" , "*" , "/")
        sign = random.choice(option)
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

        question = f"{first_number} {sign} {second_number}"
        answer = ops[sign](first_number, second_number)
        answer = round(answer, 2)
        return question , answer


    def alarm_function(self):

        self.hours = str(self.hour_input.value()).zfill(2)
        self.minutes = str(self.minute_input.value()).zfill(2)
        self.seconds = str(self.second_input.value()).zfill(2) 

        self.set_button.setEnabled(False)
        alarm_time = f"{self.hours}:{self.minutes}:{self.seconds}"
        self.response_label.setText(f"Alarm set for {alarm_time}")
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.alarm_check)
        self.check_timer.start(1000)

        

    def alarm_check(self):    
        
        alarm_time = f"{self.hours}:{self.minutes}:{self.seconds}"
        current_time = QTime.currentTime().toString("hh:mm:ss")

        if current_time == alarm_time:
            self.check_timer.stop()
            self.ring_alarm()

    def ring_alarm(self):
        file = os.path.join(os.path.dirname(__file__), "tone.mp3")
        
        pygame.mixer.init()
        if os.path.exists(file):
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(loops=-1)

        question_text , self.correct_answer = self.question_function()

        self.Question_label.setText(f"what is {question_text}")

        self.answer_input.setEnabled(True)
        self.submit_answer.setEnabled(True)
        self.response_label.setText("Enter the answer upto 2 decimals")

    def stop_alarm(self):
        correct_answer = self.correct_answer
        user_answer = self.answer_input.text()

        try:
            if float(user_answer) == correct_answer:
                pygame.mixer.music.stop()
                self.response_label.setText("Correct answer !")
                self.answer_input.clear()
                self.hour_input.setValue(0)
                self.minute_input.setValue(0)
                self.second_input.setValue(0)
                self.set_button.setEnabled(True)
                self.answer_input.setEnabled(False)
                self.submit_answer.setEnabled(False)

            else:
                self.answer_input.clear()
        except ValueError:
            self.response_label.setText("Please Enter a Valid Anwswer !")

            

    def resizeEvent(self, event):
        label1_width = int(self.width() * 0.07)
        label2_width = int(self.width() * 0.0314)
        

        self.alarm_label.setStyleSheet(f"""
            font-family:consolas;
            font-size : {label1_width}px;
            color:lime;
            font-weight:bold;
            """)
        
        self.response_label.setStyleSheet(f"""
            font-family : DejaVu Sans;
            color : teal;
            font-weight : bold;
            font-size : {label2_width}px;
        """)

        self.set_button.setStyleSheet("""
            color : #03fc7f;
        """)

        self.Question_label.setStyleSheet("""
            color : #6bfc03;""")

        self.hour_label.setStyleSheet("""
            color:#0ecca0;""")
        
        self.minute_label.setStyleSheet("""
            color:#0ecca0;""")
        
        self.second_label.setStyleSheet("""
            color:#0ecca0;""")


        super().resizeEvent(event)

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.stopwatch_label = QLabel("00:00:00 .00" , self)
        self.time = QTime(0 , 0 , 0 , 0)
        self.timer = QTimer(self)
        self.start_button = QPushButton("Start" , self)
        self.stop_button = QPushButton("Stop" , self)
        self.reset_button = QPushButton("Reset" , self)
        self.Stopwatch_UI()


    def Stopwatch_UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addWidget(self.stopwatch_label)
        self.stopwatch_label.setAlignment(Qt.AlignCenter)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

        self.setStyleSheet("""
            QPushButton,QLabel{font-family:Sans;
                        font-weight:bold;
                        }
            QPushButton{font-size:40px;
                        color:#4dff00;
                        border:2px solid lime;
                        border-radius:20px;
                        text-align:center;
                        background-color:#1d5740;
                        }
            QPushButton:hover{background-color:0;}

        """)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0 , 0 , 0 , 0)
        self.stopwatch_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.stopwatch_label.setText(self.format_time(self.time))

    def resizeEvent(self, event):
        new_width = int(self.width() * 0.1)
        self.stopwatch_label.setStyleSheet(f"font-size : {new_width}px;color:lime;")

        super().resizeEvent(event)



class Countdown(QWidget):
    def __init__(self):
        super().__init__()
        self.Countdown_label = QLabel("HH:MM:SS" , self)
        self.hour_input = QSpinBox()
        self.minute_input = QSpinBox()
        self.second_input = QSpinBox()
        self.start_button = QPushButton("start" , self)
        self.pause_button = QPushButton("pause" , self)
        self.reset_button = QPushButton("reset" , self)
        self.hour_label = QLabel("Hours" , self)
        self.minute_label = QLabel("Minutes" , self)
        self.timer_color = "lime"
        self.second_label = QLabel("Seconds" , self)
        self.countdown_Ui()
        self.style_()

    def countdown_Ui(self):
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox.addWidget(self.pause_button)
        hbox.addWidget(self.reset_button)
        vbox2.addLayout(hbox3)
        vbox2.addLayout(hbox2)
        vbox2.addWidget(self.start_button)
        vbox2.addLayout(hbox)

        hbox2.addWidget(self.hour_input)
        hbox2.addWidget(self.minute_input)
        hbox2.addWidget(self.second_input)
        
        hbox3.addWidget(self.hour_label)
        hbox3.addWidget(self.minute_label)
        hbox3.addWidget(self.second_label)

        vbox.addWidget(self.Countdown_label)
        vbox.addLayout(vbox2)
        

        self.setLayout(vbox)

        self.minute_input.setRange(0,59)
        self.second_input.setRange(0,59)

        self.hour_label.setAlignment(Qt.AlignBottom)
        self.minute_label.setAlignment(Qt.AlignBottom)
        self.second_label.setAlignment(Qt.AlignBottom)

        self.Countdown_label.setAlignment(Qt.AlignCenter)

        self.pause_button.setEnabled(False)
        self.reset_button.setEnabled(False)

        self.start_button.clicked.connect(self.countdown_function)
        self.pause_button.clicked.connect(self.pause_countdown)
        self.reset_button.clicked.connect(self.reset_countdown)


    

    def countdown_function(self):
        self.timer = QTimer(self)
        
        hours = self.hour_input.value()
        minutes = self.minute_input.value()
        seconds = self.second_input.value()

        self.total_seconds = (hours * 3600) + (minutes * 60) + seconds

        if self.total_seconds > 0:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_countdown)
            self.timer.start(1000)

            self.start_button.setEnabled(False)
            self.hour_input.setEnabled(False)
            self.minute_input.setEnabled(False)
            self.second_input.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.reset_button.setEnabled(True)
            self.pause_button.setText("Pause")

    def update_countdown(self):
        if self.total_seconds > 0:
            self.total_seconds -= 1
            hours = self.total_seconds // 3600
            minutes = (self.total_seconds % 3600) // 60
            seconds = self.total_seconds % 60
            
            self.Countdown_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        else:
            self.timer.stop()
            self.Countdown_label.setText("00:00:00")
            self.Countdown_label.setStyleSheet("font-weight: bold;")
            self.start_button.setEnabled(True)
            self.timer_color = "red"
            self.update_label_style()

    def pause_countdown(self):
        button_text = self.pause_button.text()
        if button_text == "Pause":
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.pause_button.setText("Resume")
        else:
            self.timer.start()
            self.pause_button.setText("Pause")

    def reset_countdown(self):
        if hasattr(self, 'timer'):
            self.timer.stop()
        self.total_seconds = 0
        self.Countdown_label.setText("00:00:00")
        self.Countdown_label.setStyleSheet("color: lime;")
        self.start_button.setEnabled(True)
        self.hour_input.setEnabled(True)
        self.minute_input.setEnabled(True)
        self.second_input.setEnabled(True)
        self.hour_input.setValue(0)
        self.minute_input.setValue(0)
        self.second_input.setValue(0)
        self.timer_color = "lime"
        self.update_label_style()

    def resizeEvent(self,event):
        self.update_label_style()
        super().resizeEvent(event)


    def update_label_style(self):
        width = int(self.width() * 0.1)
        self.Countdown_label.setStyleSheet(f"""
            font-size: {width}px;
            color: {self.timer_color};
            font-weight: bold;
        """)


    def style_(self):
        self.start_button.setStyleSheet("color:#0be6d0 ; font-size:25px;")

        
        



class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChronoSentinel")
        self.initUI()
        self.style_()

    def initUI(self):
        self.setGeometry(350 , 400 , 500 , 500)

        self.clock_button = QRadioButton("Clock")
        self.Alarm_button = QRadioButton("Alarm")
        self.Stopwatch_button = QRadioButton("Stopwatch")
        self.Countdown_button = QRadioButton("Countdown")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        navigation = QHBoxLayout()

        navigation.addWidget(self.clock_button)
        navigation.addWidget(self.Alarm_button)
        navigation.addWidget(self.Stopwatch_button)
        navigation.addWidget(self.Countdown_button)
        main_layout.addLayout(navigation)

        self.pages = QStackedWidget()
        main_layout.addWidget(self.pages)

        self.page_clock = clock()
        self.page_alarm = alarm()
        self.page_stopwatch = Stopwatch()
        self.page_countdown = Countdown()

        self.pages.addWidget(self.page_clock)     
        self.pages.addWidget(self.page_alarm)     
        self.pages.addWidget(self.page_stopwatch) 
        self.pages.addWidget(self.page_countdown) 

        self.clock_button.toggled.connect(lambda: self.switch_page(0))
        self.Alarm_button.toggled.connect(lambda: self.switch_page(1))
        self.Stopwatch_button.toggled.connect(lambda: self.switch_page(2))
        self.Countdown_button.toggled.connect(lambda: self.switch_page(3))

        self.clock_button.setChecked(True)

    def switch_page(self, index):
        if self.sender().isChecked():
            self.pages.setCurrentIndex(index)

    def style_(self):
        self.clock_button.setStyleSheet("border:2px solid #0990d9 ; border-radius:5px ; font-size: 20px;font:Arial; font-weight:bold; color:#ebc805;")
        self.Alarm_button.setStyleSheet("border:2px solid #0990d9 ; border-radius:5px ; font-size: 20px;font:Arial; font-weight:bold; color:#ebc805")
        self.Stopwatch_button.setStyleSheet("border:2px solid #0990d9 ; border-radius:5px ; font-size: 20px;font:Arial; font-weight:bold; color:#ebc805")
        self.Countdown_button.setStyleSheet("border:2px solid #0990d9 ; border-radius:5px ; font-size: 20px;font:Arial; font-weight:bold; color:#ebc805")
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())