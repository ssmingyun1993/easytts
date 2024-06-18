import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_text_lxkg6ybz = self.__tk_text_lxkg6ybz(self)
        self.tk_button_lxkg83n3 = self.__tk_button_lxkg83n3(self)
        self.tk_select_box_lxkg8iwv = self.__tk_select_box_lxkg8iwv(self)
        self.tk_label_lxkg8pvz = self.__tk_label_lxkg8pvz(self)
        self.tk_label_lxkg9gbz = self.__tk_label_lxkg9gbz(self)
        self.tk_input_lxkga19j = self.__tk_input_lxkga19j(self)
    def __win(self):
        self.title("文本转语音")
        # 设置窗口大小、居中
        width = 812
        height = 475
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_text_lxkg6ybz(self,parent):
        text = Text(parent)
        text.place(x=2, y=6, width=562, height=459)
        return text
    def __tk_button_lxkg83n3(self,parent):
        btn = Button(parent, text="开始转换", takefocus=False,)
        btn.place(x=580, y=373, width=148, height=30)
        return btn
    def __tk_select_box_lxkg8iwv(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("zh-CN-XiaoxiaoNeural",
                        "zh-CN-XiaoyiNeural",
                        "zh-CN-YunjianNeural",
                        "zh-CN-YunxiNeural",
                        "zh-CN-YunxiaNeural",
                        "zh-CN-YunyangNeural",
                        "zh-CN-liaoning-XiaobeiNeural",
                        "zh-CN-shaanxi-XiaoniNeural")
        cb.place(x=580, y=231, width=150, height=30)
        return cb
    def __tk_label_lxkg8pvz(self,parent):
        label = Label(parent,text="选择声音",anchor="center", )
        label.place(x=580, y=186, width=50, height=30)
        return label
    def __tk_label_lxkg9gbz(self,parent):
        label = Label(parent,text="选择声音保存位置",anchor="center", )
        label.place(x=578, y=79, width=121, height=30)
        return label
    def __tk_input_lxkga19j(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=580, y=125, width=214, height=33)
        return ipt
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.config(menu=self.create_menu())
        self.ctl.init(self)
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="帮助",command=self.ctl.menu_help)
        return menu
    def __event_bind(self):
        self.tk_button_lxkg83n3.bind('<Button-1>',self.ctl.start_convert)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()