import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QTextCursor
from PyQt6.QtCore import QSize


class WordleBoard(QMainWindow):

    def __init__(self):
        super(WordleBoard, self).__init__()

        self.setWindowTitle("Test")
        self.letters_layout = QGridLayout()

        # for i in range(6):
        #     for j in range(5):
        #         if i % 2 == 0:
        #             letters_layout.addWidget(WordleLetter(), i, j)
        #         else:
        #             letters_layout.addWidget(WordleLetter(), i, j)
        self.draw_empty_board()

        display_widget = QWidget()
        display_widget.setLayout(self.letters_layout)
        self.setCentralWidget(display_widget)

    def draw_empty_board(self):
        """add empty WordleLetter objects to grid layout"""

        # first row figure how to set active focus
        for j in range(5):
            self.letters_layout.addWidget(WordleLetterTile(), 0, j)

        # other rows figure how to set inactive focus
        for i in range(1, 6):
            for j in range(5):
                this_letter = WordleLetterTile()
                self.letters_layout.addWidget(this_letter, i, j)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class WordleLetterTile(QLineEdit):

    def __init__(self):
        super(WordleLetterTile, self).__init__()
        self.setFixedSize(QSize(120, 120))
        self.setAutoFillBackground(True)

        # input mask dictates input validation
        # 'A' means alpha character, and since only 1 'A' only one character
        self.setInputMask('A')

        # make big font
        font = self.font()
        font.setPointSize(100)
        self.setFont(font)

        # color definitions
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor('white'))
        palette.setColor(QPalette.ColorRole.Base, QColor('black'))
        self.setPalette(palette)

        # margin
        margin = self.textMargins()
        margin.setLeft(15)
        margin.setRight(15)
        self.setTextMargins(margin)


# app = QApplication(sys.argv)
# window = WordleBoard()
# window.show()

# app.exec()
