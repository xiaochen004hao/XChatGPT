from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.Qsci import QsciScintilla, QsciLexerPython
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        self.editor = QsciScintilla(self)
        self.editor.setFont(QFont("Courier New", 12))
        self.setCentralWidget(self.editor)

        # 设置代码编辑器的颜色样式
        self.editor.setMarginsBackgroundColor(QColor("#1E1E1E"))
        self.editor.setMarginsForegroundColor(QColor("#D4D4D4"))
        self.editor.setCaretForegroundColor(QColor("#D4D4D4"))
        self.editor.setMarginsFont(QFont("Courier New", 12))
        self.editor.setUtf8(True)

        # 设置语法高亮
        lexer = QsciLexerPython()
        lexer.setDefaultFont(QFont("Courier New", 12))
        self.editor.setLexer(lexer)

        # 设置文本框的换行模式
        self.editor.setWrapMode(QsciScintilla.WrapMode.WrapNone)

        # 设置文本框的垂直滚动条策略
        self.editor.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # 设置文本框的自动缩进
        self.editor.setAutoIndent(True)

        # 设置文本框的折叠模式
        self.editor.setFolding(QsciScintilla.FoldStyle.BoxedTreeFoldStyle)

        # 设置文本框的折叠标记颜色
        self.editor.setFoldMarginColors(QColor("#1E1E1E"), QColor("#D4D4D4"))

        # 设置文本框的折叠标记区域宽度
        self.editor.setStyleSheet("QsciScintilla::fold-margin { width: 16px; }")

        # 设置文本框的折叠标记外观
        # self.editor.setFoldMarginMarkers(True, QsciScintilla.SC_MARKNUM_FOLDEROPEN, QsciScintilla.SC_MARKNUM_FOLDER)

        # 设置文本框的自动换行模式
        # self.editor.setWrapMode(QsciScintilla.WrapNone)

        # 设置文本框的缩进宽度
        self.editor.setIndentationWidth(4)

        # 设置文本框的缩进替代符号
        self.editor.setIndentationGuides(True)

        # 设置文本框的自动补全
        self.editor.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.All)
        self.editor.setAutoCompletionCaseSensitivity(False)
        self.editor.setAutoCompletionThreshold(1)
        self.editor.setAutoCompletionFillupsEnabled(True)

        # 加载文件或设置初始文本
        self.editor.setText('''
        for i in range(3):
            print(i)
        ''')

        # 设置窗口标题
        self.setWindowTitle("Code Editor")

        # 显示窗口
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())