from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

progress_bar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate : 불확실한
progress_bar2 = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate : 확실한, 단호한
progress_bar.start(5) # 5ms마다 움직임게 실행시킴 
progress_bar2.start(5) 

progress_bar.pack()
progress_bar2.pack()
def print_day():
    progress_bar2.stop() # 멈춰!
Button(root, text="멈춰!", command=print_day).pack()


import time
progress_var = DoubleVar()
progress_bar3 = ttk.Progressbar(root, maximum=100, length=200,  variable=progress_var)
def progress_start():
    for i in range(1, 101):
        time.sleep(0.01)
        progress_var.set(i) # 값 설정
        progress_bar3.update() # gui update
        print(progress_var.get()) # print current percentage

progress_bar3.pack()
Button(root, text="시작~~~~~~~~~~~~~~~~~~하겠습니다!!!!!", command=progress_start).pack()
root.mainloop() # 창을 띄우는 함수