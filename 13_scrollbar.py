from sys import set_coroutine_origin_tracking_depth
from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

main_frame = Frame(root)
main_frame.pack()

# 스크롤 바랑 리스트 박스 둘 다 main_frame안에 들어감
scrollbar = Scrollbar(main_frame)
scrollbar.pack(side="right", fill="y")

list_box = Listbox(main_frame, selectmode="expended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    list_box.insert(END, str(i) + "일")
list_box.pack()
# 스크롤 바에 리스트 박스 매핑
scrollbar.config(command=list_box.yview)

root.mainloop() # 창을 띄우는 함수