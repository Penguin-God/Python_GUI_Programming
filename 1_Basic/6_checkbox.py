from msilib.schema import CheckBox
from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

intVar = IntVar() # chkbox에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="Hello Checkbox", variable=intVar)
chkbox.select() # 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()

intVar2 = IntVar()
chkbox2 = Checkbutton(root, text="Hello Checkbox", variable=intVar2)
chkbox.select()
chkbox2.pack()

def BtnCmd():
    print(intVar.get()) # 0 : 체크 해제, 1 : 체크
    print(intVar2.get())
    

btn = Button(root, text="HIHI", command=BtnCmd)
btn.pack()

root.mainloop() # 창을 띄우는 함수