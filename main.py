import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QDir
from Ui_ui import Ui_mainWindow
import edge_tts
from edge_tts import VoicesManager
import asyncio
from datetime import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
import os

async def update_character(comboBox) -> None:
    """Main function"""
    voices = await VoicesManager.create()
    voice = voices.find(Gender="Male", Language="zh")
    for character in voice:
        if 'zh-cn' in character['ShortName'].lower():
            comboBox.addItem("男 " + character['ShortName'])

    voice = voices.find(Gender="Female", Language="zh")
    for character in voice:
        if 'zh-cn' in character['ShortName'].lower():
            comboBox.addItem("女 " + character['ShortName'])


# 定义一个线程类，继承自 QThread  
class WorkerThread(QThread):  
    # 定义一个信号，用于在主线程中更新文本  

    def setpara(self,path, txt, voc):
        self.path = path
        self.txt = txt
        self.voc = voc

    result_ready = pyqtSignal(str)

  
    def run(self):  
        """线程执行的函数"""  
        communicate = edge_tts.Communicate(self.txt, self.voc)
        communicate.save_sync(self.path)
        result = "完成"  
        # 发出信号，通知主线程  
        self.result_ready.emit(result) 

        

class MyApp(QMainWindow, Ui_mainWindow):
    def __init__(self, parent = None):
        super(MyApp, self).__init__(parent)
        self.setupUi(self)
        asyncio.run(update_character(self.comboBox))
        self.lineEdit.setText(QDir.currentPath())

        self.pushButton_select_dir.clicked.connect(self.pushButton_select_dir_Clicked)
        self.pushButton_start.clicked.connect(self.pushButton_start_Clicked)
        self.pushButtonlisten.clicked.connect(self.pushButtonlisten_Clicked)
        

        self.thread = WorkerThread()  
        self.isListening = False
        self.tmpPath = ""
        # 连接线程的信号到槽函数  
        self.thread.result_ready.connect(self.on_result_ready)  

    def pushButton_select_dir_Clicked(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.lineEdit.setText(folder_path)

    def pushButton_start_Clicked(self):
        if not QFileInfo(self.lineEdit.text()).isDir():
            QMessageBox.warning(None, "错误", "保存路径不合法！")
            return 

        if len(self.textEdit.toPlainText()) == 0:
            QMessageBox.warning(None, "错误", "请输入文本！")
            return

        voc = self.comboBox.currentText().replace("男 ", "")
        voc = voc.replace("女 ", "")

        
        date = datetime.now()
        formatted_date = date.strftime("%Y%d%m%H%M%S")

        if self.lineEdit.text()[-1] == '/':
            path = self.lineEdit.text() + formatted_date + ".mp3"
        else:
            path = self.lineEdit.text() + '/' + formatted_date+".mp3"

        txt = self.textEdit.toPlainText()

        self.thread.setpara(path, txt, voc)

        self.thread.start() 
        self.pushButton_start.setEnabled(False)

    def on_result_ready(self, result):  
        if result == "完成":
            self.pushButton_start.setEnabled(True)
            self.thread.quit()  
            self.thread.wait()  

    def pushButtonlisten_Clicked(self):
        self.tmpPath = QDir.currentPath()+ '/.tmp.mp3'
        if len(self.textEdit.toPlainText()) == 0:
            QMessageBox.warning(None, "错误", "请输入文本！")
            return
        txt = self.textEdit.toPlainText()
        if(len(txt) > 20):
            txt = txt[:20]
        voc = self.comboBox.currentText().replace("男 ", "")
        voc = voc.replace("女 ", "")
        if self.isListening:
            return
        self.isListening = True
        communicate = edge_tts.Communicate(txt, voc)
        communicate.save_sync(self.tmpPath)
        player = QMediaPlayer(self)
        player.stateChanged.connect(self.handle_state_changed)
        player.setMedia(QMediaContent(QUrl.fromLocalFile(self.tmpPath)))
        player.play()
        
        

    def handle_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            os.remove(self.tmpPath)
            self.isListening = False




 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())