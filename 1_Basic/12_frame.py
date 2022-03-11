from cProfile import label
from tkinter import *

from matplotlib.pyplot import text
from numpy import rot90

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

# 아래 있는 프레임들이 fill을 하기전에 설정해야 위, 아래에 딱 붙음
Label(root, text="오늘 자기 전에 볼 작품 후보").pack(side="top")
Button(root, text="보기").pack(side="bottom")

# 프레임
anima_frame = Frame(root, relief="solid", bd=1)
# root 대신 anima_frame가 들어감
Button(anima_frame, text="주술회전").pack()
Button(anima_frame, text="도쿄 구울").pack()
Button(anima_frame, text="강철의 연금술사").pack()
anima_frame.pack(side="left", fill="both", expand=True)

comic_book_frame = Frame(root, relief="solid", bd=1)
Button(comic_book_frame, text="호리미야").pack()
Button(comic_book_frame, text="그 비스크 돌은 사랑을 한다").pack()
comic_book_frame.pack(side="right", fill="both", expand=True)

root.mainloop() # 창을 띄우는 함수