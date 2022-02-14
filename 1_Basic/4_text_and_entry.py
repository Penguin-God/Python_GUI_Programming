from distutils import command
from tkinter import *
from xml.etree.ElementTree import Comment

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

# 텍스트 입력 창(여러 줄)
txtWindow = Text(root, width=30, height=5)
txtWindow.insert(END, "Hello Text Window") # 기본값 설정
txtWindow.pack()

# 텍스트 입력 창(한 줄)
entry = Entry(root, width=30)
entry.insert(0, "한 줄만 가능 ")
entry.pack()

def BtnCmd():
    print(txtWindow.get("1.0", END)) # 1번째줄 0번째 글자부터 끝까지 가져오기
    print(entry.get())

    txtWindow.delete("1.0", END)
    entry.delete(0, END)

btn = Button(root, text="HIHI", command=BtnCmd)
btn.pack()

root.mainloop() # 창을 띄우는 함수