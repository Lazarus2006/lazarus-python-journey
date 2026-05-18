from PyQt5.QtWidgets import QApplication,QWidget ,  QPushButton, QTextEdit, QMainWindow, QListWidget, QLineEdit, QListWidgetItem, QWidget, QVBoxLayout, QHBoxLayout , QSpinBox , QShortcut , QFileDialog
from PyQt5.QtCore import Qt , QTimer
from PyQt5.QtGui import QFont , QKeySequence , QTextDocument 
from PyQt5.QtPrintSupport import QPrinter
import sys
import json, os

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
        border-bottom-left-radius:50px;
        border-top-right-radius:50px;}
    
    QListWidget {
        background-color: #13deaf ;
        color : #3b05de ;
        border: 1px solid pink;
        border-top-right-radius:20px;
        border-top-left-radius:20px;
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

    QPushButton#theme_btn {
        border-radius: 15px;
        background-color: purple;
    }


    QPushButton#formatting_btn {
        background-color: grey;
        }
"""

LIGHT_STYLE = """
    QMainWindow { background-color: #01b0aa; }  
    QLabel { color: #000000; font-size: 18px; }
    QPushButton { 
        background-color: #008CBA; 
        color: white;  
        border-radius: 16px;
        padding: 10px;
    }
    QPushButton:hover { background-color: #007ba7; }
    QTextEdit { background-color : #addee4;
                border: 2px solid teal;
                color: #d53939 ;
                border-bottom-left-radius:50px;
                border-top-right-radius:50px;}

    QListWidget {
        background-color: #083339 ;
        color : #3b05de ;
        border: 1px solid red;
        border-top-right-radius:20px;
        border-top-left-radius:20px;
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

    QPushButton#theme_btn {
        border-radius: 18px;
        background-color: grey;
        color:yellow;
        font-weight:bold;
    }

    QPushButton#formatting_btn {
        background-color: pink;
    }
"""


class howerbutton(QPushButton):
    def __init__(self,text , hower_text ,  parent = None):
        super().__init__(text, parent)
        self.original_text = text
        self.hower_text = hower_text

    def enterEvent(self, event):
        self.setText(self.hower_text)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setText(self.original_text)
        super().leaveEvent(event)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600 , 600 , 1000 , 1000)
        self.is_dark = True
        self.auto_save = True
        self.justify_state = 1
        self.theme_btn = QPushButton("⏾", self)
        self.save_btn = QPushButton("Save", self)
        self.new_btn = QPushButton("New", self)
        self.text_box = QTextEdit(self)
        self.notes_list = QListWidget(self)
        self.notes = {}
        self.current_note = None
        self.notes_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
        self.load_notes()
        self.title_box = QLineEdit(self)
        self.delete_btn = QPushButton("Delete", self)
        self.font_size = QSpinBox(self)
        self.search_box = QLineEdit(self)
        self.font_size.setRange(1 , 100)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.save_note)

        
        self.initUI()
        self.app_layout()
        self.keyboard_shortcuts()
        self.get_font_size()
        self.auto_save_function()
    

    def initUI(self):
        self.setWindowTitle("Dnotes")
        
        self.theme_btn.setObjectName("theme_btn")
        self.title_box.setPlaceholderText("TITLE")
        self.text_box.setPlaceholderText("Start writing your note from here ")
        self.search_box.setPlaceholderText("🔍 Search notes...")
        self.title_box.setAlignment(Qt.AlignCenter)
        self.search_box.setAlignment(Qt.AlignCenter)
        

        self.bold_btn = howerbutton("B" , "Bold", self)
        self.bold_btn.setObjectName("formatting_btn")
        self.italic_btn = howerbutton("I" , "Italic", self)
        self.italic_btn.setObjectName("formatting_btn")
        self.underline_btn = howerbutton("U" , "Underline", self)
        self.underline_btn.setObjectName("formatting_btn")
        self.autosave_btn = howerbutton("A" , "Auto Save", self)
        self.justify_btn = howerbutton("J", "Justify", self)
        self.justify_btn.setObjectName("formatting_btn")
        self.export_txt_btn = howerbutton("Txt" , "Export as Text" , self)
        self.export_txt_btn.setObjectName("formatting_btn")
        self.export_pdf_btn = howerbutton("PDF" , "Export as PDF" , self)
        self.export_pdf_btn.setObjectName("formatting_btn")
        self.open_btn = howerbutton("Open" , "Open txt file" , self)
        self.open_btn.setObjectName("formatting_btn")
        
        
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.save_btn.clicked.connect(self.save_note)
        self.new_btn.clicked.connect(self.new_note)
        self.notes_list.itemClicked.connect(self.open_note)
        self.delete_btn.clicked.connect(self.delete_note)
        self.title_box.textChanged.connect(self.valid_title)
        self.bold_btn.clicked.connect(self.bold_text)
        self.italic_btn.clicked.connect(self.italic_text)
        self.underline_btn.clicked.connect(self.underline_text)
        self.font_size.valueChanged.connect(self.change_font_size)
        self.autosave_btn.clicked.connect(self.toggle_autosave)
        self.justify_btn.clicked.connect(self.justify_text)
        self.search_box.textChanged.connect(self.search_notes)
        self.export_txt_btn.clicked.connect(self.save_as_txt)
        self.export_pdf_btn.clicked.connect(self.save_as_pdf)
        self.open_btn.clicked.connect(self.open_external_file)
        
        
        self.setStyleSheet(DARK_STYLE)
        self.save_btn.setEnabled(False)
        self.valid_title()


    
    def app_layout(self):
        container = QWidget()

        hbox  = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()

        hbox2.addWidget(self.bold_btn)
        hbox2.addWidget(self.italic_btn)
        hbox2.addWidget(self.underline_btn)
        hbox2.addWidget(self.justify_btn)
        hbox2.addWidget(self.autosave_btn)
        hbox2.addWidget(self.font_size)

        theme_hbox = QHBoxLayout()

        vbox1.addWidget(self.text_box)
        vbox1.addLayout(hbox2)

        theme_hbox.addWidget(self.export_txt_btn)
        theme_hbox.addWidget(self.export_pdf_btn)
        theme_hbox.addWidget(self.open_btn)
        theme_hbox.addStretch(1)
        theme_hbox.addWidget(self.theme_btn)
        vbox2.addLayout(theme_hbox)
        vbox2.addWidget(self.title_box)
        vbox2.addWidget(self.new_btn)
        vbox2.addWidget(self.save_btn)
        vbox2.addWidget(self.delete_btn)
        vbox2.addWidget(self.search_box)
        vbox2.addWidget(self.notes_list)
        

        hbox.addLayout(vbox1 , 4)
        hbox.addLayout(vbox2 , 1)
        
        container.setLayout(hbox)
        self.setCentralWidget(container)


    def keyboard_shortcuts(self):
        self.new_btn.setShortcut("Ctrl+N")
        self.save_btn.setShortcut("Ctrl+S")
        self.delete_btn.setShortcut("Ctrl+del")

        self.increase_font_size = QShortcut(QKeySequence("Ctrl++"), self)
        self.increase_font_size.activated.connect(lambda: self.font_size.setValue(self.font_size.value() + 1))

        self.increase_font_size_2 = QShortcut(QKeySequence("Ctrl+="), self)
        self.increase_font_size_2.activated.connect(lambda: self.font_size.setValue(self.font_size.value() + 1))
        
        self.decrease_font_size = QShortcut(QKeySequence("Ctrl+-") , self)
        self.decrease_font_size.activated.connect(lambda: self.font_size.setValue(self.font_size.value() - 1))

        self.bold_shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
        self.bold_shortcut.activated.connect(self.bold_text)
        
        self.italic_shortcut = QShortcut(QKeySequence("Ctrl+I"), self)
        self.italic_shortcut.activated.connect(self.italic_text)

        self.underline_shortcut = QShortcut(QKeySequence("Ctrl+U"), self)
        self.underline_shortcut.activated.connect(self.underline_text)

        self.justify_shortcut = QShortcut(QKeySequence("Ctrl+J"), self)
        self.justify_shortcut.activated.connect(self.justify_text)

        self.theme_shortcut = QShortcut(QKeySequence("Ctrl+T"), self)
        self.theme_shortcut.activated.connect(self.toggle_theme)


    def toggle_theme(self):
        if self.is_dark:
            self.setStyleSheet(LIGHT_STYLE)
            self.is_dark = False
            self.theme_btn.setText("𖤓")
        
        else:
            self.setStyleSheet(DARK_STYLE)
            self.is_dark = True
            self.theme_btn.setText("⏾")

        self.theme_bug_fix()
        self.theme_bug_fix()


    def theme_bug_fix(self):
        self.bold_text()
        self.italic_text()
        self.underline_text()
        

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as file:
                loaded = json.load(file)
                if isinstance(loaded, dict):
                    self.notes = loaded
                else:
                    self.notes = {}
        self.refresh_list()

    def refresh_list(self):
        self.notes_list.clear()
        for title in self.notes:
            item = QListWidgetItem(title)
            item.setTextAlignment(Qt.AlignCenter)
            self.notes_list.addItem(item)

    def save_note(self):
        content = self.text_box.toHtml()
        if not self.text_box.toPlainText().strip():
            return

        title = self.title_box.text()

        if self.current_note and self.current_note in self.notes:
            del self.notes[self.current_note]

        if len(title) == 0:
            return
        
        self.current_note = title
        self.notes[title] = content
        with open(self.notes_file, "w") as f:
            json.dump(self.notes, f)
        self.refresh_list()

    def new_note(self):
        self.text_box.clear()
        self.title_box.clear()
        self.current_note = None

    def open_note(self, item):
        title = item.text()
        self.current_note = title
        self.title_box.setText(title)
        self.text_box.setHtml(self.notes[title])

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
        title = self.title_box.text()
        if len(title) > 20:
            self.save_btn.setEnabled(False)
            self.save_btn.setStyleSheet("background-color: red;")
        elif len(title) != 0:
            self.save_btn.setEnabled(True)
            self.save_btn.setStyleSheet("background-color: #008CBA;")
        else:
            self.save_btn.setEnabled(False)
            self.save_btn.setStyleSheet("background-color: red;")

    def bold_text(self):
        current_weight = self.text_box.fontWeight()
    
        if current_weight == QFont.Bold:
            self.text_box.setFontWeight(QFont.Normal)
            if self.is_dark:
                self.bold_btn.setStyleSheet("background-color:grey;")
            else:
                self.bold_btn.setStyleSheet("background-color: pink;")
        else:
            self.text_box.setFontWeight(QFont.Bold)
            if self.is_dark:
                self.bold_btn.setStyleSheet("background-color:teal;")
            else:
                self.bold_btn.setStyleSheet("background-color: lime;")

    def italic_text(self):
        is_currently_italic = self.text_box.fontItalic()
        self.text_box.setFontItalic(not is_currently_italic)
        if not is_currently_italic:
            if self.is_dark:
                self.italic_btn.setStyleSheet("background-color:teal;font-style:italic;")
            else:
                self.italic_btn.setStyleSheet("background-color:lime;font-style:italic;")
        else:
            if self.is_dark:
                self.italic_btn.setStyleSheet("background-color:grey;font-style:normal;")
            else:
                self.italic_btn.setStyleSheet("background-color:pink;font-style:normal;")    
        
    def underline_text(self):
        is_underlined = self.text_box.fontUnderline()
        self.text_box.setFontUnderline(not is_underlined)

        if not is_underlined:
            if self.is_dark:
                self.underline_btn.setStyleSheet("background-color:teal;")
            else:
                self.underline_btn.setStyleSheet("background-color:lime;")
        else:
            if self.is_dark:
                self.underline_btn.setStyleSheet("background-color:grey;")
            else:
                    self.underline_btn.setStyleSheet("background-color:pink") 


    def justify_text(self):
        if self.justify_state == 1:
            self.text_box.setAlignment(Qt.AlignCenter)
            self.justify_btn.setText("Center")
            self.justify_state = 2

        elif self.justify_state == 2:
            self.text_box.setAlignment(Qt.AlignRight)
            self.justify_btn.setText("Right")
            self.justify_state = 3

        elif self.justify_state == 3:
            self.text_box.setAlignment(Qt.AlignJustify)
            self.justify_btn.setText("Justify")
            self.justify_state = 4

        elif self.justify_state == 4:
            self.text_box.setAlignment(Qt.AlignLeft)
            self.justify_btn.setText("Left")
            self.justify_state = 1

        else:
            pass



    def get_font_size(self):
        current_size = self.text_box.font().pointSize()
        self.font_size.setValue(int(current_size))

    def change_font_size(self):
        new_size = self.font_size.value()
        self.text_box.setFontPointSize(new_size)


    def toggle_autosave(self):
        if self.auto_save:
            self.auto_save = False
            if self.is_dark:
                self.autosave_btn.setStyleSheet("background-color:grey;")
            else:
                self.autosave_btn.setStyleSheet("background-color:pink;")
            self.timer.stop()
        else:
            self.auto_save = True
            self.autosave_btn.setStyleSheet("background-color:#2f8571;")
            self.timer.start(10000)
        
    def search_notes(self):
        search_text = self.search_box.text().strip().lower()
        for i in range(self.notes_list.count()):
            item = self.notes_list.item(i)
            if not search_text or search_text in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
    

    def auto_save_function(self):
        if self.auto_save:
            self.timer.start(10000)

    def save_as_txt(self):
        note_title = self.title_box.text().strip()
        default_name = f"{note_title}.txt" if note_title else "untitled.txt"
        file_path , _ = QFileDialog.getSaveFileName(self , "Export Note as Text",default_name , "Text Files (*.txt);;All Files (*)")
        if file_path:
            plain_text = self.text_box.toPlainText()
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(plain_text)

    def save_as_pdf(self):
        note_title = self.title_box.text().strip()
        default_name = f"{note_title}.pdf" if note_title else "untitled.pdf"

        file_path, _ = QFileDialog.getSaveFileName(self, "Export Note as PDF", default_name, "PDF Files (*.pdf);;All Files (*)")
        if file_path:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_path)
            self.text_box.document().print_(printer)

    def open_external_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Document", "", "Text Files (*.txt);;HTML Files (*.html)")
        
        if file_path:
            file_name = os.path.basename(file_path)
            title_without_ext, ext = os.path.splitext(file_name)
            
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()

                self.title_box.setText(title_without_ext)
                
                if ext.lower() == ".html":
                    self.text_box.setHtml(file_content)
                else:
                    self.text_box.setPlainText(file_content)
                    
                self.valid_title()
                
            except Exception as e:
                self.title_box.setText("Error")
                self.text_box.setPlainText(f"Could not read file structure: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())
