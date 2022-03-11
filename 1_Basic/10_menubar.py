from tkinter import *

root = Tk()
root.title("Hello GUI") # 제목 설정
root.geometry("700x500+350+150") # 가로크기 * 세로크기 + x좌표 + y좌표
root.resizable(False, False) # x,y 크기 조정 가능 여부

main_menu = Menu(root)

def play_anima():
    print("애니 재생중")
# 단일 meun 생성 및 세팅 
anima_menu = Menu(main_menu, tearoff=0)
anima_menu.add_command(label="애니 재생", command=play_anima)
anima_menu.add_command(label="애니 정보")
anima_menu.add_separator()
anima_menu.add_command(label="애니 추천")
anima_menu.add_separator()
anima_menu.add_command(label="애니 다운로드", state="disable")
anima_menu.add_separator()
anima_menu.add_command(label="exit", command=root.quit)
# 전체 메뉴에 세팅한 단일 메뉴 추가
main_menu.add_cascade(label="애니메이션", menu=anima_menu)

# 빈 메뉴 추가하기
main_menu.add_cascade(label="영화")

# 메뉴에 라디오 버튼 추가
genre_menu = Menu(main_menu, tearoff=0)
genre_menu.add_radiobutton(label="일상")
genre_menu.add_radiobutton(label="러브 코미디")
genre_menu.add_radiobutton(label="액션")
main_menu.add_cascade(label="장르", menu=genre_menu)

# 체크박스 메뉴 추가
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label="리뷰 보기")
main_menu.add_cascade(label="보기", menu=view_menu)



# 메뉴 보이게 하기
root.config(menu=main_menu)

root.mainloop() # 창을 띄우는 함수