from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

Label(text="펭귄갓 햄버거").pack()

burger_var = StringVar()
#burger_var2 = StringVar()
# 같은 variable이 있는 것 중에 하나만 선택할 수 있음
# 버튼이 선택되면 그 버튼의 value의 값이 burger_var로 넘어감
burger_btn1 = Radiobutton(root, text="햄버거", value="햄버거", variable=burger_var)
burger_btn1.select() # 기본 선택(이거 안하면 처음에 다 선택함)
burger_btn2 = Radiobutton(root, text="치즈버거", value="치즈버거", variable=burger_var)
burger_btn3 = Radiobutton(root, text="불고기버거", value="불고기버거", variable=burger_var)

burger_btn1.pack()
burger_btn2.pack()
burger_btn3.pack()


Label(text="펭귄갓 음료").pack()
drink_var = StringVar()
drink_btn1 = Radiobutton(root, text="콜라", value="팹시", variable=drink_var)
drink_btn1.select() # 기본 선택(이거 안하면 처음에 다 선택함)
drink_btn2 = Radiobutton(root, text="사이다", value="칠성 사이다", variable=drink_var)
drink_btn3 = Radiobutton(root, text="우유", value="서울우류", variable=drink_var)

# .pack()을 하고 변수에 넣어버리면 .select() 등의 함수를 이용할 수 없음 그래서 다 만들고 맨 아래에서 .pack()함
drink_btn1.pack()
drink_btn2.pack()
drink_btn3.pack()

def print_burger():
    print(burger_var.get()) # burger_var를 가지고 있는 버튼 중 값을 선택된 버튼의 값을 가져옴
def print_drink():
    print(drink_var.get()) # burger_var를 가지고 있는 버튼 중 값을 선택된 버튼의 값을 가져옴

Button(root, text="버거 주문", command=print_burger).pack()
Button(root, text="음료 주문", command=print_drink).pack()
root.mainloop() # 창을 띄우는 함수