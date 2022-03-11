from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

days = [str(i) + "일" for i in range(1, 32)]
# height=5 : 목록이 5개 보일 정도로 높이가 설정됨
combo_box = ttk.Combobox(root, height=5, values=days, state="readonly") # state="readonly" : 값 변경 안되게 막음
#combo_box.set("카드 결제일") # 목록의 최초 제목 설정
combo_box.current(0) # 0번째 값을 최초 값으로 설정
combo_box.pack()

def print_day():
    print(combo_box.get()) # 선택된 값 출력
Button(root, text="결제", command=print_day).pack()

root.mainloop() # 창을 띄우는 함수