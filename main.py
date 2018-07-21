# 作者：李可艺
# 创建于：2018-7-14
import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class CarPlatteRecognitionWidget(QWidget):
    def __init__(self):
        # init
        super().__init__()


        # layout setting
        # gird layout
        grid = QGridLayout()
        self.setLayout(grid)

        # buttons
        self.button1 = QPushButton('选择图片')
        self.button1.clicked.connect(self.load_image)
        grid.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton('识别车牌')
        self.button2.clicked.connect(self.process)
        grid.addWidget(self.button2, 2, 0)

        # labels
        self.pic_label = QLabel()
        self.pic_label.setFixedSize(400, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.pic_label, 1, 0)

        self.res_label = QLabel()
        self.res_label.setAlignment(Qt.AlignLeft)
        self.res_label.setFixedWidth(400)
        grid.addWidget(self.res_label, 3, 0)

        # window setting
        # set size
        self.resize(400, 600)
        # set window title
        self.setWindowTitle('车牌识别 © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./src/icon.png'))


        # args
        self.file_name = ''


        # show
        self.show()


    def load_image(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                                                   '选择图片',
                                                   '',
                                                   'Image files(*.jpg *.gif *.png)')
        self.pic_label.setPixmap(QPixmap(self.file_name).
                                 scaled(400, 300, Qt.KeepAspectRatioByExpanding))


    def process(self):
        try:
            if self.file_name == '':
                QMessageBox.information(self, '错误！找不到图片',
                                        "请先上传图片！",
                                        QMessageBox.Yes)
                return

            from car_platte_recognition import main
            res, precision = main.predict(self.file_name)

            self.res_label.setText('%s\n准确度%f%%' % (res, precision))
        except:
            QMessageBox.information(self, '错误！找不到模型',
                                    "找不到训练好的模型！请先训练模型！",
                                    QMessageBox.Yes)


class FaceRecognitionWidget(QWidget):
    def __init__(self):
        # init
        super().__init__()


        # layout setting
        # gird layout
        grid = QGridLayout()
        self.setLayout(grid)

        # buttons
        self.button1 = QPushButton('选择图片')
        self.button1.clicked.connect(self.load_image)
        grid.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton('识别人脸')
        self.button2.clicked.connect(self.process)
        grid.addWidget(self.button2, 2, 0)

        # labels
        self.pic_label = QLabel()
        self.pic_label.setFixedSize(400, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.pic_label, 1, 0)

        self.respic_label = QLabel()
        self.respic_label.setFixedSize(400, 300)
        self.respic_label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.respic_label, 3, 0)


        self.res_label = QLabel()
        self.res_label.setAlignment(Qt.AlignLeft)
        self.res_label.setFixedWidth(400)
        grid.addWidget(self.res_label, 4, 0)


        # window setting
        # set size
        self.resize(400, 600)
        # set window title
        self.setWindowTitle('人脸识别 © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./src/icon.png'))


        # args
        self.file_name = ''


        # show
        self.show()


    def load_image(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                                                   '选择图片',
                                                   '',
                                                   'Image files(*.jpg *.gif *.png)')
        self.pic_label.setPixmap(QPixmap(self.file_name).
                                 scaled(400, 300, Qt.KeepAspectRatioByExpanding))



    def process(self):
        try:
            if self.file_name == '':
                QMessageBox.information(self, '错误！找不到图片',
                                        "请先上传图片！",
                                        QMessageBox.Yes)
                return

            from car_platte_recognition import main

            from face_recognition import main
            list_, disp_image = main.predict(self.file_name)

            str_ = '一共找到%d张脸\n' % len(list_)
            for i, l in enumerate(list_):
                str_ += '%d:%s 准确度7%f%%\n' % (i, l[0], l[1])

            self.respic_label.setPixmap(QPixmap(disp_image).
                                        scaled(400, 300, Qt.KeepAspectRatioByExpanding))
            self.res_label.setText(str_)
        except:
            QMessageBox.information(self, '错误！找不到模型',
                                    "找不到训练好的模型！请先训练模型！",
                                    QMessageBox.Yes)


class OpticalCharacterRecognitionWidget(QWidget):
    def __init__(self):
        # init
        super().__init__()


        # layout setting
        # gird layout
        grid = QGridLayout()
        self.setLayout(grid)

        # buttons
        self.button1 = QPushButton('选择图片')
        self.button1.clicked.connect(self.load_image)
        grid.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton('识别印刷文字')
        self.button2.clicked.connect(self.process)
        grid.addWidget(self.button2, 2, 0)

        # labels
        self.pic_label = QLabel()
        self.pic_label.setFixedSize(400, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.pic_label, 1, 0)

        self.res_label = QLabel()
        self.res_label.setAlignment(Qt.AlignCenter)
        self.res_label.setFixedWidth(400)
        grid.addWidget(self.res_label, 3, 0)

        # window setting
        # set size
        self.resize(400, 600)
        # set window title
        self.setWindowTitle('印刷文字识别 © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./src/icon.png'))


        # args
        self.file_name = ''


        # show
        self.show()


    def load_image(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                                                   '选择图片',
                                                   '',
                                                   'Image files(*.jpg *.gif *.png)')
        self.pic_label.setPixmap(QPixmap(self.file_name).
                                 scaled(400, 300, Qt.KeepAspectRatioByExpanding))


    def process(self):
        try:
            if self.file_name == '':
                QMessageBox.information(self, '错误！找不到图片',
                                        "请先上传图片！",
                                        QMessageBox.Yes)
                return

            from car_platte_recognition import main
            from optical_character_recognition import main
            res, precision = main.predict(self.file_name)

            self.res_label.setText(res)
        except:
            QMessageBox.information(self, '错误！找不到模型',
                                    "找不到训练好的模型！请先训练模型！",
                                    QMessageBox.Yes)


class HandWrittenRecognitionWidget(QWidget):
    def __init__(self):
        # init
        super().__init__()


        # layout setting
        # gird layout
        grid = QGridLayout()
        self.setLayout(grid)

        # buttons
        self.button1 = QPushButton('选择图片')
        self.button1.clicked.connect(self.load_image)
        grid.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton('识别手写汉字')
        self.button2.clicked.connect(self.process)
        grid.addWidget(self.button2, 2, 0)

        # labels
        self.pic_label = QLabel()
        self.pic_label.setFixedSize(400, 300)
        self.pic_label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.pic_label, 1, 0)

        self.res_label = QLabel()
        self.res_label.setAlignment(Qt.AlignLeft)
        self.res_label.setFixedWidth(400)
        grid.addWidget(self.res_label, 3, 0)

        # window setting
        # set size
        self.resize(400, 600)
        # set window title
        self.setWindowTitle('手写汉字识别 © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./src/icon.png'))


        # args
        self.file_name = ''

           # show
        self.show()


    def load_image(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,
                                                   '选择图片',
                                                   '',
                                                   'Image files(*.jpg *.gif *.png)')
        self.pic_label.setPixmap(QPixmap(self.file_name).
                                 scaled(400, 300, Qt.KeepAspectRatioByExpanding))


    def process(self):
        try:
            if self.file_name == '':
                QMessageBox.information(self, '错误！找不到图片',
                                        "请先上传图片！",
                                        QMessageBox.Yes)
                return

            from car_platte_recognition import main
            from handwritten_recognition import main
            res, precision = main.predict(self.file_name)

            self.res_label.setText('%s\n准确度%f%%' % (res, precision))
        except:
            QMessageBox.information(self, '错误！找不到模型',
                                    "找不到训练好的模型！请先训练模型！",
                                    QMessageBox.Yes)


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
        self.funcs = [
            CarPlatteRecognitionWidget(),
            OpticalCharacterRecognitionWidget(),
            HandWrittenRecognitionWidget(),
            FaceRecognitionWidget()
        ]
        self.buttons = []
        for i, name in enumerate(names):
            self.funcs[i].hide()
            self.buttons.append(QPushButton(name, self))
            self.buttons[i].clicked.connect(self.funcs[i].show)

        for pos, button in enumerate(self.buttons):
            grid.addWidget(button, pos + 1, 0)


        # window setting
        # set size
        self.resize(300, 400)
        # set window title
        self.setWindowTitle('识别工具箱 CV toolkit © v1.0')
        # set windows icon
        self.setWindowIcon(QIcon('./src/icon.png'))


        # show
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # set global style
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    mw = MainWidget()
    sys.exit(app.exec_())