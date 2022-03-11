from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부


def info():
    msgbox.showinfo("알림창", "정보")

def warning():
    msgbox.showwarning("경고창", "인간 시대의 끝이 도래했다.")

def error():
    msgbox.showerror("에러", "error?")

def okcancle():
    msgbox.askokcancel("yes / no", "스텔라 패스를 정말로 구매하시겠습니까?")

def retrycancle():
    response = msgbox.askretrycancel("재접속 / 나가기", "오류로 접속이 종료되었습니다. 재접속 하시겠습니까?")
    if(response == 1):
        print("재접")
    elif(response == 0):
        print("종료")

def yesno():
    msgbox.askyesno("yes or no", "yes or no")

def yesnocancle():
    # True, False, None
    # 예 : 0, 아니요 : 1, 그 외
    # 2개 중 아무거나 하면 됨
    response = msgbox.askyesnocancel(title=None, message="정보가 사라질 수 있습니다. \n 정보를 저장하고 종료하시겠습니까?")
    if(response):
        print("저장하고 종료")
    elif(response == False):
        print("저장하지 않고 종료")
    elif(response == None):
        print("종료 취소")
    


Button(root, command=info, text="정보").pack()
Button(root, command=warning, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancle, text="2차원 질문").pack()
Button(root, command=retrycancle, text="재시도 질문").pack()
Button(root, command=yesno, text="단축키가 추가된 2차원 질문").pack()
Button(root, command=yesnocancle, text="3차원 질문").pack()

root.mainloop() # 창을 띄우는 함수