import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWidget(QWidget):
    def __init__(self):
        # init
        super().__init__()


        # layout setting
        # gird layout
        grid = QGridLayout()
        self.setLayout(grid)

        # name and icon
        title = QLabel('识别工具箱 © v1.0', self)
        # align
        title.setFixedWidth(300)
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Roman times", 20, QFont.Bold))

        grid.addWidget(title, 0, 0)


        # buttons
        names = [
            '车牌识别',
            '印刷文字识别',
            '手写汉字识别',
            '人脸识别'
        ]
        buttons = []
        for name in names:
            buttons.append(QPushButton(name, self))

        for pos, button in zip(range(4), buttons):
            grid.addWidget(button, pos + 1, 0)


        # window setting
        # set size
        self.resize(300, 400)
        # set window title
        self.setWindowTitle('识别工具箱 CV toolkit © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./image/icon.png'))


        # stylesheet

        # show
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # set global style
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    mw = MainWidget()
    sys.exit(app.exec_())