import random
#improt(파이썬 자체내에서 제공되는 기본 명령어(도서관같은 느낌)
#무엇을? 'random(아무거나)'을.

print('\033[0m' )

win = 0
draw = 0
lose = 0

count = 0

options = ['가위', '바위', '보']
#options(명칭) [명칭으로 사용할 이름들]

while True:

    def get_player_choice():
        while True:
            player_choice = input('가위, 바위, 보 중 하나를 선택하세요: ')
            #player_choice(명칭) = input(입력)('전달사항')
            if player_choice in ['가위', '바위', '보']:
                #if(만약에) player_choice(명칭) in(안에) [가위,바위,보] 중에 입력을 하면.
                return player_choice
            else:
                print('잘못된 입력입니다. 다시 입력하세요.')

            while True:
                player_choice = get_player_choice()

                computer_choice = random.choice(options)
                print(computer_choice)

                if (
                    (player_choice == '가위' and computer_choice == '보')
                    #if(만약에) player_choice가 가위고, computer_choice가 보라면.
                        or (player_choice == '바위' and computer_choice == '가위')
                        #or(또는) #if(만약에) player_choice가 '바위'고, computer_choice가 '가위'라면.
                        or (player_choice == '보' and computer_choice == '바위')):
                    #or(또는) #if(만약에) player_choice가 '보'고, computer_choice가 '바위'라면.
                    print('이겼음')
                    win += 1
                elif player_choice == computer_choice:
                    ##elif(그게아니라) player_choice와 computer_choice가 ==(같다면)
                    print('비겼음')
                    draw += 1
                else:
                    ##else(그것도 아니라면)
                    print('졌음')
                    lose += 1

                retry = input('다시하시겠습니까? (Y/N)').lower()
                if retry == 'y':
                    continue
                elif retry == 'n':
                    break

                print(f"승리 : {win}회 / 비김 : {draw}회 / 패배 : {lose}회")
