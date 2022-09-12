import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font

# メインフレーム
root = tk.Tk()

# 現在の機能面管理
currentFunction = "Home"

# 各機能の基盤フレームをグローバル変数として宣言
drawHomeArea = tk.Frame(root)
drawTaskArea = tk.Frame(root)
drawAllocationArea = tk.Frame(root)
inputTask_home = []
inputAllocation_home = []
amountTask_home = 0

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ホーム画面描画
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drawHome():
        global drawHomeArea        
        drawHomeArea = tk.Frame(root)
        drawHomeArea.pack(fill=tk.BOTH, expand=True)

        global inputTask_home
        # inputTask_home = []
        print("タスク選択数" + str(len(inputTask_home)))
        global amountTask_home
        print("確定されたタスク数" + str(amountTask_home))

        home = homeClass()
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

        # # タスク名と割り当て
        global taskNameArea_home
        taskNameArea_home = tk.Frame(drawHomeArea, pady = 10)
        taskNameArea_home.configure(bg="white")
        # taskName_home = tk.Label(taskNameArea, text = "タスク名", padx=10)
        # taskName_home.configure(bg="white")
        taskNameArea_home.pack(side = tk.LEFT, fill="both", expand=True)

        global allocationNameArea_home
        allocationNameArea_home = tk.Frame(drawHomeArea, pady=10)
        allocationNameArea_home.configure(bg="white")
        # allocationName_home = tk.Label(allocationNameArea, text="割り当て", padx=10)
        # allocationName_home.configure(bg="white")
        allocationNameArea_home.pack(side = tk.LEFT, fill="both", expand=True)
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
        # taskName_home.pack()
        # allocationName_home.pack()
        # ----------------------------------------
        home.updateHome()

class homeClass:
        # グローバル変数宣言
        global drawHomeArea
        global inputTask_home
        global inputAllocation_home
        global taskNameArea_home
        global allocationNameArea_home
        # タスク、割り当てフレームの初期化
        taskNameArea_home = tk.Frame(drawHomeArea, pady = 10)
        allocationNameArea_home = tk.Frame(drawHomeArea, pady=10)
        # タブを切り替える前に選択していたタスク数
        previousSelected = 0
        # 選択値管理配列
        inputValueManager = []
        # 入力されたタスク名
        inputValueForTask = []
        # 実行フラグ
        flag = 0
        # タスク名ラベル管理配列
        taskName_home = []
        # タスク名入力管理配列
        allocationName_home = []
        # 前回選択した値（初期値=0）
        previous = 0
        # タスク名ラベル共通フォント設定
        taskFont = tkinter.font.Font(
                taskNameArea_home,
                family="Bahnschrift",
                size=20,
                weight='bold'
        )         
        allocationFont = tkinter.font.Font(
                allocationNameArea_home,
                family="Bahnschrift",
                size=15
        )

        # タスク更新
        def updateHome(self):                        
                # 配列の初期化
                for i1 in range(self.previous):
                        self.taskName_home[i1].pack_forget()                        
                        self.allocationName_home[i1].pack_forget()
                
                # 選択値を変更した時に値を保持するかどうか
                # 保持する場合はinputValueForTaskのlenが永遠に増加する（良くない）
                # self.inputValueForTask.clear()

                # 配列のインスタンス化
                self.taskName_home =[]
                self.allocationName_home = []                

                # ラベル、入力欄の設定、入力値の保持
                # 変数counterの値に応じて描画を行う
                for i2 in range(amountTask_home):
                        # 変数の提示
                        self.inputValueManager
                        # # inputValueForTask配列の確保
                        # self.inputValueForTask.append("dummy")
                        
                        inputTask_home.append("default")
                        inputAllocation_home.append("default")

                        # # 入力値管理配列（inputValueManager）にウィジェット変数を設置
                        # # （目的：入力値を個別に管理するため）
                        # self.inputValueManager.append(tk.StringVar())

                        # タスク名、割り当て名の引き継ぎ
                        viewText = inputTask_home[i2]
                        allocation = inputAllocation_home[i2]
                        # 引き継ぐタスク名がない場合
                        if inputTask_home[i2] == "":
                                viewText = "Not is set..."

                        # 選択値に応じてラベルと入力欄を用意
                        self.taskName_home.append(tk.Label(taskNameArea_home, text=viewText, font = self.taskFont))
                        self.allocationName_home.append(tk.Label(allocationNameArea_home, font=self.allocationFont, text= allocation))

                        # ラベルの設置
                        self.taskName_home[i2].pack(side = tk.TOP, fill="both", expand=True)
                        self.taskName_home[i2].configure(bg="white")

                        # 入力欄の設置
                        self.allocationName_home[i2].pack(side = tk.TOP, fill="both", expand=True)
                        self.allocationName_home[i2].configure(bg = "white")

                if self.flag == 0:
                        # 選択値に応じてラベルと入力欄を用意
                        self.taskName_home.append(tk.Label(taskNameArea_home, text="Not is set...", font = self.taskFont))
                        self.allocationName_home.append(tk.Label(allocationNameArea_home, font=self.allocationFont, text= "Not is set..."))

                        # ラベルの設置
                        self.taskName_home[0].pack(side = tk.TOP, fill="both", expand=True)
                        self.taskName_home[0].configure(bg="white")

                        # 入力欄の設置
                        self.allocationName_home[0].pack(side = tk.TOP, fill="both", expand=True)
                        self.allocationName_home[0].configure(bg = "white")
                

        # bindで呼び出す用のタスク更新メソッド（不服）
        def updateHomeForBind(self, event):
                self.updateHome()       

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
        dropdownForAmountOfTask = ttk.Combobox(amountOfTaskArea, width=10, state="readonly", values=amountOfTask, textvariable=selectedAmountOfTask)
        # 初期値の設定
        try:
                dropdownForAmountOfTask.current(selectedAmountOfTask.get())
        except:
                dropdownForAmountOfTask.current(amountTask_home)


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
        global selectedAmountOfTask
        selectedAmountOfTask = tk.IntVar()
        # タブを切り替える前に選択していたタスク数
        previousSelected = 0
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
                inputTask_home.clear()
                # self.inputValueManager.clear()
                # 現在選択値の保持
                counter = int(selectedAmountOfTask.get())            
                self.previousSelected = counter
                print("入力値"+str(len(self.inputValueManager)))
                print("タスク更新：確定タスク数" + str(amountTask_home))

                # 初期表示(タスク名、入力エリアの配置)
                if self.previous == 0:
                        self.taskNameArea = tk.Frame(drawTaskArea)
                        self.taskNameArea.configure(bg="white")                                               
                        self.taskNameArea.pack(side=tk.LEFT, fill = "both", expand =True)

                        self.taskInputArea = tk.Frame(drawTaskArea)
                        self.taskInputArea.configure(bg="white")
                        self.taskInputArea.pack(side=tk.LEFT, fill = "both", expand =True)

                        check = amountTask_home
                        
                # 配列の初期化
                for i1 in range(self.previous):
                        self.taskName[i1].pack_forget()                        
                        self.inputTask[i1].pack_forget()
                
                # 選択値を変更した時に値を保持するかどうか
                # 保持する場合はinputValueForTaskのlenが永遠に増加する（良くない）
                # self.inputValueForTask.clear()
                # print("counter:"+str(counter))

                # 配列のインスタンス化
                self.taskName =[]
                self.inputTask = []                

                # ラベル、入力欄の設定、入力値の保持
                # 変数counterの値に応じて描画を行う
                for i2 in range(counter):
                        # 変数の提示
                        self.inputValueManager
                        # inputValueForTask配列の確保
                        self.inputValueForTask.append("dummy")

                        # 入力値管理配列（inputValueManager）にウィジェット変数を設置
                        # （目的：入力値を個別に管理するため）
                        self.inputValueManager.append(tk.StringVar())
                        
                        # 選択値に応じてラベルと入力欄を用意
                        self.taskName.append(tk.Label(self.taskNameArea, text="task"+str(i2+1), padx=25, font = self.taskFont))
                        self.inputTask.append(ttk.Entry(self.taskInputArea, font=self.taskFont, textvariable=self.inputValueManager[i2]))
                        inputTask_home.append(str(self.inputValueManager[i2].get()))

                        # ラベルの設置
                        self.taskName[i2].pack(side = tk.TOP, anchor = tk.E, expand = True)
                        self.taskName[i2].configure(bg="white")

                        # 入力欄の設置
                        self.inputTask[i2].pack(side = tk.TOP, anchor = tk.W, expand = 1)

                # 選択値の引き継ぎ
                self.previous = counter
                # print(self.previous)
                # print(self.previousSelected)
                

        # bindで呼び出す用のタスク更新メソッド（不服）
        def updateTaskForBind(self, event):
                self.updateTask()

        # タスク名確定メソッド
        def reflectionInputValue(self):
                # グローバル変数宣言
                self.inputValueForTask
                self.inputValueManager
                global amountTask_home
                global inputTask_home
                # 選択値の保持
                counter = int(selectedAmountOfTask.get())
                print("選択されたタスク数（確定ボタン押下）："+ str(len(inputTask_home)))
                print("入力値（確定ボタン押下）：" + str(len(self.inputValueManager)))

                # グローバル変数inputValueForTaskへの反映
                for i2 in range(counter):
                        self.inputValueForTask[i2] = self.inputValueManager[i2].get()
                        inputTask_home[i2] = self.inputValueManager[i2].get()
                        amountTask_home = counter
                        # print(self.inputValueForTask[i2])
                        # print(inputTask_home)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 割り当て画面描画
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def drawAllocation():
        global drawAllocationArea
        drawAllocationArea = tk.Frame(root)
        # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # # フレーム作成↓↓↓
        # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 割り当てエリア描画 ----------------------------------------------------------------
        drawAllocationArea.pack(fill = tk.BOTH, expand = True)
        drawAllocationArea.configure(bg = "white")        
        # ---------------------------------------------------------------------------------------

        allocation = allocationClass()

        # 確定ボタン-----------------------------------------------------------------------
        confirmButton = tk.Button(drawAllocationArea, text="confirm", command = allocation.reflectAllocation)        
        confirmButton.pack(side = tk.BOTTOM, anchor=tk.E, padx=20, pady=10)
        # -----------------------------------------------------------------------------------

        # 初期画面描画
        allocation.updateAllocation()

# 割り当てタブ管理クラス
class allocationClass:
        # タスク名表示管理配列 
        taskName_allocation = []
        # 割り当て値管理配列
        allocationName_allocation = []
        # タスク名ラベル設置エリア
        taskNameArea_allocation = tk.Frame(drawAllocationArea)
        # 割り当て値入力欄設置エリア
        inputAllocatonArea = tk.Frame(drawAllocationArea)
        # 入力値管理配列
        inputAllocationManager = []
        # 実行フラグ
        flag = 0
        allocationFont = tkinter.font.Font(
                inputAllocatonArea,
                family="Bahnschrift",
                size=15,
                weight="bold"
        )

        def updateAllocation(self):
                # 実行フラグがオフ（flag == 0）の場合、ラベルと入力欄を設置するフレームを用意
                if self.flag == 0:
                        self.taskNameArea_allocation = tk.Frame(drawAllocationArea)
                        self.taskNameArea_allocation.configure(bg = "white")
                        self.taskNameArea_allocation.pack(side = tk.LEFT, fill="both", expand=True)

                        self.inputAllocatonArea = tk.Frame(drawAllocationArea)
                        self.inputAllocatonArea.configure(bg = "white")        
                        self.inputAllocatonArea.pack(side = tk.LEFT, fill="both", expand=True)

                # 配列の初期化
                length = len(self.taskName_allocation)
                for i1 in range(length):
                        self.taskName_allocation[i1].pack_forget()
                        self.allocationName_allocation[i1].pack_forget()

                # 配列のインスタンス化
                self.taskName_allocation = []
                self.allocationName_allocation = []                

                # ラベル、入力欄の設定
                for i2 in range(amountTask_home):
                        # タスク名が空白の場合の代替テキスト設定
                        if inputTask_home[i2] == "":
                                inputTask_home[i2] = "Task" + str(i2+1)

                        # 入力値管理配列にウィジェット変数を設置
                        self.inputAllocationManager.append(tk.StringVar())

                        # タスクタブで選択した値に応じてラベルと入力欄を用意
                        self.taskName_allocation.append(tk.Label(self.taskNameArea_allocation, text = inputTask_home[i2], padx=50, font=self.allocationFont))
                        self.allocationName_allocation.append(ttk.Entry(self.inputAllocatonArea, textvariable=self.inputAllocationManager[i2], font = self.allocationFont))

                        # ラベルの設置
                        self.taskName_allocation[i2].pack(side = tk.TOP, anchor = tk.E, expand=True)
                        self.taskName_allocation[i2].configure(bg="white")

                        # 入力欄の設置
                        self.allocationName_allocation[i2].pack(side = tk.TOP, anchor = tk.W, expand=True)
                        # allocationName_allocation[0].configure(bg = "white")

                # タスク数が0の場合の処理
                if amountTask_home == 0:
                        self.taskName_allocation.append(tk.Label(self.taskNameArea_allocation, text = "Not yet any tasks...", padx=50, font=self.allocationFont))
                        self.taskName_allocation[0].pack(side = tk.TOP, anchor = tk.E, expand=True)
                        self.taskName_allocation[0].configure(bg="white")
                
                # 実行フラグオン
                self.flag = 1

        # 割り当て入力値の反映
        def reflectAllocation(self):
                for i1 in range(len(inputTask_home)):
                        inputAllocation_home[i1] = self.inputAllocationManager[i1].get()
                

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
        elif currentFunction == "Allocation":      
                functionFont[2] = underlineFont          
        elif currentFunction == "Cycle":               
                functionFont[3] = underlineFont 
        elif currentFunction == "Linkage":       
                functionFont[4] = underlineFont
        
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
        title = tk.Label(titleArea, text = "what was 'task management app'")

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
        global drawAllocationArea
        global functionFont

        previousFunction = currentFunction

        # print(previousFunction)

        # 現在の機能名を管理変数に格納
        currentFunction = event.widget["text"]
        # print(currentFunction)

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
        elif previousFunction == "Allocation":
                drawAllocationArea.pack_forget()
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
                # task.previousSelected = task.selectedAmountOfTask.get()
                # task.selectedAmountOfTask.set(task.previousSelected)
                selectedAmountOfTask.set(0)
                if not previousFunction == "Task":
                        selectedAmountOfTask.set(int(amountTask_home)-1)
                drawTask()
        elif currentFunction == "Allocation":                
                drawFunctionName()
                drawAllocationArea = tk.Frame(root)
                drawAllocation()
        elif currentFunction == "Cycle":                
                drawFunctionName()
        elif currentFunction == "Linkage":                
                drawFunctionName()
        
        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# メインウィンドウの設定
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":      
        
        root.title("taskManagement")
        root.geometry("600x600")
        # root.resizable(False, False)
        root.configure(bg="white")       

        # 機能名一覧を描画
        drawFunctionName()

        # 最初はHome画面を開く
        drawHome()

        # メインフレームの描画
        root.mainloop()
        