#모든 코드들을 print를 통해 눈으로 직접 확인하면서 단계적으로 진행하자!

import random
#improt(파이썬 자체내에서 제공되는 기본 명령어(도서관같은 느낌)
#무엇을? 'random(아무거나)'을.

#'random'은 파이썬 회사(import(도서관)) 자체에서 만든 코드로 만든 파일을, 
#유저들이 쉽게 사용할 수 있도록, 명령어 만으로 꺼내쓸 수 있게, 파이썬 자체내에서 제공하는 기능.
#간단 요약 : 만들어진 코드를 파이썬 파일로 만들어, 간단한 명령어로 꺼내쓸수있게 파이썬에서 제공하는 것.(모듈)

#컴퓨터가 임의로 유저가 맞출 정답을 생성하기 위한 준비.
#라이브러리 : 파이썬 하나의 파일(모듈), 모듈을 여러개 모아놓은 하나의 압축파일(패키지), 패키지 모으면? 니가맞춰!
#모르면 바보, 코딩 접어 오케이 !? :)

best = 100

while True:
    answer = random.randint(1, 49) and random.randint(51, 100)
    #answer(답변) 이라는 명칭을 준 곳에 random.randint(자연수 중 랜덤으로 수를 선택하는것을 의미) 
    # 이라는 코드로 한정된 a-b 까지의 숫자를 정해주는 것.
    # 요약 : 컴퓨터가 임의로 만든 정답 범위를 지정해주는 작업.

    ###### [예외처리] 50을 제외한 1~100의 숫자 중 랜덤 ######

    if answer == 50:
        reload
        ###### [예외처리] if(만약에 answer(답변이) == 50(50과 같다면.) ######
        ###### reload(모듈을 다시 실행하자!) ######                                                                

    count = 0
    #유저의 시작 포인트를 지정해주는 것.

    print(answer)
    #해설 : print(인쇄.보여주다) 무엇을 ? answer(답변)을.
    #answer(답변)라고 정한 명칭한에 코드명령을 행동하게 하는 코드.

    if best != 100:
        print('그 전 대빵은 :', best, '회 만의 맞추더라.')

    while True:
        #while(~하는동안) 이기때문에 true가 될때까지라는 의미.
        #거꾸로 false 라면, 오답이 나올때까지라는 의미가 가능하다.

        user_pick = int(input('\033[31m' + '50을 제외한 1부터 100까지 내가 고른 숫자 맞춰봐 임마'))
    #입력할떄 쓰이는 코드:input / 해설 : user_pick = (유저가) int(정수)를 input(입력) 한다.
            ###### '\033[색상코드m' + '문장' + '\033[다시돌려놓을색상코드m']
            #색깔을 넣는 코드는 '\033' 색상코드 입력란은 '[색상코드m'
            #색깔은 구글링 '파이썬 색상코드' 검색.

        if user_pick < 1:
            print('1부터하라고 임마')
            #if(만약에) user_pick이 1보다 작은 숫자를 입력하게 되면 print(보여줘라) '손가락이 잘못됫는겨?'를.

        elif user_pick > 100:
            print('100보다 작은거라고 쨔샤')
            #or(또는) user_pick이 100보다 큰 숫자를 입력하게 되면 print(보여줘라) '손가락이 잘못됫는겨?'를

        elif user_pick == 50:
            import random
            print('50을 제외한이 뭔뜻인지 몰러?')
            ###### [예외처리] 제외한 50을 입력했을때, 처리(print) 할 반복문 #####

            continue
        #'continue'를 입력하게 될 경우 잘못된것을 인지하고, 다시 처음부터 입력할수있게 해준다.
        #if,elif,else 코드로 입력된 설정은 무시하고, 처음으로 돌아간다.
        #continue 명령어는 무조건 반복문에만 사용이 가능하다. 

        # 요약 : 유저가 게임을 하고 있는데, 잘못 입력을 하게 되면, 시도 횟수가 올라가지 않고(아래코드를 무시하고)
        # 다시 입력할 수 있게 해주는 명령어. or 재시도 할수있게 해주는 명령어.

        count = count + 1
        #유저가 입력시도를 할 때마다 카운트가 올라가게 하는 방식.

        if answer > user_pick:
            print('좀 더 분발하슈')
            #if(만약에) ansewr(답변)이 user_pick 보다 크다면, print(보여줘라) 무엇을? '좀 더 분발하슈'
        elif answer < user_pick:
            print('쪼까내려야쓰것다')
            #elif(그게아니고) answe(답변)이 user_pick 보다 작다면, print(보여줘라) 무엇을? '내가 높은디 ***' 
        else:
            print('\033[34m' + '샹크스 : 이 전쟁을 끝내러 왔다.' + '\033[0m')
            #else(그것도아니야?) break 그럼 끝내자.
            #만약에 break 라는 명령어가 입력되어 있지않다면, 맨 마지막 선택지가 되는게 else 명령어 이다.

            ###### '\033[색상코드m' + '문장' + '\033[다시돌려놓을색상코드m']
            #색깔을 넣는 코드는 '\033' 색상코드 입력란은 '[색상코드m'
            #색깔은 구글링 '파이썬 색상코드' 검색.

            print(count, '번 만의 맞춘거 실화냐?')
            best = min(best, count)
            #best(최고는) =(는) min(매개변수로 들어온 인자 내부에서 제일 작은 값을 반환)
            #반대로는 max(최대값)

            break
        #여기까지 입력한 코드로 만든게임을 유저가 정답을 맞춰서 끝이나면, 이 게임을 끝내는 명령어는 break
        #게임의 마무리를 시키는거다. 마치 샹크스가 전쟁을 끝내로 온거처럼.
        
        while True:
                retry = input('다시하시겠습니까? (Y/N)')
                retry = retry.lower()
                #upprr(입력값을 소문자로 입력해도 대문자로) #lower(입력값을 소문자로 입력해도 대문자로)
                if retry in ['y', 'yes', 'ok'] or retry in ['n', 'no']:
                    break
                else:
                    print('Y 또는 N을 입력하세요.')
                if retry in ['y', 'yes', 'ok']:
                    continue
                #if(만약에) retry(명칭)에 in(대한) 답이 'y'일 경우,
                #continue(다시하자)
                elif retry in ['n', 'no']:
                    break
                #elif(그게아니고) retry(명칭)에 (in)대한 답이 'n'일 경우,
                #break(끝내자)
                
                print('게임을 종료합니다. 최고기록: ', best)