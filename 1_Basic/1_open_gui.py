from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

root.mainloop() # 창을 띄우는 함수