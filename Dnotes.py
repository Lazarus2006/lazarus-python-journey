from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit , QMainWindow , QListWidget , QLineEdit, QListWidgetItem , QHBoxLayout
from PyQt5.QtCore import Qt
import sys
import json , os


DARK_STYLE = """
    QMainWindow { background-color: #1b292c; }
    QLabel { color: #ffffff; font-size: 18px; }
    QPushButton { 
        background-color: #2f8571; 
        color: white; 
        border-radius: 16px; 
        padding: 10px; 
        font-weight: bold;
    }
    QPushButton:hover { background-color: #45a049; }
    QTextEdit{
        background-color: #083339;
        border: 2px solid teal;
        color: #15f500;
        font-size: 20px;}
    
    QListWidget {
        background-color: #13deaf ;
        color : #3b05de ;
        border: 1px solid pink ;
        padding: 10px}

    QListWidget::item {
        background-color: #7AAACE; 
        color: #e1f010;
        border: 2px solid #4CAF50;
        border-radius: 15px; 
        margin-bottom: 10px;      
        padding: 10px;
        font-family: mono sans;
        font-weight: bold;
        
    }

    QListWidget::item:selected {
        background-color: #355872;
        color: #ffffff;
        border: 2px solid #4CAF50;
    }

    QListWidget::item:hover {
        background-color: #42c8cd;
    }
"""

LIGHT_STYLE = """
    QMainWindow { background-color: #01b0aa; }
    QLabel { color: #000000; font-size: 18px; }
    QPushButton { 
        background-color: #008CBA; 
        color: white; 
        border-radius: 5px; 
        border-radius: 16px;
        padding: 10px;
    }
    QPushButton:hover { background-color: #007ba7; }
    QTextEdit { background-color : #addee4; border: 2px solid teal;color: #d53939 ; font-size:20px;}

    QListWidget {
        background-color: #083339 ;
        color : #3b05de ;
        border: 1px solid red ;
        padding: 10px}

    QListWidget::item {
        background-color: #3BC1A8; 
        color: #005461;
        border: 2px solid #4CAF50;
        border-radius: 15px; 
        margin-bottom: 10px;      
        padding: 10px;
        font-family: mono sans;
        font-weight: bold;
        
    }

    QListWidget::item:selected {
        background-color: #0C7779;
        color: #ffffff;
        border: 2px solid #4CAF50;
    }

    QListWidget::item:hover {
        background-color: #42c8cd;
    }
"""


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000  , 500 , 1000 , 800)
        self.is_dark = True
        self.theme_btn = QPushButton("theme" , self)
        self.save_btn = QPushButton("Save", self)
        self.new_btn = QPushButton("New", self)
        self.text_box = QTextEdit(self)
        self.notes_list = QListWidget(self)
        self.notes = {}        
        self.current_note = None
        self.notes_file = "notes.json"
        self.load_notes()
        self.title_box = QLineEdit(self)
        self.delete_btn = QPushButton("Delete" , self)
        
        self.initUI()





    def initUI(self):
        self.theme_btn.adjustSize()
        self._position_theme_btn()
        self.setWindowTitle("Dnotes")
        
        self.text_box.setGeometry(0 , 0 , int(self.width() * 0.8) , int(self.height()))
        self.title_box.setPlaceholderText("TITLE")
        self.text_box.setPlaceholderText("Start writing your note from here ")
        self.title_box.setAlignment(Qt.AlignCenter)
        self.title_box.textChanged.connect(self.valid_title)
        

        self.theme_btn.clicked.connect(self.toggle_theme)
        self.save_btn.clicked.connect(self.save_note)
        self.new_btn.clicked.connect(self.new_note)
        self.notes_list.itemClicked.connect(self.open_note)
        self.delete_btn.clicked.connect(self.delete_note)

        


        self.save_btn.adjustSize()
        self.new_btn.adjustSize()
        self._position_side_widgets()
        self.setStyleSheet(DARK_STYLE)

        self.save_btn.setEnabled(False)
        self.valid_title()
        




    def toggle_theme(self):
        if self.is_dark:
            self.setStyleSheet(LIGHT_STYLE)
            self.is_dark = False
        else:
            self.setStyleSheet(DARK_STYLE)
            self.is_dark = True
        

    def resizeEvent(self,event):
        self.text_box.setGeometry(0 , 0 , int(self.width() * 0.8) , int(self.height()))
        self._position_side_widgets()
        self._position_theme_btn()
        super().resizeEvent(event)

    def _position_theme_btn(self):
        margin = 10
        x = self.width() - self.theme_btn.width() - margin
        y = margin
        self.theme_btn.move(x, y)
        

    def _position_side_widgets(self):
        sidebar_x = int(self.width() * 0.8)
        sidebar_w = self.width() - sidebar_x
        btn_h = 35

        self.new_btn.setGeometry(sidebar_x + 10, 100, sidebar_w -20, btn_h)
        self.save_btn.setGeometry(sidebar_x + 10, 150, sidebar_w -20 , btn_h)
        self.notes_list.setGeometry(sidebar_x, 250, sidebar_w, self.height() - 125)
        self.title_box.setGeometry(sidebar_x + 10 , 50 , sidebar_w -20 , btn_h)
        self.delete_btn.setGeometry(sidebar_x + 10, 200 , sidebar_w -20 , btn_h)

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                self.notes = json.load(file)
        self.refresh_list()

    def refresh_list(self):
        self.notes_list.clear()
        for title in self.notes:
            item = QListWidgetItem(title)
            item.setTextAlignment(Qt.AlignCenter)
            self.notes_list.addItem(item)

    def save_note(self):
        content = self.text_box.toPlainText()
        if not content.strip():
            return

        title = self.title_box.text()
        if self.current_note and self.current_note in self.notes:
            del self.notes[self.current_note]
        self.current_note = title
        self.notes[title] = content
        with open(self.notes_file, "w") as f:
            json.dump(self.notes, f)
        self.refresh_list()

    def new_note(self):
        self.text_box.clear()
        self.current_note = None

    def open_note(self, item):
        title = item.text()
        self.current_note = title
        self.title_box.setText(title)
        self.text_box.setText(self.notes[title])

    def delete_note(self):
        title = self.title_box.text()

        if title in self.notes:
            del self.notes[title]

        with open(self.notes_file, "w") as f:
            json.dump(self.notes, f, indent=4)
        
        self.title_box.clear()
        self.text_box.clear()
        self.current_note = None
        
        self.refresh_list()


    def valid_title(self):
        content = self.title_box.text()

    

        if len(content) > 20:
            self.save_btn.setEnabled(False)
            self.save_btn.setStyleSheet("background-color: red;")

        elif len(content) != 0:
            self.save_btn.setEnabled(True)
            self.save_btn.setStyleSheet("background-color: #008CBA;")
            
        else:
            self.save_btn.setEnabled(False)
            self.save_btn.setStyleSheet("background-color: red;")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
    