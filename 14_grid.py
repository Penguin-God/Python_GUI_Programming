from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

# .pack() 처럼 gui요소를 보여주는 역할을 하지만 좌표를 지정해 위치를 원하는 대로 설정할 수 있다.
# bth1 = Button(root, text="btn1")
# bth2 = Button(root, text="btn2")

# bth1.grid(row=0, column=0)
# bth2.grid(row=1, column=1)

current_row = 0
current_column = 0
row_limit = 4

def create_bth(_text):
    global current_row
    global current_column
    # sticky : 빈 공간 중 원하는 방향을 채움. 지금은 4방향 다 꽉 채웠음
    # pad : 글자 기준으로 각 축마다 밀어서 빈 공간을 만듬
    # button에 주면 button이 넓어지고 grid에 주면 서로 떨어짐
    Button(root, text=_text, width=5, height=2).grid(row = current_row, column = current_column, sticky=N+E+W+S, padx=3, pady=3)

    current_column = current_column + 1
    if(current_column >= row_limit):
        current_column = 0
        current_row = current_row + 1

create_bth("F16")
create_bth("F17")
create_bth("F18")
create_bth("F19")

create_bth("Clear")
create_bth("=")
create_bth("/")
create_bth("*")

create_bth("7")
create_bth("8")
create_bth("9")
create_bth("-")

create_bth("4")
create_bth("5")
create_bth("6")
create_bth("+")

create_bth("1")
create_bth("2")
create_bth("3")
Button(root,text="enter",  width=5, height=2).grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로부터 아래로 2칸 먹음

Button(root,text="0",  width=5, height=2).grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로부터 오른쪽으로 2칸 먹음
Button(root,text=".",  width=5, height=2).grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)



root.mainloop() # 창을 띄우는 함수