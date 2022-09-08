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

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# tips
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ・self.変数名とクラス名.変数名は揃えないとダメ
#       →フレームはselfで設定し、要素をクラス名で配置とかすると順番がズレて意図しない配置になる
# ・インスタンス化はむやみにしない
#       →引数selfには注意するべき

from ast import FunctionDef
from distutils.cmd import Command
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font
from turtle import clear, width
from types import ClassMethodDescriptorType
from typing_extensions import IntVar

# メインフレーム
root = tk.Tk()

# 現在の機能面管理
currentFunction = "Home"

# 各機能の基盤フレームをグローバル変数として宣言
drawHomeArea = tk.Frame(root)
drawTaskArea = tk.Frame(root)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ホーム画面描画
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drawHome():
        global drawHomeArea
        drawHomeArea = tk.Frame(root)
        drawHomeArea.pack(fill=tk.BOTH, expand=True)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # フレーム作成↓↓↓
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # 期間表示エリア-----------------------------------------------------------------
        # 期間表示エリア定義
        viewArea = tk.Frame(drawHomeArea, padx = 0, pady = 15, width = 5)
        viewArea.configure(bg="white")
        viewArea.pack(side = tk.TOP, anchor = tk.W, fill = tk.X)

        # 開始日表示エリア
        startArea = tk.Frame(viewArea, padx = 0, pady = 15,width = 5)
        startArea.configure(bg="white")
        start1 = tk.Label(startArea, text = "from", padx = 10)
        start1.configure(bg="white")
        start2 = tk.Label(startArea, text = "2022/09/22", font = ("normal", 13, "bold"), padx=10)
        start2.configure(bg="white")
        startArea.pack(side = tk.LEFT, fill="both", expand=True)

        # 終了日表示エリア
        endArea = tk.Frame(viewArea, padx = 0, pady = 15,width = 5)
        endArea.configure(bg="white")
        end1 = tk.Label(endArea, text = "to", padx = 10)
        end1.configure(bg="white")
        end2 = tk.Label(endArea, text = "2022/10/10", font = ("normal", 13, "bold"))
        end2.configure(bg="white")
        endArea.pack(side = tk.LEFT, fill="both", expand=True)
        # --------------------------------------------------------------------------------

        # ホーム----------------------------------------------------------
        homeArea = tk.Frame(drawHomeArea, padx = 0, pady = 15, width = 5)
        homeArea.configure(bg="white")
        homeArea.pack(side = tk.TOP, anchor = tk.W, fill="both")

        # ラベル
        tipsArea1 = tk.Frame(homeArea, padx = 0, pady =15,width = 5)
        tipsArea1.configure(bg="white")
        homeTips1 = tk.Label(tipsArea1, text = "task", padx = 15)
        homeTips1.configure(bg="white")
        tipsArea1.pack(side = tk.LEFT, fill="both", expand=True)

        tipsArea2 = tk.Frame(homeArea, padx = 0, pady =15,width = 5)
        tipsArea2.configure(bg="white")
        homeTips2 = tk.Label(tipsArea2, text = "allocation", padx=0)
        homeTips2.configure(bg="white")
        tipsArea2.pack(side = tk.LEFT, fill="both", expand=True)

        # タスク名と割り当て
        taskNameArea = tk.Frame(drawHomeArea, pady = 10)
        taskNameArea.configure(bg="white")
        taskName_home = tk.Label(taskNameArea, text = "タスク名", padx=10)
        taskName_home.configure(bg="white")
        taskNameArea.pack(side = tk.LEFT, fill="both", expand=True)

        allocationNameArea = tk.Frame(drawHomeArea, pady=10)
        allocationNameArea.configure(bg="white")
        allocationName_home = tk.Label(allocationNameArea, text="割り当て", padx=10)
        allocationName_home.configure(bg="white")
        allocationNameArea.pack(side = tk.LEFT, fill="both", expand=True)
        # ----------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 描画↓↓↓
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 設定された期間（期間表示エリア）------------------
        start1.pack()
        start2.pack()
        end1.pack()
        end2.pack()
        # -----------------------------------

        # 説明（ホーム）---------------------
        homeTips1.pack()
        homeTips2.pack()
        # --------------------------------------

        # タスク名------------------------------
        taskName_home.pack()
        allocationName_home.pack()
        # ----------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# タスク画面描画
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drawTask():
        global drawTaskArea
        drawTaskArea = tk.Frame(root)
        # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # # フレーム作成↓↓↓
        # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # # 機能名エリア--------------------------------------------------------------------
        drawTaskArea.pack(fill=tk.BOTH, expand=True)

        # タスク数決定エリア-----------------------------------------------------------------
        task = taskClass()

        amountOfTask = ("1", "2", "3", "4", "5", "6", "7")
        amountOfTaskArea = tk.Frame(drawTaskArea, padx=20, pady=40)
        amountOfTaskArea.configure(bg = "white")
        TextForAmountOfTask = tk.Label(amountOfTaskArea, text="total amount of task    :", font=normalFont)
        TextForAmountOfTask.configure(bg = "white")
        dropdownForAmountOfTask = ttk.Combobox(amountOfTaskArea, width=10, state="readonly", values=amountOfTask, textvariable=task.selectedAmountOfTask)
        # 初期値（=1）の設定
        dropdownForAmountOfTask.current(task.selectedAmountOfTask.get())
        confirmButton = tk.Button(drawTaskArea, text="confirm", command = task.reflectionInputValue)
        drawTaskArea.configure(bg="white")

        amountOfTaskArea.pack(side = tk.TOP, fill = tk.X)
        # ---------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 描画↓↓↓
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # タスク数（タスク数決定エリア）-----------------------
        TextForAmountOfTask.pack(side = tk.LEFT, fill="both", expand=True)
        dropdownForAmountOfTask.pack(side = tk.LEFT, fill="both", expand=True, padx=10)
        # dropdownForAmountOfTask.bind('<<ComboboxSelected>>', task.updateTask())
        dropdownForAmountOfTask.bind('<<ComboboxSelected>>', task.updateTaskForBind)
        # bindを記述する位置、()の有無、メソッド実行にワンクッション挟むと挙動が変わる--2022.09.07
        # ------------------------------------------------------------

        # 確定ボタン-----------------------------------------------------------------------
        confirmButton.pack(side = tk.BOTTOM, anchor=tk.E, padx=20, pady=10)
        # -----------------------------------------------------------------------------------

        # 初期画面描画
        task.updateTask()


# タスクタブ管理クラス
class taskClass:
        # 選択されたタスク数
        selectedAmountOfTask = tk.IntVar()
        # 選択値管理配列
        inputValueManager = []
        # 入力されたタスク名
        inputValueForTask = []

        # タスク名ラベル管理配列
        taskName = []
        # タスク名入力管理配列
        inputTask = []
        # 前回選択した値（初期値=0）
        previous = 0
        # タスク名ラベル設置エリア
        taskNameArea = tk.Frame(drawTaskArea)
        # タスク名入力設置エリア
        taskInputArea = tk.Frame(drawTaskArea)
        # タスク名ラベル共通フォント設定
        taskFont = tkinter.font.Font(
                taskNameArea,
                family="Bahnschrift",
                size=15,
                weight='bold'
        )                

        # タスク更新
        def updateTask(self):
                # グローバル変数宣言
                self.inputValueForTask.clear()
                # 現在選択値の保持
                counter = int(self.selectedAmountOfTask.get())            

                print(self.previous)

                # 初期表示(タスク名、入力エリアの配置)
                if self.previous == 0:
                        self.taskNameArea = tk.Frame(drawTaskArea)
                        self.taskNameArea.configure(bg="white")                                               
                        self.taskNameArea.pack(side=tk.LEFT, fill = "both", expand =True)

                        self.taskInputArea = tk.Frame(drawTaskArea)
                        self.taskInputArea.configure(bg="white")
                        self.taskInputArea.pack(side=tk.LEFT, fill = "both", expand =True)
                        
                # 配列の初期化
                for i1 in range(self.previous):
                        self.taskName[i1].pack_forget()                        
                        self.inputTask[i1].pack_forget()
                
                # 選択値を変更した時に値を保持するかどうか
                # 保持する場合はinputValueForTaskのlenが永遠に増加する（良くない）
                # self.inputValueForTask.clear()
                print("counter:"+str(counter))

                # 配列のインスタンス化
                self.taskName =[]
                self.inputTask = []      

                # ラベル、入力欄の設定、入力値の保持
                for i2 in range(counter):
                        # グローバル変数宣言
                        self.inputValueManager
                        # inputValueForTask配列の確保
                        self.inputValueForTask.append("dummy")

                        # 入力値管理配列（inputValueManager）にウィジェット変数を設置
                        # （目的：入力値を個別に管理するため）
                        self.inputValueManager.append(tk.StringVar())
                        
                        # 選択値に応じてラベルと入力欄を用意
                        self.taskName.append(tk.Label(self.taskNameArea, text="task"+str(i2+1), padx=25, font = self.taskFont))
                        self.inputTask.append(ttk.Entry(self.taskInputArea, font=self.taskFont, textvariable=self.inputValueManager[i2]))

                        # ラベルの設置
                        self.taskName[i2].pack(side = tk.TOP, anchor = tk.E, expand = True)
                        self.taskName[i2].configure(bg="white")

                        # 入力欄の設置
                        self.inputTask[i2].pack(side = tk.TOP, anchor = tk.W, expand = 1)

                # 選択値の引き継ぎ
                self.previous = counter
                print(self.previous)
                

        # bindで呼び出す用のタスク更新メソッド（不服）
        def updateTaskForBind(self, event):
                self.updateTask()

        # タスク名確定メソッド
        def reflectionInputValue(self):
                # グローバル変数宣言
                self.inputValueForTask
                self.inputValueManager
                self.selectedAmountOfTask
                # 選択値の保持
                counter = int(self.selectedAmountOfTask.get())                

                # グローバル変数inputValueForTaskへの反映
                for i2 in range(counter):
                        self.inputValueForTask[i2] = self.inputValueManager[i2].get()
                        print(self.inputValueForTask[i2])

# メインフレーム：機能名を表示している機能に応じて再描画するメソッド
def drawFunctionName():
        # 機能名エリア-----------------------------------------------------------------------------------------------------------------------------------------
        # 機能名エリア定義
        global functionNameArea
        global titleArea
        functionNameArea = tk.Frame(root, padx = 15, pady = 15, bd =1, relief=tk.RAISED)
        functionNameArea.configure(bg="white")

        # 機能名ボタンエリア定義
        buttonArea = tk.Frame(functionNameArea)
        buttonArea.configure(bg="white")

        # フォント定義
        global normalFont
        global underlineFont
        global functionFont     

        normalFont = tkinter.font.Font(
                buttonArea,
                family="Bahnschrift",
                size=10
        )
        underlineFont = tkinter.font.Font(
                buttonArea,
                family="Bahnschrift", 
                size = 12, 
                weight = 'bold', 
                underline = True
        )

        functionFont = [normalFont, normalFont, normalFont, normalFont, normalFont]

        # フォント設定処理
        if currentFunction == "Home":
                functionFont[0] = underlineFont
        elif currentFunction == "Task":
                functionFont[1] = underlineFont
        
        # 機能名ボタン定義
        functionName1 = tk.Button(buttonArea, font = functionFont[0], text = "Home", width = 10, relief = tk.FLAT, pady = 15)
        functionName1.configure(bg="white")
        functionName1.bind("<1>", currentFunctionManagement)
        functionName2 = tk.Button(buttonArea, font =functionFont[1], text = "Task", width = 10, relief = tk.FLAT, pady = 15)
        functionName2.configure(bg="white")
        functionName2.bind("<1>", currentFunctionManagement)
        functionName3 = tk.Button(buttonArea, font = functionFont[2], text = "Allocation", width = 10, relief = tk.FLAT, pady = 15)
        functionName3.configure(bg="white")
        functionName3.bind("<1>", currentFunctionManagement)
        functionName4 = tk.Button(buttonArea, font = functionFont[3], text = "Cycle", width = 10, relief = tk.FLAT, pady = 15)
        functionName4.configure(bg="white")
        functionName4.bind("<1>", currentFunctionManagement)
        functionName5 = tk.Button(buttonArea, font = functionFont[4], text = "Linkage", width = 10, relief = tk.FLAT, pady = 15)
        functionName5.configure(bg="white")
        functionName5.bind("<1>", currentFunctionManagement)

        # ウィジェットを配置→要素を配置
        functionNameArea.pack(side = tk.LEFT, fill = tk.Y)
        buttonArea.pack(side = tk.LEFT)
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------

        # タイトルエリア-----------------------------------------------------------------
        titleArea = tk.Frame(root, padx = 10, pady = 10, bd = 1, relief=tk.RAISED)
        title = tk.Label(titleArea, text = "title")

        titleArea.pack(side = tk.TOP, fill = tk.X)
        # --------------------------------------------------------------------------------

        # 機能名（機能名エリア）-------------------------------
        functionName1.pack(side = tk.TOP, anchor = tk.N, pady = 10)
        functionName2.pack(side = tk.TOP, anchor = tk.N, pady = 10)
        functionName3.pack(side = tk.TOP, anchor = tk.N, pady = 10)
        functionName4.pack(side = tk.TOP, anchor = tk.N, pady = 10)
        functionName5.pack(side = tk.TOP, anchor = tk.N, pady = 10)
        # --------------------------------------

        # タイトル（タイトルエリア）-------------------------
        title.pack(fill="both", expand=True)
        # -----------------------------------

# 機能名のフォントをノーマルに統一（リセット）するメソッド
def fontReset():
        for i in range(5):
                functionFont[i] = normalFont

# 押下された機能名を取得、管理するメソッド
def currentFunctionManagement(event):
        global currentFunction
        global drawHomeArea
        global drawTaskArea
        global functionFont

        previousFunction = currentFunction

        print(previousFunction)

        # 現在の機能名を管理変数に格納
        currentFunction = event.widget["text"]
        print(currentFunction)

        if not previousFunction == currentFunction:
                fontReset()
                functionNameArea.pack_forget()
                titleArea.pack_forget()
       
        # 前回の機能名に応じてフレーム（下地）を削除
        if previousFunction == currentFunction:
                # 同じボタンをクリックしたときは何もしない
                pass
        elif previousFunction == "Home":
                drawHomeArea.pack_forget()                                
        elif previousFunction == "Task":         
                drawTaskArea.pack_forget()           
        # elif previousFunction == "Allocation":                
        # elif previousFunction == "Cycle":                
        # elif previousFunction == "Linkage":                
        
        # 今回表示する機能エリアのフレーム（下地）を設定
        if previousFunction == currentFunction:
                # 同じボタンをクリックしたときは何もしない
                pass
        elif currentFunction == "Home":
                drawFunctionName()

                drawHomeArea = tk.Frame(root)                
                drawHome()
        elif currentFunction == "Task":          
                drawFunctionName()

                # ここで生成される引数self（taskClass）を引き継いで処理を行う
                # →設定されたパラメータ等を引き継いで処理を行いたいため
                drawTaskArea = tk.Frame(root)
                task = taskClass()
                task.previous = 0
                task.selectedAmountOfTask.set(0)
                drawTask()
        elif currentFunction == "Allocation":                
                drawFunctionName()
        elif currentFunction == "Cycle":                
                drawFunctionName()
        elif currentFunction == "Linkage":                
                drawFunctionName()

        for i in range(5):
                print(functionFont[i])
        
        print(underlineFont)
        
        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# メインウィンドウの設定
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":      
        
        root.title("taskManagement")
        root.geometry("600x600")
        root.resizable(False, False)
        root.configure(bg="white")       

        # 機能名一覧を描画
        drawFunctionName()

        # 最初はHome画面を開く
        drawHome()

        # メインフレームの描画
        root.mainloop()
        