from email.mime import image
from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표

# 버튼을 넣을 창,  띄울 텍스트
btn1 = Button(root, text="Hello Button1") # 버튼 설정
btn1.pack() # 설정한 버튼 포함시키기(이거 해야 버튼이 보임)

# 가로, 세로 지정 고정 크기로 글자 길어지면 글자가 깨짐
btn2 = Button(root, width=10, height=3,text="Hello Button222222222222222222222222")
btn2.pack()

# 가로, 세로 지정 반응형 크기로 글자 길어지면 버튼이 커짐
btn3 = Button(root, text="Hello Button333333333333333333")
btn3.pack()

# 글자 색깔, 배경 색깔
btn4 = Button(root, fg="red", bg="yellow",text="Hello Button4")
btn4.pack()

# 이미지로 버튼 생성
checkImg = PhotoImage(file="checkImg.png")
btn5 = Button(root, image=checkImg)
btn5.pack()

# 버튼 동작
def ButtonTest():
    print("신기방기!!!")

btn6 = Button(root, text="동작하는 버튼. 우와 신기하다!!", command=ButtonTest)
btn6.pack()


root.mainloop() # 창을 띄우는 함수