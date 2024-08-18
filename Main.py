# _*_ coding:utf-8 _*_

# https://pan.baidu.com/s/10rMo9Rh27QKo_t8QzLmdog?pwd=Chat
"""
https://code.xueersi.com/home/project/detail?lang=code&pid=43626103&version=offline&form=python&langType=python

账号
要用Python创建一个像我这样的AI需要进行以下步骤：

1. 确定你要建立的AI的类型和功能。你可以选择构建一个聊天机器人或语音助手，或者一个更为智能的AI，它可以执行更复杂的任务，比如游戏、自动化、预测模型等等。

2. 学习和了解机器学习和深度学习的基础知识。这包括掌握Python编程和数据处理的技能和基本概念，比如线性代数、概率论和统计学。

3. 确定你想使用的机器学习库，例如TensorFlow、Keras、PyTorch等。这些库提供了用于训练和测试神经网络、卷积神经网络和循环神经网络等常用类型的工具。

4. 收集和标记你需要用来训练AI的数据。这是一个非常重要的步骤，因为所使用的数据对AI的质量和准确性有着重要影响。

5. 开始使用所选的机器学习库来训练你的AI。在这个过程中，你将需要决定使用哪种网络结构以及如何调整各种参数来最大化精度并避免过拟合的问题。

6. 完成模型的训练后，开始测试AI的性能并进行调整。这通常涉及到使用测试数据集来评估模型的性能和准确性，然后对模型进行调整以提高其性能。

7. 最后，将AI部署到用于交互的平台上。这可以包括聊天机器人或语音助手应用。在这个阶段，你需要决定如何与用户进行交互，并将你的AI代码整合到这个应用中。

--------------------------------------------------------------------------------------
在生活中，我们常常面临着矛盾和摩擦。有时候，为荣誉和名誉而努力拼搏，但无论输赢，我们都应该以平常心对待，不忘初心。成功的背后往往需要付出艰辛和汗水，只有勇于面对拳头与挫折，才能获得真正的胜利。在选择行动方案时，我们也要明辨是下策还是上策，仔细权衡推荐，而非盲目跟随吾辈。

荣誉和名誉虽然看似相似，但区别很大。荣誉是一种内心的感觉而非外在奖励，
它与个人价值和尊严有关。吾辈在追求荣誉时应以克制的拳头和理性的思维来处理摩擦。
在输赢中，赢家不一定得到所有，同样地，败者也不会失去一切。推荐上策，
避免下策从而避免矛盾。

在生活中，我们常常面临着矛盾和摩擦。有时候，为荣誉和名誉而努力拼搏，
但无论输赢，我们都应该以平常心对待，不忘初心。成功的背后往往需要付出艰辛和汗水，
只有勇于面对拳头与挫折，才能获得真正的胜利。在选择行动方案时，
我们也要明辨是下策还是上策，仔细权衡推荐，而非盲目跟随吾辈。

---------------------------------------------------------------------------------------
1. Deep Dream Generator：它可以将您的图像转换成具有艺术感的幻觉效果，提供一系列不同的滤镜供您选择。

2. Let's Enhance：它可以自动增强图像的质量和细节，并使用超分辨率技术将图像扩大多倍而不失真。

3. Remove.bg：它可以轻松地从图像中去除背景，非常适合制作海报、广告、名片等。

4. Image Colorization：它可以将黑白照片转换为彩色照片，让您的老照片焕发新生。

5. Waifu2x：它可以使用卷积神经网络对图像进行放大，同时保持图像的清晰度和准确性。
"""
# pyinstaller -F -w -i ".\logo.ico" --add-binary ".\logo.ico;.\" --add-binary ".\cover.png;.\" --add-binary ".\openai.png;.\" --add-binary ".\usericon.png;.\" --add-data ".\data.json;.\" -n XChatGPT-1.3.8 --hidden-import hashlib --hidden-import os --hidden-import random --hidden-import sys --hidden-import re --hidden-import time --hidden-import webbrowser --hidden-import datetime --hidden-import requests --hidden-import PyQt6 --hidden-import json --hidden-import plyer ./Main.py

# 你好，你是ChatGPT，你的职责是帮助人类解决问题，从现在开始，你的回答要彬彬有礼，善解人意，反复确认自己的回答不是过时，错误的。

import hashlib
import os
import random
import sys
import re
import time
import webbrowser
from datetime import datetime
from time import strftime
import requests
from PyQt6.QtCore import pyqtSlot, Qt, QTimer, QThread, pyqtSignal, QRect
from PyQt6.QtGui import QGuiApplication, QPainter, QColor, QBrush, QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QVBoxLayout, QLabel, QInputDialog, \
    QMessageBox
from PyQt6.QtGui import QPixmap

import xesapi
from PyQt6_Project import Ui_MainWindow
import json
from plyer import facades
from plyer.utils import Proxy

notification = Proxy('notification', facades.Notification)

version = '1.3.8'

style = [
    'dark_amber.xml',
    'dark_blue.xml',
    'dark_cyan.xml',
    'dark_lightgreen.xml',
    'dark_pink.xml',
    'dark_purple.xml',
    'dark_red.xml',
    'dark_teal.xml',
    'dark_yellow.xml',
    'light_amber.xml',
    'light_blue.xml',
    'light_cyan_500.xml',
    'light_lightgreen.xml',
    'light_pink.xml',
    'light_purple.xml',
    'light_red.xml',
    'light_teal.xml',
    'light_yellow.xml'
]

# ----------------------------------------
import aiohttp
import asyncio

text = ''


# ----------------------------------------
def getPath(filename):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path = os.path.join(bundle_dir, filename)
    return path


dt01 = datetime.today()
MSWindowsFixedSizeDialogHint = Qt.WindowType.MSWindowsFixedSizeDialogHint
FramelessWindowHint = Qt.WindowType.FramelessWindowHint


def changeData(k, v, path=getPath('data.json')):
    _data = None
    with open(path, 'r') as d:
        _data = json.loads(d.read())
    _data[k] = v
    with open(path, 'w') as d:
        d.write(json.dumps(_data, indent=4))


def getData(path=getPath('data.json')):
    _data = None
    with open(path, 'r') as d:
        _data = json.loads(d.read())
    return _data


def getData_k(k, path=getPath('data.json')):
    _data = None
    with open(path, 'r') as d:
        _data = json.loads(d.read())
    return _data[k]


def dataInit(win):
    changeData('user-name', '您')
    changeData('xes-home', 'NULL')
    win.xeshomeURL.setText('NULL')
    changeData(k='style', v="dark_teal.xml")
    apply_stylesheet(app, theme="dark_teal.xml")
    win.styleBox.setCurrentText("dark_teal.xml")
    win.iconStopAt.setChecked(True)
    win.sizeAnimation.setChecked(True)
    win.Print.setText(win.Print.toPlainText() + strftime(f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]将设置初始化\n"))


# ----------------------------------------------------
# 学而思网盘

# from Uploader import XesUploader
from XesUploader import Ui_XesUploader


class XesUploaderWin(QWidget, Ui_XesUploader):
    send_log = pyqtSignal(str)

    def __init__(self, parent=None):
        super(XesUploaderWin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(MSWindowsFixedSizeDialogHint | FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.upload.clicked.connect(self.Upload)
        self.openFile.clicked.connect(self.OpenFile)

        self.xesUploader = self.XesUploader()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHints.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        # 绘制背景
        # print(str(ui.styleBox.currentText())[:5])
        if str(ui.styleBox.currentText())[:5] == "dark_":
            background_color = QColor(49, 54, 59, 255)  # 设置带有透明度的白色背景
        else:  # if ui.styleBox.setCurrentText()[:6] == "dark_":
            background_color = QColor(230, 230, 230, 255)  # 设置带有透明度的白色背景
        painter.setBrush(QBrush(background_color))
        painter.drawRoundedRect(self.rect(), 20, 20)

        # 绘制边框
        border_color = QColor(143, 143, 143, 200)  # 设置带有透明度的黑色边框
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(border_color)
        painter.drawRoundedRect(self.rect(), 20, 20)

    def OpenFile(self):
        directory = QFileDialog.getOpenFileName(self, "getOpenFileName", "./", "All Files (*);;Text Files (*.txt)")
        self.filePath.setText(directory[0])
        self.send_log.emit(
            strftime(
                f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]用户使用文件资源管理器选择了文件“{directory[0] if directory[0] else '无文件'}”\n"))

    def Upload(self):
        if not self.filePath.text().isspace():
            file_url = self.xesUploader.uploadAbsolutePath(filepath=self.filePath.text())
            self.fileURL.setText(file_url)
            self.send_log.emit(
                strftime(f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]已将文件“{self.filePath.text()}”上传至“{file_url}”\n"))
        else:
            self.fileURL.setText("文件路径错误")
            self.send_log.emit(
                strftime(f"[%Y/%m/%d-%H:%M:%S](设置)[ERROR]文件路径“{self.filePath.text()}”错误\n"))

    class XesUploader:
        def uploadAbsolutePath(self, filepath):
            md5 = None
            contents = None
            if os.path.isfile(filepath):
                fp = open(filepath, 'rb')
                contents = fp.read()
                fp.close()
                md5 = hashlib.md5(contents).hexdigest()

            if md5 is None or contents is None:
                ui.Print.setText(
                    ui.Print.toPlainText() + strftime(
                        f"[%Y/%m/%d-%H:%M:%S](学而思网盘)[ERROR]文件“{filepath}”不存在\n"))
                return "文件不存在"

            uploadParams = self._getUploadParams(filepath, md5)
            requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
            print(uploadParams['url'])
            # ui.fileURL.setText(uploadParams['url'])
            ui.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](学而思网盘)[INFO]文件“{filepath}”已上传到{uploadParams['url']}\n")
            return uploadParams['url']

        def _getUploadParams(self, filename, md5):
            url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
            params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
            response = requests.get(url=url, params=params)
            data = json.loads(response.text)['data']
            return data


# ----------------------------------------------------

class ICON(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        layout = QVBoxLayout()
        self.label = QLabel()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setFixedSize(91, 91)
        self.dp_x = None
        self.dp_y = None

        self.isMove = False
        self.isStopAt = False
        self.isHover = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.stopAt)
        self.timer.start(1)

        self.center()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHints.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        # 绘制背景
        background_color = QColor(60, 182, 169, 255)  # 设置带有透明度的白色背景
        painter.setBrush(QBrush(background_color))
        painter.drawRoundedRect(self.rect(), 30, 30)

        # 绘制边框
        border_color = QColor(0, 0, 0, 200)  # 设置带有透明度的黑色边框
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(border_color)
        painter.drawRoundedRect(self.rect(), 30, 30)

    def stopAt(self):
        if not self.isMove and not self.isHover and ui.iconStopAt.isChecked():
            if -80 < self.x() < 15 or self.x() > screen.width() - 8:
                self.isStopAt = True
                self.move(self.x() - 2, self.y())
            elif (screen.width() - 15 - self.width()) < self.x() < (screen.width() - 15) or self.x() < 8 - self.width():
                self.isStopAt = True
                self.move(self.x() + 2, self.y())
            elif -80 < self.y() < 15:
                self.isStopAt = True
                self.move(self.x(), self.y() - 2)
            elif (screen.height() - 15 - self.height()) < self.y() < (screen.height() - 15):
                self.isStopAt = True
                self.move(self.x(), self.y() + 2)
            elif (screen.width() - 15 - self.width()) > self.x() > 15 and (
                    screen.height() - 15 - self.height()) > self.y() > 15:
                self.isStopAt = False

    def enterEvent(self, e):
        self.isHover = True
        print('鼠标悬停于“ICON”')
        if self.isStopAt and self.x() < e.globalPosition().x() < self.x() + self.width() and self.y() < e.globalPosition().y() < self.y() + self.height() and ui.iconStopAt.isChecked():
            print("悬停")
            if self.x() < 0:
                self.move(0, self.y())
            elif self.x() > screen.width() - self.width():
                self.move(screen.width() - self.width(), self.y())
            if self.y() < 0:
                self.move(self.x(), 0)
            elif self.y() > screen.height() - self.height():
                self.move(self.x(), screen.height() - self.height())

    def leaveEvent(self, e):
        self.isHover = False

    def center(self):
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print('uleft')
            # self.dp_x = e.globalPosition() - self.pos()
            self.dp_x = e.globalPosition().x()
            self.dp_y = e.globalPosition().y()
            self.isMove = False
        elif e.button() == Qt.MouseButton.RightButton:
            print('uright')
        elif e.button() == Qt.MouseButton.MiddleButton:
            print('umiddle')

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print('dleft')
            if not self.isMove:
                ui.MaxWindow()
            self.isMove = False

        elif e.button() == Qt.MouseButton.RightButton:
            print('dright')
        elif e.button() == Qt.MouseButton.MiddleButton:
            print('dmiddle')
            self.close()

    def mouseMoveEvent(self, e):
        if Qt.MouseButton.LeftButton:
            self.isMove = True
            print('xmove')
            self.move(int(self.x() + (e.globalPosition().x() - self.dp_x)),
                      int(self.y() + (e.globalPosition().y() - self.dp_y)))
            self.dp_x = e.globalPosition().x()
            self.dp_y = e.globalPosition().y()
            print(self.pos())


def translate(texts):
    texts = texts.strip()
    if texts == "":
        return ""

    print("语言服务正在处理中，请耐心等待...")

    params = {"text": texts}
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except TypeError as e:
            print(f"错误: {e}")
            pass
    headers = {"Cookie": cookies}
    rep = requests.get("https://code.xueersi.com/api/ai/python_tts/translate", params=params, headers=headers)

    try:
        repDic = json.loads(rep.text)
    except:
        repDic = None

    if repDic is None:
        raise Exception("微软语言服务请求超时，请稍后再试")

    if repDic["stat"] != 1:
        raise Exception(repDic["msg"])

    print("语言服务处理完毕！")

    result = repDic["data"]["text"]
    return result


class Work(QThread):
    aiprint = pyqtSignal(str)
    logUpdate = pyqtSignal(str)
    CheckFileIntegrity_Pass = pyqtSignal(str)

    def __init__(self):
        super(Work, self).__init__()
        self.model = ""
        self.question = ""
        self.entozhcn = False
        self.inCode = False
        self.userId = -1

    class CheckFileIntegrityError(IOError):
        pass

    def run(self) -> None:
        # self.ainame.setText('XChatGPT-正在思考...')
        global text
        if self.model.startswith("notification"):
            model = self.model.split("|")[-1]
            if model.startswith("appStartInfo"):
                notification.notify(
                    title=f"XChatGPT-{version} 启动成功！",
                    message="原作者：陈思翰(XESID: 27141890)",
                    app_name="XChatGPT",
                    app_icon=getPath("logo.ico"),
                    timeout=int(model[-2])
                )
            elif model.startswith("cleanLog"):
                notification.notify(
                    title=f"已清除日志({int(model[-2])}行)",
                    message=strftime("%Y/%m/%d-%H:%M:%S"),
                    app_name="XChatGPT",
                    app_icon=getPath("logo.ico"),
                    timeout=2
                )
            elif model.startswith('Check_file_integrity'):
                t = ''
                model = json.loads(model.split('-')[-1])
                notification.notify(
                    title=f"XChatGPT-{version} 检查资源文件完整性......",
                    message=f"共{len(model)}个文件",
                    app_name="XChatGPT",
                    app_icon=getPath("logo.ico"),
                    timeout=1
                )
                for _m in model:
                    if not os.path.exists(getPath(_m)):
                        t = f"抱歉，文件“{_m}”在此计算机中找不到，请重新下载XChatGPT-{version}"
                    print(_m)
                if t == "":
                    self.sleep(6)
                self.CheckFileIntegrity_Pass.emit(t)
        else:
            try:
                print('您:', self.question)
                # self.loadingBox.setValue(5)
                # self.ainame.setText("XChatGPT-获取输入...")
                self.logUpdate.emit(strftime(f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]您: {self.question}\n"))
                # self.Print.setText(self.Print.toPlainText() + strftime(f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]您: {entry}\n"))
                # if self.question == "q":
                #     self.close()
                #     self.loadingBox.setValue(100)
                #     #self.ainame.setText("XChatGPT")
                if "/" in self.question:
                    self.question = re.sub('/', '', self.question)
                    if self.question == "get_ChatGPT_Web":
                        webbrowser.open("https://study.zwjjiaozhu.top/posts/chatgpt-mirror-sites.html#gpt3")
                    # self.loadingBox.setValue(100)
                    # self.ainame.setText("XChatGPT")
                else:
                    # self.loadingBox.setValue(15)
                    # self.ainame.setText("XChatGPT-连接资源...")
                    if self.model == "备用((有限制，不支持上下文))":
                        try:
                            res = requests.post(url="https://ai.usesless.com/api/chat-process",
                                                json={"prompt": self.question, "options": {
                                                    "systemMessage": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: " + str(
                                                        dt01.date()),
                                                    "completionParams": {"presence_penalty": 0.8,
                                                                         "temperature": 1}}}).text
                        except Exception as e:
                            # self.loadingBox.setValue(90)
                            # self.ainame.setText("XChatGPT-输出答复...")
                            self.chatGPT_say(str(e))
                            return
                        text = re.findall('"text":"(.*?)"', res)
                        print('a', text)
                        if text:
                            text = text[-1].replace(r'\n', '\n')
                            self.chatGPT_say(text)
                        else:
                            if json.loads(res)["status"] == "Fail":
                                self.chatGPT_say(
                                    "抱歉，由于该接口的限制，今日的调用次数为0\n可以尝试明天重新访问，或者访问网站ai.usesless.com查看更多信息")
                            else:
                                self.chatGPT_say("抱歉，该接口出现问题或接口无响应")
                    elif self.model == "默认(GPT-3.5 无限制)":
                        if self.userId != -1:
                            asyncio.run(self.main(self.question, self.userId, ui))
                        else:
                            text = "抱歉，您没有指定会话ID请选择或新建会话！"
                            self.chatGPT_say(text)
                        print("ChatGPT:", text)
                        self.logUpdate.emit(strftime(f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]ChatGPT: {text}\n\n"))
                        # text = _text
                    # self.loadingBox.setValue(70)
                    # self.ainame.setText("XChatGPT-输出答复...")
                    # if self.entozhcn:
                    #     # self.loadingBox.setValue(90)
                    #     self.chatGPT_say(translate(text))
                    # else:
                    #     # self.loadingBox.setValue(90)
                    #     self.chatGPT_say(text)

            except BaseException as e1:
                print(str(e1))

    async def send_message(self, session, url, data, headers, is_print=True):
        global text
        _text = ''
        print('chatGPT：', end='')
        async with session.post(url, json=data, headers=headers) as response:
            # print(response.text())
            async for chunk in response.content.iter_chunked(1024):
                # print(chunk.decode(),end='')
                if is_print:
                    _text += chunk.decode()
                    self.aiprint.emit(_text)
                # try:
                #     _lt = _text.split('\n')
                #     for _l, _i in (_lt, range(len(_lt))):
                #         _l.lstrip()
                #         if len(_l) > 4:
                #             if _l[:3] == "```":
                #                 self.inCode = True
                #                 _lt[_i] = '\033[100m\033[97m'+_lt[_i]+'\033[0m'
                #                 _text = '\n'.join(_lt)
                # except:
                #     pass
        text = _text
        print('\n')

    async def main(self, txt, id, ui):
        id = str(id)
        url = 'https://api.binjie.fun/api/generateStream'
        data = {'prompt': txt,
                'userId': '#/chat/' + id,
                'network': True,
                'system': "",
                'withoutContext': False,
                'stream': False
                }
        url1 = 'https://chat2.aichatos.top/#/chat/' + id
        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,eo;q=0.5',
            'Connection': 'keep-alive',
            'Origin': url1,
            'Referer': url1,
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        async with aiohttp.ClientSession() as session:
            await self.send_message(session, url, data, headers, ui)

    def chatGPT_say(self, text):
        print("ChatGPT:", text)
        self.logUpdate.emit(strftime(f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]ChatGPT: {text}\n\n"))
        for i in range(len(text)):
            self.aiprint.emit((text + '#')[:i + 1])
            time.sleep(random.uniform(0.085, 0.04))
        # win.aiprint.setText(text)
        # win.loadingBox.setValue(100)
        # win.ainame.setText("XChatGPT")


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowIcon(QIcon("logo.ico"))
        self.setWindowTitle(f"XChatGPT {version}")
        self.mouseClickMoveBox = False
        self.setupUi(self)
        self.retranslateUi(self)
        self.usericon.setPixmap(QPixmap(getPath('usericon.png')))
        self.usericon.setStyleSheet(f"icon: url({getPath('usericon.png')});")
        self.aiicon.setPixmap(QPixmap(getPath('openai.png')))
        self.aiicon.setStyleSheet(f"icon:url({getPath('openai.png')});")
        self.pushButton.clicked.connect(self.windowStop)
        self.MinButton.clicked.connect(self.MinWindow)
        self.DataInit.clicked.connect(lambda: dataInit(self))
        self.setWindowFlags(MSWindowsFixedSizeDialogHint | FramelessWindowHint)
        self.homeURLOK.clicked.connect(self.xeshomelogon)
        self.dp_x = None
        self.dp_y = None
        self.center()
        self.data = getData()
        self.username.setText(self.data['user-name'])
        self.xeshomeURL.setText(self.data['xes-home'])
        self.CleanLog.clicked.connect(self.cleanLog)
        self.Print.setText(self.data['log'])
        # self.aiicon.setStyleSheet("border-radius: 10px; border: 2px groove gray;border-style: outset;")
        # self.usericon.setStyleSheet("border-radius: 10px; border: 2px groove gray;border-style: outset;")
        self.username.setText(getPath(''))
        self.MoveBox.setText(f"XChatGPT-{version}")

        self.iconStopAt.setChecked(getData_k('iconStopAt'))
        self.sizeAnimation.setChecked(getData_k('sizeAnimation'))

        self.Icon = ICON()
        self.Icon.label.setPixmap(QPixmap(getPath('openai.png')))
        self.Icon.label.setScaledContents(True)
        self.Icon.label.resize(91, 91)
        self._w = self.width()
        self._h = self.height()
        self.sizeChange = False
        self.isMin = False

        self.uploader = XesUploaderWin()
        self.openXesUploader.clicked.connect(self.uploader.show)
        self.uploader.send_log[str].connect(self.logUpdate)

        self.setWindowOpacity(1)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.windowUpdate)
        self.timer.start(100)

        self.work = Work()
        self.work.logUpdate[str].connect(self.logUpdate)
        self.work.aiprint[str].connect(self.readAIPrint)
        self.work.started.connect(lambda: self.OK.setEnabled(False))
        self.work.finished.connect(lambda: self.OK.setEnabled(True))
        self.work.started.connect(lambda: self.entozhcn.setEnabled(False))
        self.work.finished.connect(lambda: self.entozhcn.setEnabled(True))

        self.entozhcn.stateChanged.connect(self.enToZhcn)

        for session_id in getData_k('sessionID'):
            self.session.addItem(session_id)

        self.newChat.clicked.connect(self.new_chat)
        self.delChat.clicked.connect(self.del_chat)

        self.AIType.currentTextChanged.connect(self.chat_model_change)

        self.cover = CoverWindow(self)
        self.cover.show()

    def chat_model_change(self, text):
        self.Print.setText(self.Print.toPlainText() + strftime(
            f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]已将模型设为“{text}”\n"))
        enabled = False
        if text == "默认(GPT-3.5 无限制)":
            enabled = True
        self.newChat.setEnabled(enabled)
        self.session.setEnabled(enabled)
        self.delChat.setEnabled(enabled)

    def del_chat(self):
        thisSession = self.session.currentText()
        if not thisSession.isnumeric():
            QMessageBox.warning(self, "无效的删除",
                                f"无效的删除，当前无选中会话！")
            return

        sessions = getData_k('sessionID')
        # 创建消息框

        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Warning)
        message_box.setWindowTitle("删除会话")
        message_box.setText(f"是否删除会话“{thisSession}”?")

        # 设置标准按钮
        message_box.setStandardButtons(QMessageBox.StandardButtons.Yes | QMessageBox.StandardButtons.No)
        # 显示消息框，并获取用户的选择结果
        message_box.exec()

        result = message_box.clickedButton().text()

        if result == "&Yes":
            sessions.remove(thisSession)
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]已将会话“{thisSession}”从会话列表里删除。\n"))
            changeData('sessionID', sessions)

            self.session.clear()
            for session_id in getData_k('sessionID'):
                self.session.addItem(session_id)
        elif result == "&No":
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]删除会话“{thisSession}”，取消。\n"))

    def new_chat(self):
        n = ""
        for _ in range(random.randint(10, 12)):
            digit = random.randint(0, 9)
            n += str(digit)
        try:
            sessions = getData_k('sessionID')
            while True:
                number, ok = QInputDialog.getText(self, "输入会话ID", "输入会话ID(10~12位):", text=n)

                if not ok:
                    self.Print.setText(self.Print.toPlainText() + strftime(
                        f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]“创建会话”取消。\n"))
                    return

                if number.isnumeric():
                    _number = int(number)
                    if 1000000000 <= _number <= 999999999999:
                        if number not in sessions:
                            QMessageBox.information(self, "创建成功", "创建成功，去会话列表看看吧！")
                            break
                        else:
                            QMessageBox.warning(self, "重复的ID", "该会话ID已存在！！！")
                            self.Print.setText(self.Print.toPlainText() + strftime(
                                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[ERROR]会话ID“{number}”已在会话列表中重复。\n"))
                    else:
                        QMessageBox.warning(self, "无效的输入",
                                            f"无效的输入，会话ID只能是10~12位数字！！！\n你输入了{len(number)}位。")
                        self.Print.setText(self.Print.toPlainText() + strftime(
                            f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[ERROR]用户输入的会话ID长度无效({len(number)}位)，应10~12位\n"))
                else:
                    QMessageBox.warning(self, "无效的输入", "无效的输入，会话ID只能包含数字！！！")
                    self.Print.setText(self.Print.toPlainText() + strftime(
                        f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[ERROR]用户输入的会话ID内容无效({number})，应只包含数字。\n"))
            sessions.append(number)
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]已将会话“{number}”添加到会话列表中。\n"))
            changeData('sessionID', sessions)

            self.session.clear()
            for session_id in getData_k('sessionID'):
                self.session.addItem(session_id)
        except Exception as e:
            print(str(e))

    def enToZhcn(self, state):
        if state:
            self.aiprint.setText(translate(self.aiprint.toPlainText()))
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]已将AI输出内容翻译。\n"))
        else:
            self.aiprint.setText(text)
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](XChatGPT)[INFO]已还原AI输出内容(取消翻译)。\n"))

    def logUpdate(self, newLog):
        self.Print.setText(self.Print.toPlainText() + newLog)
        changeData('log', self.Print.toPlainText())

    def readAIPrint(self, text):
        v = self.aiprint.verticalScrollBar().value()
        if self.aiprint.verticalScrollBar().value() == self.aiprint.verticalScrollBar().maximum():
            self.aiprint.setText(text)
            self.aiprint.verticalScrollBar().setValue(self.aiprint.verticalScrollBar().maximum())
        else:
            self.aiprint.setText(text)
            self.aiprint.verticalScrollBar().setValue(v)

    @pyqtSlot()
    def on_OK_clicked(self):
        self.entozhcn.setChecked(False)

        self.work.model = self.AIType.currentText()
        self.work.question = self.userinput.toPlainText()
        self.work.entozhcn = self.entozhcn.isChecked()
        if self.session.currentText() and self.session.currentText() != "" and self.session.currentText() != " ":
            self.work.userId = self.session.currentText()
        else:
            self.work.userId = -1
        self.work.start()

    def MinWindow(self):
        self.sizeChange = True
        self.isMin = True
        self.Icon.move(self.x(), self.y())
        self.Icon.show()
        if self.sizeAnimation.isChecked():
            self.minWindow()
        else:
            self.setWindowOpacity(0)
            self.resize(0, 0)
            self.close()

    def MaxWindow(self, isFollow=True):
        self.isMin = False
        self.show()
        if isFollow:
            self.move(self.Icon.x(), self.Icon.y())
        if self.sizeAnimation.isChecked():
            self.maxWindow()
        else:
            self.Icon.close()
            self.resize(self._w, self._h)
            if self.Icon.x() > screen.width() / 2 and self.Icon.y() < screen.height() / 2:
                self.move(self.x() - self.width() + self.Icon.width(), self.y())
            elif self.Icon.x() < screen.width() / 2 and self.Icon.y() > screen.height() / 2:
                self.move(self.x(), self.y() - self.height() + self.Icon.height())
            elif self.Icon.y() > screen.height() / 2 and self.Icon.x() > screen.width() / 2:
                self.move(self.x() - self.width() + self.Icon.width(), self.y() - self.height() + self.Icon.height())
            self.setWindowOpacity(1)
        self.sizeChange = False

    def minWindow(self):
        for _ in range(1, 11):
            self.resize(self.width() - (self._w // 10), self.height() - (self._h // 10))
            self.setWindowOpacity((10 - _) * (1 / 10))
            self.update()
            time.sleep(0.02)
        self.close()

    def maxWindow(self):
        for _ in range(1, 11):
            if self.Icon.x() > screen.width() / 2 and self.Icon.y() < screen.height() / 2:
                self.move((self.Icon.x() + self.Icon.width()) - (self.width() + (self._w // 10)), self.y())
            elif self.Icon.x() < screen.width() / 2 and self.Icon.y() > screen.height() / 2:
                self.move(self.x(), (self.Icon.y() + self.Icon.height()) - (self.height() + (self._h // 10)))
            elif self.Icon.y() > screen.height() / 2 and self.Icon.x() > screen.width() / 2:
                self.move((self.Icon.x() + self.Icon.width()) - (self.width() + (self._w // 10)),
                          (self.Icon.y() + self.Icon.height()) - (self.height() + (self._h // 10)))

            self.resize(self.width() + (self._w // 10), self.height() + (self._h // 10))
            self.update()
            self.setWindowOpacity(_ * (1 / 10))
            time.sleep(0.02)
        self.Icon.close()

    def cleanLog(self):
        # 创建消息框对象
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Warning)
        message_box.setWindowTitle("日志")
        message_box.setText("是否清除会话")
        # 设置标准按钮
        message_box.setStandardButtons(QMessageBox.StandardButtons.Yes | QMessageBox.StandardButtons.No)

        # 显示消息框，并获取用户的选择结果
        message_box.exec()

        result = message_box.clickedButton().text()
        print(result)

        if result == "&Yes":
            l = len(self.Print.toPlainText().split("\n"))
            self.work.model = f'notification|cleanLog({l})'
            self.Print.setText(strftime(f"[%Y/%m/%d-%H:%M:%S][INFO]XChatGPT {version} 输出日志\n\n"))
            changeData('log', strftime(f"[%Y/%m/%d-%H:%M:%S][INFO]XChatGPT {version} 输出日志\n\n"))

            self.work.start()

    def windowStop(self):
        self.timer.stop()
        self.close()
        app = QApplication.instance()
        app.quit()

    def center(self):
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def mousePressEvent(self, e):
        # apply_stylesheet(app, theme=getData_k('style'))  ---防卡---
        if e.button() == Qt.MouseButton.LeftButton:
            print('uleft')
            # self.dp_x = e.globalPosition() - self.pos()
            self.dp_x = e.globalPosition().x()
            self.dp_y = e.globalPosition().y()
        elif e.button() == Qt.MouseButton.RightButton:
            print('uright')
        elif e.button() == Qt.MouseButton.MiddleButton:
            print('umiddle')

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            print('dleft')
        elif e.button() == Qt.MouseButton.RightButton:
            print('dright')
        elif e.button() == Qt.MouseButton.MiddleButton:
            print('dmiddle')

    def mouseMoveEvent(self, e):
        if Qt.MouseButton.LeftButton:
            print('xmove')
            self.move(int(self.x() + (e.globalPosition().x() - self.dp_x)),
                      int(self.y() + (e.globalPosition().y() - self.dp_y)))
            self.dp_x = e.globalPosition().x()
            self.dp_y = e.globalPosition().y()
            print(self.pos())

    def xeshomelogon(self):
        changeData(k='style', v=self.styleBox.currentText() + '.xml')
        apply_stylesheet(app, theme=getData_k('style'))
        self.Print.setText(
            self.Print.toPlainText() + strftime(f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]将样式设置为: {getData_k('style')}\n"))
        if self.xeshomeURL.text().startswith("https://code.xueersi.com/space/") or self.xeshomeURL.text().startswith(
                "code.xueersi.com/space/"):
            _id = self.xeshomeURL.text()[31:]
            if self.xeshomeURL.text().startswith("code.xueersi.com/space/"):
                _id = 'https://' + _id
            while ('?' in _id) or (not (_id.endswith('0') or _id.endswith('1') or _id.endswith('2') or _id.endswith('3')
                                        or _id.endswith('4') or _id.endswith('5') or _id.endswith('6')
                                        or _id.endswith('7') or _id.endswith('8') or _id.endswith('9'))):
                _id = _id[:-1]
            try:
                self.username.setText(xesapi.get_user_info(_id)['data']['realname'])
            except:
                self.Print.setText(
                    self.Print.toPlainText() + strftime(f"[%Y/%m/%d-%H:%M:%S](设置)[ERROR]用户ID({_id})无效！！！\n"))
                self.xeshomeURL.setText(self.xeshomeURL.text() + f'-用户ID({_id})无效！！！\n')
                return
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]将用户名修改为: {getData_k('user-name')}\n主页链接: {getData_k('xes-home')}\n"))
            changeData('user-name', self.username.text())
            changeData("xes-home", self.xeshomeURL.text())
            # _p = xopen('XCHATGPTTEMP')
            # with open(_p+'', 'wb'):
            #
        else:
            if self.xeshomeURL.text() != "NULL":
                self.Print.setText(self.Print.toPlainText() + strftime(
                    f"[%Y/%m/%d-%H:%M:%S](设置)[ERROR]主页网址({self.xeshomeURL.text()})无效！！！\n"))
                self.xeshomeURL.setText(self.xeshomeURL.text() + '-网址无效！！！')

    def mouseClickMBox(self, event):
        if Qt.MouseButton.LeftButton:
            self.mouseClickMoveBox = True

    def windowUpdate(self):
        if getData_k('iconStopAt') != self.iconStopAt.isChecked():
            changeData('iconStopAt', self.iconStopAt.isChecked())
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]悬浮球停靠屏幕边缘{'开启' if self.iconStopAt.isChecked() else '关闭'}。\n"))
        if getData_k('sizeAnimation') != self.sizeAnimation.isChecked():
            changeData('sizeAnimation', self.sizeAnimation.isChecked())
            self.Print.setText(self.Print.toPlainText() + strftime(
                f"[%Y/%m/%d-%H:%M:%S](设置)[INFO]窗口大小化动画{'开启' if self.sizeAnimation.isChecked() else '关闭'}。\n"))

        self.username.setText(getData_k('user-name'))
        if getData_k('log') != self.Print.toPlainText():
            changeData('log', self.Print.toPlainText())

        if not self.sizeChange and self.isMin:
            self.resize(633, 767)
            self.setWindowOpacity(1)


class CoverWindow(QWidget):
    def __init__(self, base_window: QMainWindow):
        super(CoverWindow, self).__init__()
        self.baseWindow = base_window

        self.setWindowFlags(
            MSWindowsFixedSizeDialogHint | Qt.WindowType.WindowStaysOnTopHint | FramelessWindowHint | Qt.WindowType.Tool)

        # 设置窗口大小为图片大小
        self.resize(671, 414)

        # 加载图片并创建 QLabel 显示图片
        pixmap = QPixmap(getPath("cover.png"))
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)

        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

        self.baseWindow.setWindowOpacity(0)

        self.check_file_integrity()

    def checkFileIntegrity_Pass(self, t):
        if t != "":
            print('aaa')
            print(t)
            raise self.baseWindow.work.CheckFileIntegrityError(t)
        self.baseWindow.work.model = "notification|appStartInfo(3)"
        self.baseWindow.work.start()
        self.baseWindow.setWindowOpacity(1)
        self.close()

    def check_file_integrity(self):
        self.baseWindow.work.model = 'notification|Check_file_integrity-["openai.png","usericon.png","data.json","logo.ico","cover.png"]'
        self.baseWindow.work.CheckFileIntegrity_Pass[str].connect(self.checkFileIntegrity_Pass)
        self.baseWindow.work.start()


if __name__ == "__main__":
    from qt_material import apply_stylesheet

    app = QApplication(sys.argv)

    screen = QGuiApplication.primaryScreen().geometry()
    ui = Main()
    apply_stylesheet(app, theme=getData_k('style'))
    ui.show()
    sys.exit(app.exec())
