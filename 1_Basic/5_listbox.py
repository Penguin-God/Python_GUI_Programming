from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

listbox = Listbox(root, selectmode="extended", height=3) # height가 0이면 모든 요소가 다 보임
listbox.insert(0, "루저 걸")
listbox.insert(1, "저승으로 가는 버스에 타고 안녕")
listbox.insert(2, "나 홀로 숨바꼭질")
listbox.insert(3, "Rock한 너와 작별이야")
listbox.insert(END, "비교당하는 아이")
listbox.insert(END, "진흙탕 주제에 나만의 소중함을 빼앗으려 하다니")
listbox.pack()

def BtnCmd():
    # listbox.delete(END) # 마지막 요소 삭제
    # listbox.delete(1) # 지정한 인덱스의 요소 삭제

    print(listbox.size()) # 개수 확인
    print("1번째부터 3번째까지 노래 제목 : ", listbox.get(0,2))
    print("현재 선택된 노래 순서 값 : ", listbox.curselection())
    

btn = Button(root, text="HIHI", command=BtnCmd)
btn.pack()

root.mainloop() # 창을 띄우는 함수