# 参考サイト
# http://pc-chem-basics.blog.jp/archives/24112647.html

# tkinterのインポート
import tkinter as tk

# 関数の作成=>GUIよりも上に記述する必要がある
# ディレクトリに注意
def newtxt_func():
    datafile = open("newtxt.txt","w")
    test = "ok?"
    datafile.write(test)
    datafile.close()

# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("350x100")

# Runボタン設置
# commandに関数newtxt_huncを設定
run_button = tk.Button(root, text = "Run", command=newtxt_func)
run_button.place(x = 160, y = 40)

# Setボタン設置
set_button = tk.Button(root, text = "Set")
set_button.place(x = 300, y = 7)

# テキストボックス設置
input_box = tk.Entry(width = 40)
input_box.place(x = 10, y = 10)

# ステータスバー設置
# bd = 1 ：縁(ボーダー)の幅を1に指定 (値を大きくすると幅が広がります)
# relief = tk.SUNKEN： 縁のスタイルを指定 (SUNKEN：親要素より沈んで表示)
# anchor = tk.W： 配置可能なスペースに余裕がある場合、ウイジットをどこに配置するか指定 (W ：左よせ, E  : 右寄せ)
statusbar = tk.Label(root, text =  " No Data!!", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
# pack()メソッドはウイジットを順番に配置します。x, y座標で細かくウイジットの配置を決める必要がなく、存在するウイジットを単純に順番通り配置してよい場合などに用います。
# 下から順番に配置、空いているスペースは横に広がって埋める
statusbar.pack(side = tk.BOTTOM, fill = tk.X)

# ウインドウ状態の維持
root.mainloop()

