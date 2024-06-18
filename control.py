import edge_tts
import asyncio
import os
from tkinter import messagebox


async def convert_voice(pre_text,pre_voice,out_put_file) -> None:  
    communicate = edge_tts.Communicate(pre_text, pre_voice)  
    await communicate.save(out_put_file)


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def menu_help(self):
        print("version0.1")

    def start_convert(self,evt):
        txt = self.ui.tk_text_lxkg6ybz.get('0.0','end').rstrip()
        voc = self.ui.tk_select_box_lxkg8iwv.get()
        loc = self.ui.tk_input_lxkga19j.get()

        if(len(txt) == 0):
            return
        
        if(len(voc) == 0):
            return

        if os.path.isdir(loc):
            asyncio.run(convert_voice(txt, voc, loc+("convert.mp3")))
        else:
            messagebox.showerror(title='错误', message='请输入要保存的文件地址，如 C:\\Users\\Administrator\\Documents\\')         # 提出错误对话窗
            return










