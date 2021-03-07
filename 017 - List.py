# List
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[1,'a','abc',[1,2,3,4,5],['a','b','c']]
print(list1)
print(list2)
print(list3)
list1[0]=6
print(list1, 'list1 맨 앞자리가 6으로 바뀜')

def myfunc():
    print('hello')

list4=[1,2,myfunc]
list4[2]() # myfunc가 출력됨

# Tuple

tuple1=(1,2,3,4,5)
tuple2=('a','b','c')
tuple3=(1,'a','abc',[1,2,3,4,5,6],['a','b','c'])

print(tuple1)
print(tuple2)
print(tuple3)

#tuple1[0]=6 # tuple값은 변경 불가능

def myfunc1():
    print('hello~!!!')

tuple4=(1,2,myfunc1)
tuple4[2]() # myfunc1이 출력됨

# Dictionary

dict1={'a':1,'b':2,'c':3}
print(dict1['a'])
dict1['d']=4 # dict1에 값 추가
print(dict1)
dict1['b']=7 # dict1의 값 1개 수정
print(dict1)
print(len(dict1))

# Definition

def add_number(n1,n2):
    ret=n1+n2
    return ret

def add_txt(t1,t2):
    print(t1+t2)

ans=add_number(10,15)
print(ans)
text1='Korea~!!!!'
text2='Australia~!!!'
add_txt(text1,text2)

"""

- 인자와 리턴값이 있는 함수 선언 방법 -
def 함수이름(인자1, 인자2, ...):
코드들
return 결과값

- 리턴값은 있지만 인자가 없는 함수 선언 방법 -
def 함수이름():
코드들
return 결과값

- 인자와 리턴값이 없는 함수 선언 방법 -
def 함수이름():
코드들
return (또는 생략)

- 인자와 리턴값이 있는 함수 호출 방법 -
변수 = 함수이름(값1,값2,...)

- 리턴값이 없는 함수 호출 방법 -
함수이름(값1,값2,...)

- 인자와 리턴값이 없는 함수 호출 방법 -
함수이름()

"""

# 함수 인자

def add_txt2(t3,t4='Python'):
    print(t3+':'+t4)

add_txt2('Best')
add_txt2(t4='KOREA',t3='First')

def func1(*args):
    print(args)
def func2(width,height,**kwargs):
    print(kwargs)

func1()
func1(3,5,1,5)
func2(10,20)
func2(10,20,depth=50,color='red')

# 지역변수, 전역변수
param=10
strdata='전역변수'

def func3():
    strdata='지역변수'
    print(strdata)

def func4():
    global param
    param=50
def func5(param):
    param=1
    
func3()
print(strdata)
print(param)
func5(param)
print(param)
func4()
print(param)

# 함수 리턴값
def reverse(x,y,z):
    return z,y,x

ret=reverse(1,2,3)
print(ret)

r1,r2,r3=reverse('a','b','c')
print(r1);print(r2);print(r3)



