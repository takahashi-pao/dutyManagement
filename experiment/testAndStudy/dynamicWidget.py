import tkinter as tk

# Tkinter お決まりフレーズ
class App(tk.Tk) :
    def __init__(self) :
        super().__init__()

        # タイトルとウィンドウサイズ
        self.title('appendEntry')
        self.geometry('640x480')

        # エントリーウィジェットをグループ化するためのフレーム
        self.FrameWindow = tk.Frame(self)
        self.FrameWindow.grid(row=0)

        # エントリーウィジェットマネージャを初期化
        self.Entries = []        # エントリーウィジェットのインスタンス
        self.insertEntries = []  # 追加するボタンのようなラベル
        self.removeEntries = []  # 削除するボタンのようなラベル

        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0           # 最新のインデックス番号
        self.indexes = []        # インデックスの並び

        # 最初のエントリーウィジェットを作成して配置
        self.createEntry(0)

        # テキストを取得ボタン作成
        self.GetEntryTextButton = tk.Button(
            text='テキストを取得',
            command=self.GetEntryTextButton_click
        )
        self.GetEntryTextButton.grid(row=1)

    # エントリーウィジェットを追加するボタンのようなラベルをクリック
    def insertEntry_click(self, event, id) :

        # 追加する位置
        next = self.indexes.index(id) + 1
        self.index = self.index + 1

        # エントリーウィジェットを作成して配置
        self.createEntry(next)

    # エントリーウィジェットを削除するボタンのようなラベルをクリック
    def removeEntry_click(self, event, id) :

        # 削除する位置
        current = self.indexes.index(id)

        # エントリーウィジェットと追加・削除ボタンのようなラベルを削除
        self.Entries[current].destroy()
        self.insertEntries[current].destroy()
        self.removeEntries[current].destroy()

        # エントリーウィジェットマネージャから削除
        self.Entries.pop(current)
        self.insertEntries.pop(current)
        self.removeEntries.pop(current)
        self.indexes.pop(current)

        # 再配置
        self.updateEntries()

    # エントリーウィジェットを再配置
    def updateEntries(self) :

        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)) :
            self.Entries[i].grid(column=0, row=i)
            self.Entries[i].lift()
            self.insertEntries[i].grid(column=1, row=i)
            self.removeEntries[i].grid(column=2, row=i)

        # 1つしかないときは削除ボタンのようなラベルを表示しない
        if len(self.indexes) == 1 :
            self.removeEntries[0].grid_forget()

    # エントリーウィジェットを作成して配置
    def createEntry(self, next) :

        # 最初のエントリーウィジェットを追加
        self.Entries.insert(next, tk.Entry(self.FrameWindow, width=30))

        # エントリーウィジェットを追加するボタンのようなラベルを作成
        self.insertEntries.insert(next, tk.Label(
            self.FrameWindow,
            text='+',
            fg='#33ff33',
            font=('Arial Black', 20)
        ))

        # エントリーウィジェットを削除するボタンのようなラベルを作成（初期の段階では表示しない）
        self.removeEntries.insert(next, tk.Label(
            self.FrameWindow,
            text='−',
            fg='#ff3333',
            font=('Arial Black', 20)
        ))

        # 追加するボタンのようなラベルにクリックイベントを設定
        self.insertEntries[next].bind('<1>', lambda event, id=self.index: self.insertEntry_click(event, id))

        # 削除するボタンのようなラベルにクリックイベントを設定
        self.removeEntries[next].bind('<1>', lambda event, id=self.index: self.removeEntry_click(event, id))

        # インデックスマネージャの指定の位置に登録
        self.indexes.insert(next, self.index)

        # 再配置
        self.updateEntries()

    # テキストを取得するボタンを押す
    def GetEntryTextButton_click(self) :
        GetEntry =[]

        # 全てのエントリーウィジェットの内容を配列化
        for i in range(len(self.indexes)) :
            GetEntry.append(self.Entries[i].get())

        # コンソールに表示
        print(GetEntry)

# Tkinter お決まりフレーズ
if __name__ == '__main__' :
    app = App()
    app.mainloop()