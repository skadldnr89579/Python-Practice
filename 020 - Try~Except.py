try:
    print('Hello')
    print(param) # try~except 내부에 있어서 except부분으로 넘어감
except:
    print('Error')

# 예외(Exception)상황
# 프로그램을 작성시 뜻하지 않은 오류 발생 가능성 많음
# 프로그램이 실행 되는 동안 오류가 발생시 프로그램이 더 이상 진행 불가 상태를 뜻함

"""
# 프로그램 예외가 발생하더라도 중지시키지 않고, 예외에 대한 적절한 처리를 하여 계속 실행 가능하게
하는게 try~except 구문

# 프로그램의 논리적 오류가 발생할 가능성이 큰 부분을 try~except 사이에 두고 예외가 발생할 경우,
except 부분에서 적절한 처리를 해주기

# 위에 있는 코드는 정의되지 않은 변수(param)를 호출하는 예외 상황에 대한 예시
# 정의 안 된 param을 화면에 출력하는 코드는 다음과 같은 예외 발생, 프로그램 중단
# NameError : name 'param' is not defined
"""
print()

try:
    print('Hello')
    #print(param)
except:
    print('Error')
else:
    print('No Error')

# 어떤 로직을 수행했을때 오류 상황이 아닐 경우에만 어떤 작업을 수행하는 코드를 작성해야 할 때
# try~except~else 를 씀
# 위에 param변수가 정의 되지 않아서 'Error'라는 문구가 뜸
# 위에 param변수를 주석처리(#)를 하면 'No Error'라는 문구가 뜸

print()

try:
    print('Hello')
    print(param)
except:
    print('Error')
finally:
    print('Execute without questions')

# 오류 발생 유무 상관없이 무조건 실행 시키려면 try~except~finally 구문 씀
# 무조건 실행 시키려는 코드는 finally 부분에 작성
# param변수를 주석처리(#)해도 finally 부분은 무조건 실행됨

print()

try:
    print(param)
except Exception as e:
    print(e)

# 오류 코드 name 'param' is not defined가 나옴
# param이라는 정의 안 된 변수를 쓰고 있음
# 파이썬에서는 NameError라는 예외 발생 시킴
# except Exception as e는 NameError라는 객체를 e라는 이름으로 접근할 수 있게 해줌

# 코드에서 예외가 발생하면 이에 대한 내용 파악이 중요
# 파이썬은 발생 가능한 예외에 대해 exception 객체로 미리 정의해 두었음 
print()

import time # sleep() 함수 사용하기 위해 time 모듈 불러옴
count=1 # count의 초기값을 1로 설정
try:
    while True: # 무한 반복문을 지칭
        print(count) # count값 출력
        count+=1
        time.sleep(0.5) # 0.5초마다 출력
        print() #한 줄 공백
except KeyboardInterrupt: # Ctrl+c가 입력되면 발생하는 오류
    print('User killed this program')

# 특정 예외 상황이 발생했을 때만 except에서 처리할 수 있음
# except 다음에 특정 예외를 알려 주면 됨
# Ctrl+c를 누르기 전까지는 0.5초마다 숫자 출력
# Ctrl+c를 누르면 발생하는 오류는 KeyboardInterrupt
