from cgitb import text
from distutils.log import debug
from email.mime import image
from math import fabs
from tabnanny import check
from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표

label1 = Label(root, text="Hello Label")
label1.pack()

checkImg = PhotoImage(file="1_Basic\img\checkImg.png")
label2 = Label(root, image=checkImg)
label2.pack()

XImg = PhotoImage(file="1_Basic\img\XImg.png")

isChange = False
def Change():
    global isChange
    if(isChange):
        label1.config(text="Hello Label")
        label2.config(image=checkImg)
        isChange = False
    else:
        label1.config(text="안녕 레이블")
        label2.config(image=XImg)
        isChange = True

btn6 = Button(root, text="동작하는 버튼. 우와 신기하다!!", command=Change)
btn6.pack()


root.mainloop() # 창을 띄우는 함수