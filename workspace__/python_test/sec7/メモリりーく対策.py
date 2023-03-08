import tkinter as tk

# 円の座標
x = 400
y = 300

def move():
    global x, y
    # X座標を動かす
    x = x + 1
    # 円の位置を更新する
    canvas.coords(circle, x - 20, y - 20, x + 20, y + 20)
    # 再びタイマー
    root.after(10, move)

# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

# キャンバスを置く
canvas =tk.Canvas(root, width =600, height =400, bg="white")
canvas.place(x = 0, y = 0)

# 円を描画する
circle = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", width=0)

# タイマーを設定する
root.after(10, move)

root.mainloop()