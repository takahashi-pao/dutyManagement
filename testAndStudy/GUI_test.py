# # 参考サイト
# # http://pc-chem-basics.blog.jp/archives/24112647.html

# tkinterのインポート
# import tkinter as tk
# import tkinter.ttk as ttk


# # 関数の作成=>GUIよりも上に記述する必要がある
# # ディレクトリに注意
# def newtxt_func():
#     datafile = open("newtxt.txt","w")
#     test = "ok?"
#     datafile.write(test)
#     datafile.close()

# def selectValue(event):
#     value = combobox.get()

#     print(value+10)

# # ウインドウの作成
# root = tk.Tk()
# # ウインドウのサイズ指定
# root.geometry("350x100")

# # Runボタン設置
# # commandに関数newtxt_huncを設定
# run_button = tk.Button(root, text = "Run", command=newtxt_func)
# run_button.place(x = 160, y = 40)

# # Setボタン設置
# set_button = tk.Button(root, text = "Set", command = selectValue)
# set_button.place(x = 300, y = 7)

# # テキストボックス設置
# input_box = tk.Entry(width = 40)
# input_box.place(x = 10, y = 10)





# value = ("1", "2", "3", "4", "5", "6", "7")

# # ステータスバー設置
# # bd = 1 ：縁(ボーダー)の幅を1に指定 (値を大きくすると幅が広がります)
# # relief = tk.SUNKEN： 縁のスタイルを指定 (SUNKEN：親要素より沈んで表示)
# # anchor = tk.W： 配置可能なスペースに余裕がある場合、ウイジットをどこに配置するか指定 (W ：左よせ, E  : 右寄せ)
# statusbar = tk.Label(root, text =  " No Data!!", bd = 1, relief = tk.SUNKEN, anchor = tk.E)
# combobox = ttk.Combobox(root, state = "readonly", values = value)
# combobox.pack(side = tk.BOTTOM)
# # combobox.bind('<<ComboboxSelected>>', selectValue)
# # pack()メソッドはウイジットを順番に配置します。x, y座標で細かくウイジットの配置を決める必要がなく、存在するウイジットを単純に順番通り配置してよい場合などに用います。
# # 下から順番に配置、空いているスペースは横に広がって埋める
# statusbar.pack(side = tk.BOTTOM, fill = tk.X)

# # registerButton = tk.Button(text = "登録", command = lambda:print(combobox.get()))
# registerButton = ttk.Button(text = "登録")
# registerButton.bind('<<ComboboxSelected>>', selectValue)
# registerButton.pack()

# # ウインドウ状態の維持
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# # if __name__ == “__main__”:という記述は、そのPythonファイルが「pythonファイル名.py」という形で実行されているかどうか」を判定するif文=>importしただけで処理が行われることを防ぐ
# # モジュールとして読み込まれた場合に、__name__ には、モジュール名がセットされる
# # スクリプトとして実行される場合には__name__は__main__になる
# if __name__ == '__main__':
#     fruits = ['Apple', 'Banana', 'Grape']

#     root = Tk()
#     root.title('dropDownTest')

#     # Frame
#     frame = ttk.Frame(root, padding=10)
#     frame.grid()

#     # Combobox
#     # textvariableは値の保持であり、変数に格納等を行うにはこのオブジェクトに対しメソッドの実行が必要（ex. v.get())
#     v = StringVar()
#     cb = ttk.Combobox(
#         frame, textvariable=v, 
#         values=fruits, width=10, state = "readonly")
#     # 初期値の設定
#     cb.set(fruits[1])
#     # cb.bind(
#     #     '<<ComboboxSelected>>', 
#     #     lambda e: print('v=%s' % v.get()))
#     cb.grid(row=0, column=0)

#     # Button
#     button1 = ttk.Button(
#         frame, text='OK', 
#         #  print('v=%s' % v.get())の%sは文字列（%後の文字列）との置き換えを行う
#         command=lambda: print("selected="+v.get()))
#     button1.grid(row=0, column=2)

#     root.mainloop()



# ------------------------------------------------------------
# ラベル配置参考
# ------------------------------------------------------------
# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master = None):
#         super().__init__(master)

#         self.master.title("ウィジェットの配置(grid)")     # ウィンドウタイトル
#         self.master.geometry("300x180")       # ウィンドウサイズ(幅x高さ)

#         #--------------------------------------------------------
#         # ラベルの作成
#         label1 = tk.Label(self.master, text = "ラベル1", bg = 'cyan1')
#         label2 = tk.Label(self.master, text = "ラベル2", bg = 'green1')
#         label3 = tk.Label(self.master, text = "ラベル3", bg = 'yellow1')
#         label4 = tk.Label(self.master, text = "ラベル4", bg = 'pink1')
#         label5 = tk.Label(self.master, text = "ラベル5", bg = 'MediumPurple1')
#         label6 = tk.Label(self.master, text = "***ラベル6***", bg = 'LightSteelBlue1')

#         #--------------------------------------------------------
#         # gridでウィジェットの配置
#         label1.grid(row = 0, column = 1, columnspan = 3, sticky = tk.W+tk.E)
#         label2.grid(row = 0, column = 0, rowspan = 5, sticky = tk.N+tk.S)
#         label3.grid(row = 1, column = 1)
#         label4.grid(row = 1, column = 3)
#         label5.grid(row = 2, column = 2)
#         label6.grid(row = 3, column = 1, columnspan = 3)
#         #--------------------------------------------------------

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Application(master = root)
#     app.mainloop()

# 
# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master = None):
#         super().__init__(master)

#         self.master.title("ウィジェットの配置(grid)")     # ウィンドウタイトル
#         self.master.geometry("300x300")       # ウィンドウサイズ(幅x高さ)

#         #--------------------------------------------------------
#         # ラベルの作成
#         lbl_00 = tk.Label(self.master, text = "row,col")

#         lbl_col1 = tk.Label(self.master, text = "col1")
#         lbl_col2 = tk.Label(self.master, text = "col2")
#         lbl_col3 = tk.Label(self.master, text = "col3")

#         lbl_row1 = tk.Label(self.master, text = "row1")
#         lbl_row2 = tk.Label(self.master, text = "row2")
#         lbl_row3 = tk.Label(self.master, text = "row3")

#         #--------------------------------------------------------
#         # Entry(テキストボックス)の作成
#         entry1 = tk.Entry(self.master, width = 20)
#         entry2 = tk.Entry(self.master, width = 20)
#         entry3 = tk.Entry(self.master, width = 20)

#         #--------------------------------------------------------
#         # ボタンの作成
#         button1 = tk.Button(self.master, text = "...")
#         button2 = tk.Button(self.master, text = "...")
#         button3 = tk.Button(self.master, text = "...")

#         #--------------------------------------------------------
#         # gridでウィジェットの配置
#         lbl_00.grid(row = 0, column = 0)

#         lbl_col1.grid(row = 0, column = 1)
#         lbl_col2.grid(row = 0, column = 2)
#         lbl_col2.grid(row = 0, column = 3)

#         lbl_row1.grid(row = 1, column = 0)
#         lbl_row2.grid(row = 2, column = 0)
#         lbl_row3.grid(row = 3, column = 0)

#         entry1.grid(row = 1, column = 1, sticky=tk.EW) # 幅に合わせて大きくする
#         entry2.grid(row = 2, column = 1, sticky=tk.EW) # 幅に合わせて大きくする
#         entry3.grid(row = 3, column = 1, sticky=tk.EW) # 幅に合わせて大きくする

#         button1.grid(row = 1, column = 3)
#         button2.grid(row = 2, column = 3)
#         button3.grid(row = 3, column = 3)

#         #--------------------------------------------------------
#         # ウィンドウのリサイズに合わせてEntryの幅(column=1)を広げる
#         self.master.grid_columnconfigure(1, weight=1) # 列の調整
#         #self.master.grid_rowconfigure(1, weight=1) # 行の調整

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Application(master = root)
#     app.mainloop()

# gridを使うサンプル
# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master = None):
#         super().__init__(master)

#         self.master.title("ウィジェットの配置(grid)")     # ウィンドウタイトル
#         self.master.geometry("500x500")       # ウィンドウサイズ(幅x高さ)

#         #--------------------------------------------------------
#         # ラベルの作成
#         label0 = tk.Label(self.master, text = "ホーム")
#         label0_1 = tk.Label(self.master, text = "タスク")
#         label0_2 = tk.Label(self.master, text = "周期")

#         label1 = tk.Label(self.master, text = "項目1")
#         label1_1 = tk.Label(self.master, text = "項目1_1")
#         label1_2 = tk.Label(self.master, text = "項目1_2")
#         label1_3 = tk.Label(self.master, text = "項目1_3")

#         label2 = tk.Label(self.master, text = "項目2")
#         label2_1 = tk.Label(self.master, text = "項目2_1")
#         label2_2 = tk.Label(self.master, text = "項目2_2")
#         label2_3 = tk.Label(self.master, text = "項目2_3")

#         # テキストボックス(Entry)の作成
#         self.entry1_1 = tk.Entry(self.master, justify = tk.CENTER)
#         self.entry1_2 = tk.Entry(self.master, justify = tk.RIGHT)
#         self.entry1_3 = tk.Entry(self.master, justify = tk.RIGHT)

#         self.entry2_1 = tk.Entry(self.master, justify = tk.RIGHT)
#         self.entry2_2 = tk.Entry(self.master, justify = tk.RIGHT)
#         self.entry2_3 = tk.Entry(self.master, justify = tk.RIGHT)

        #--------------------------------------------------------
        # gridでウィジェットの配置
#         label0.grid(row = 2, column = 2, columnspan = 2)
#         label0_1.grid(row = 4, column = 2)
#         label0_2.grid(row = 6, column = 2)

#         label1.grid(row = 0, column = 4, columnspan = 2)
#         label1_1.grid(row = 1, column = 4); self.entry1_1.grid(row = 1, column = 5)
#         label1_2.grid(row = 2, column = 4); self.entry1_2.grid(row = 2, column = 5)
#         label1_3.grid(row = 3, column = 4); self.entry1_3.grid(row = 3, column = 5)

#         label2.grid(row = 5, column = 4, columnspan = 2)
#         label2_1.grid(row = 6, column = 4); self.entry2_1.grid(row = 6, column = 5)
#         label2_2.grid(row = 7, column = 4); self.entry2_2.grid(row = 7, column = 5)
#         label2_3.grid(row = 8, column = 4); self.entry2_3.grid(row = 8, column = 5)
#         #--------------------------------------------------------
#         #--------------------------------------------------------
#         # ウィンドウのリサイズに合わせてEntryの幅(column=1)を広げる
#         # self.master.grid_columnconfigure(1, pad = 5) # 列の調整
#         # self.master.grid_rowconfigure(1, minsize = 10) # 行の調整


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Application(master = root)
#     app.mainloop()

import tkinter as tk
import tkinter.ttk as ttk

# メインウィンドウの設定
root = tk.Tk()
root.title("taskManagement")
root.geometry("600x600")
root.resizable(False, False)

# 機能名エリア--------------------------------------------------------------------
functionNameArea = tk.Frame(root, padx = 15, pady = 15, bd =1, relief=tk.RAISED)

buttonArea = tk.Frame(functionNameArea)
functionName1 = tk.Button(buttonArea, text = "ホーム", width = 10, relief = tk.FLAT, pady = 15)
functionName2 = tk.Button(buttonArea, text = "タスク", width = 10, relief = tk.FLAT, pady = 15)
functionName3 = tk.Button(buttonArea, text = "割り当て", width = 10, relief = tk.FLAT, pady = 15)
functionName4 = tk.Button(buttonArea, text = "周期", width = 10, relief = tk.FLAT, pady = 15)
functionName5 = tk.Button(buttonArea, text = "連携", width = 10, relief = tk.FLAT, pady = 15)

# ウィジェットを配置→要素を配置
functionNameArea.pack(side = tk.LEFT, fill = tk.Y)
buttonArea.pack(side = tk.LEFT)
# --------------------------------------------------------------------------------

# タイトルエリア-----------------------------------------------------------------
titleArea = tk.Frame(root, padx = 10, pady = 10, bd = 1, relief=tk.RAISED)
title = tk.Label(titleArea, text = "title")

titleArea.pack(side = tk.TOP, fill = tk.X)
# --------------------------------------------------------------------------------

# 期間表示エリア-----------------------------------------------------------------
viewArea = tk.Frame(root, padx = 5, pady = 15, width = 5)
viewArea.pack(side = tk.TOP, anchor = tk.W, fill = tk.X)

startArea = tk.Frame(viewArea, padx = 0, pady = 15)
start1 = tk.Label(startArea, text = "from", padx = 10)
start2 = tk.Label(startArea, text = "2022/09/22", font = ("normal", 13, "bold"))
startArea.pack(side = tk.LEFT, fill="both", expand=True)

endArea = tk.Frame(viewArea, padx = 0, pady = 15)
end1 = tk.Label(endArea, text = "to", padx = 10)
end2 = tk.Label(endArea, text = "2022/10/10", font = ("normal", 13, "bold"))
endArea.pack(side = tk.LEFT, fill="both", expand=True)
# --------------------------------------------------------------------------------

# ホーム　メイン機能----------------------------------------------------------
homeArea = tk.Frame(root, padx = 0, pady =5)
homeArea.pack(side = tk.TOP, fill = tk.X)

tipsArea1 = tk.Frame(homeArea, padx = 0, pady =15)
homeTips1 = tk.Label(tipsArea1, text = "task", padx = 10)
tipsArea1.pack(side = tk.LEFT, fill="both", expand=True)

tipsArea2 = tk.Frame(homeArea, padx = 0, pady =15)
homeTips2 = tk.Label(tipsArea2, text = "allocation", padx = 10)
tipsArea2.pack(side = tk.LEFT, fill="both", expand=True)

# タスク名と割り当て
taskNameArea = tk.Frame(root, pady = 10)
taskNameArea.pack(side = tk.TOP, fill = tk.X)

taskName = tk.Label(taskNameArea)
# ----------------------------------------------------------------------------------

# 機能名-------------------------------
functionName1.pack(side = tk.TOP, anchor = tk.N, pady = 10)
functionName2.pack(side = tk.TOP, anchor = tk.N, pady = 10)
functionName3.pack(side = tk.TOP, anchor = tk.N, pady = 10)
functionName4.pack(side = tk.TOP, anchor = tk.N, pady = 10)
functionName5.pack(side = tk.TOP, anchor = tk.N, pady = 10)
# --------------------------------------

# タイトル-------------------------
title.pack(fill="both", expand=True)
# -----------------------------------

# 設定された期間------------------
start1.pack()
start2.pack()
end1.pack()
end2.pack()
# -----------------------------------

# 説明---------------------
homeTips1.pack()
homeTips2.pack()
# --------------------------

root.mainloop()