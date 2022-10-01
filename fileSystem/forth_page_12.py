import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import deal_with_file as df

# 第四层界面
from fileSystem.widgets import *


class window4_1():
    def __init__(self, info_dic):
        super().__init__()
        window = tk.Tk()

        # 给窗口的可视化起名字
        window.title('认证文件管理系统')
        window.config(background='Lavender')

        window.geometry('1280x650')  # 这里的乘是小x

        container = tk.Frame(window, background='Lavender')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.info_dic = info_dic

        for F in (cpgxPage, cpczPage, cpxxPage, qtxxPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(cpgxPage)
        window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


class cpgxPage(tk.Frame):
    """主页"""

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpgx1 = AddText(self, "产品1工序", "工序", "修改产品1工序", [120])
        self.cpgx2 = AddText(self, "产品2工序", "工序", "修改产品2工序", [120])
        self.cpgx3 = AddText(self, "产品3工序", "工序", "修改产品3工序", [120])
        self.cpgx4 = AddText(self, "产品4工序", "工序", "修改产品4工序", [120])
        self.cpgx5 = AddText(self, "产品5工序", "工序", "修改产品5工序", [120])

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)
        self.cpgx1.set_position(row=1, column=0, rowspan=4, columnspan=4)
        self.cpgx2.set_position(row=5, column=0, rowspan=4, columnspan=4)
        self.cpgx3.set_position(row=9, column=0, rowspan=4, columnspan=4)
        self.cpgx4.set_position(row=13, column=0, rowspan=4, columnspan=4)
        self.cpgx5.set_position(row=17, column=0, rowspan=4, columnspan=4)


class cpxxPage(tk.Frame):
    """主页"""

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpxx1 = AddText(self, "产品1信息", "生产产品1的", "修改产品1工序", [15, 12, 8, 12, 15],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户'])
        self.cpxx2 = AddText(self, "产品2信息", "生产产品2的", "修改产品2工序", [15, 12, 8, 12, 15],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户'])
        self.cpxx3 = AddText(self, "产品3信息", "生产产品3的", "修改产品3工序", [15, 12, 8, 12, 15],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户'])
        self.cpxx4 = AddText(self, "产品4信息", "生产产品4的", "修改产品4工序", [15, 12, 8, 12, 15],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户'])
        self.cpxx5 = AddText(self, "产品5信息", "生产产品5的", "修改产品5工序", [15, 12, 8, 12, 15],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户'])

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)
        self.cpxx1.set_position(row=1, column=0, rowspan=4, columnspan=4)
        self.cpxx2.set_position(row=5, column=0, rowspan=4, columnspan=4)
        self.cpxx3.set_position(row=9, column=0, rowspan=4, columnspan=4)
        self.cpxx4.set_position(row=13, column=0, rowspan=4, columnspan=4)
        self.cpxx5.set_position(row=17, column=0, rowspan=4, columnspan=4)


class cpczPage(tk.Frame):
    """主页"""

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpcz1 = AddText(self, "产品1操作工", "操作工", "修改产品1操作工", [120])
        self.cpcz2 = AddText(self, "产品2操作工", "操作工", "修改产品2操作工", [120])
        self.cpcz3 = AddText(self, "产品3操作工", "操作工", "修改产品3操作工", [120])
        self.cpcz4 = AddText(self, "产品4操作工", "操作工", "修改产品4操作工", [120])
        self.cpcz5 = AddText(self, "产品5操作工", "操作工", "修改产品5操作工", [120])

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)
        self.cpcz1.set_position(row=1, column=0, rowspan=4, columnspan=4)
        self.cpcz2.set_position(row=5, column=0, rowspan=4, columnspan=4)
        self.cpcz3.set_position(row=9, column=0, rowspan=4, columnspan=4)
        self.cpcz4.set_position(row=13, column=0, rowspan=4, columnspan=4)
        self.cpcz5.set_position(row=17, column=0, rowspan=4, columnspan=4)


class qtxxPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.jyy1 = EditText(self, '检验员1')
        self.jyy1.text_setting(height=1, width=25)

        self.scbry1 = EditText(self, '生产部人员1')
        self.scbry1.text_setting(height=1, width=25)

        self.scbry2 = EditText(self, '生产部人员2')
        self.scbry2.text_setting(height=1, width=25)

        self.scbry3 = EditText(self, '生产部人员3')
        self.scbry3.text_setting(height=1, width=25)

        self.tsgcjb = GroupButtonWithText(self, "有无搅拌过程", "有搅拌过程", "无搅拌过程", "特殊过程搅拌搅拌工")
        self.tsgcbmjsh = GroupButtonWithText(self, "有无薄膜金属化过程", "有薄膜金属化过程", "无薄膜金属化过程",
                                             "特殊过程薄膜金属化操作工")
        self.tsgchj = GroupButtonWithText(self, "有无焊接过程", "有焊接过程", "无焊接过程", "特殊过程焊接操作工")
        self.tsgchh = GroupButtonWithText(self, "有无混合过程", "有混合过程", "无混合过程", "特殊过程混合操作工")
        self.tsgcjc = GroupButtonWithText(self, "有无挤出过程", "有挤出过程", "无挤出过程", "特殊过程挤出操作工")

        self.sjaqjyspxr1 = EditText(self, '三级安全教育受培训人1')
        self.sjaqjyspxr1.text_setting(height=1, width=25)
        self.sjaqjyspxr2 = EditText(self, '三级安全教育受培训人2')
        self.sjaqjyspxr2.text_setting(height=1, width=25)
        self.sjaqjyrq1 = EditText(self, '三级安全教育第一天日期')
        self.sjaqjyrq1.text_setting(height=1, width=12)
        self.sjaqjyrq2 = EditText(self, '三级安全教育第二天日期')
        self.sjaqjyrq2.text_setting(height=1, width=12)
        self.sjaqjyrq3 = EditText(self, '三级安全教育第三天日期')
        self.sjaqjyrq3.text_setting(height=1, width=12)
        self.sjaqjybzpxr = EditText(self, '三级安全教育班组培训人')
        self.sjaqjybzpxr.text_setting(height=1, width=12)
        self.kyj = GroupButton(self, "有无空压机", "有空压机", "无空压机")

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4, columnspan=2)
        self.jyy1.set_position(row=1, column=0, columnspan=2)
        self.scbry1.set_position(row=2, column=0, columnspan=2)
        self.scbry2.set_position(row=2, column=2, columnspan=2)
        self.scbry3.set_position(row=2, column=4, columnspan=2)
        self.tsgcjb.set_position(row=3, column=0, rowspan=2, columnspan=6)
        self.tsgcbmjsh.set_position(row=5, column=0, rowspan=2, columnspan=6)
        self.tsgchj.set_position(row=7, column=0, rowspan=2, columnspan=6)
        self.tsgchh.set_position(row=9, column=0, rowspan=2, columnspan=6)
        self.tsgcjc.set_position(row=11, column=0, rowspan=2, columnspan=6)
        self.sjaqjyspxr1.set_position(row=13, column=0, rowspan=1, columnspan=2)
        self.sjaqjyspxr2.set_position(row=13, column=2, rowspan=1, columnspan=2)
        self.sjaqjyrq1.set_position(row=14, column=0, rowspan=1, columnspan=2)
        self.sjaqjyrq2.set_position(row=14, column=2, rowspan=1, columnspan=2)
        self.sjaqjyrq3.set_position(row=14, column=4, rowspan=1, columnspan=2)
        self.sjaqjybzpxr.set_position(row=15, column=0, rowspan=1, columnspan=2)
        self.kyj.set_position(row=15, column=2, rowspan=1, columnspan=2)


window4_1({})