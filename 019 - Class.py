# Class

class MyClass:
    var='Hello'
    def sayHello(self):
        print(self.var)

obj=MyClass() #MyClass 인스턴스 객체 생성
print(obj.var)
obj.sayHello()

"""
class 정의

class 클래스 이름:
클래스 맴버 정의
클래스 메소드 정의

MyClass의 인스턴스 객체 obj의 멤버 또는 메소드를 호출하는 방법
obj.클래스 멤버 # MyClass의 클래스 멤버
obj.클래스 메소드 # MyClass의 클래스 메소드
"""
print()

x,y='12'
y,z='34'
print(x+y+z)

print()

# Class Member & Instance Member

class MyClass2:
    var2='Halo'
    def sayHello2(self):
        param1='Hi'
        self.param2='Hello~!!!'
        print(param1) #'Hi'가 출력됨
        print(self.var2) #'Halo'가 출력됨

obj2=MyClass2()
print(obj2.var2) #'Halo'가 출력
obj2.sayHello2()
#obj.param1
##AttributeError:'MyClass2' object has no attribute 'param1'
#'param1'은 MyClass2의 클래스 메소드인 sayHello2()의 지역변수
#고로 MyClass2의 인스턴스 객체인 obj의 멤버로 참조 불가능

#AtrributeError:'MyClass2' object has no attribute 'param2'
#sayHello2 클래스가 호출되기 전이라 나는 오류

"""
self.var #클래스 메소드 내에서 var를 참조할 경우
MyClass.var #클래스 밖에서 클래스 이름만으로 참조할 경우(별로 안 쓰임)
obj.var #MyClass의 인스턴스 객체 obj에서 var를 참조할 경우
"""
print()
class MyClass3:
    def sayHello3(self):
        print('Hallo')
# MyClass3의 클래스 메소드 sayHello3()를 정의, 이 메소드는 인자 없음
# 호출되면 'Hallo'가 출력됨

    def sayBye(self,name):
        print('%s! See you again!'%name)
# MyClass3의 클래스 메소드 sayBye(self,name)의 인자는 name이다.
obj3=MyClass3()
obj3.sayHello3() #'Hallo'가 출력됨
# MyClass3의 인스턴스 객체를 생성하고 obj3로 지정
# MyClass3의 클래스 메소드인 sayHello3(), sayBye()를 호출

obj3.sayBye('Jenny') #'Jenny! See you again!'가 출력됨
print()

class MyClass4:
    def __init__(self):
        # 클래스의 인스턴스 객체가 생성될때 자동적으로 호출되는 메소드가 클래스 생성자
        # 클래스 생성자가 갖는 이름이 def __init__(self,*args)
        self.var='Hello~!!!'
        print('MyClass4 instance objects are created')
        # MyClass4의 클래스 생성자를 정의합니다. MyClass의 클래스 생성자는 인자가 없고
        # 생성자 내에서 self.var 인스턴스 멤버를 'Hello~!!!'라는 문자열로 초기화
        # 'MyClass4 instance objects are created' 라는 메세지 출력

obj4=MyClass4()
# MyClass4의 생성자에 인자가 없으므로 MyClass4()와 같이 인스턴스 객체를 생성함
# 인스턴스 객체가 생성될 때 MyClass4의 생성자가 자동으로 호출되므로 self.var가 초기화됨
# 화면에 메세지 출력 
print(obj4.var)
# MyClass4의 생성자에서 초기화한 self.var의 값을 출력함

# 클래스 생성자는 인자를 가질수 있음
# 생성자에 인자가 있다면 인스턴스 객체를 만들 때 인자에 적당한 값을 대입해야 함
# 이렇게 예를 들어봅시다

"""
class MyClass4:
    def __init__(self,txt):
    self.var=txt
    print('생성자 인자로 전달받은 값은 <'+self.var+'> 입니다')

# MyClass4의 생성자 인자를 하나 가지므로 MyClass4 인스턴스 객체는 다음과 같이 만듦

obj4=MyClass4('Tom')

# 인자를 입력 안 하고 인스턴스 객체를 생성하려고 하면 다음 오류 발생

# TypeError: __init__() missing 1 required positional argument: 'txt'
# 형식오류: __init__() 1개의 아규먼트('txt') 빠져있음

"""
print()
class MyClass5:
    def __del__(self):
        print('MyClass5 instance objects are erased from Memory')
    # 클래스 인스턴스를 메모리에서 제거할 때 클래스 소멸자에서 메시지를 출력하는 코드
    # 클래스 소멸자에서 print()를 호출하여 메시지를 출력

obj5=MyClass5()
del obj5 # 'MyClass5 instance objects are erased from Memory'가 출력됨
# 생성된 MyClass5 인스턴스 객체 obj5를 del 키워드로 메모리에서 제거
# 이때 클래스 소멸자는 자동으로 호출되서 print() 내용이 출력됨

# 클래스 인스턴스 객체가 메모리에서 제거될 때 자동적으로 호출되는 클래스 메소드가 클래스 소멸자
# 클래스 소멸자는 __del__(self):
# 인스턴스 객체 제거 del<인스턴스 객체>

print()

class Add:
    def add(self,n1,n2):
        return n1+n2
# Add라는 이름의 클래스를 정의
# 이 클래스는 두수를 더한 값을 리턴하는 add()라는 클래스 메소드가 있음

class Sub(Add):
    def sub(self,n1,n2):
        return n1-n2
# Sub라는 클래스는 Add 클래스를 상속받아 정의
# 따라서 Sub 클래스는 Add 클래스의 add() 메소드를 그대로 물려 받음
# Sub 클래스에서 두 수를 뺀 값을 리턴하는 sub()라는 클래스 메소드를 정의

obj6=Sub()
print(obj6.add(1,2)) # 3
print(obj6.sub(1,2)) # -1
# Sub 클래스의 인스턴스 객체를 생성, 이 객체의 add(1,2) 호출
# add()는 Sub의 부모클래스인 Add 클래스로부터 상속받았음
# 그리고 Sub 클래스에서 정의된 sub() 메소드를 호출받음


# 두 수를 더하는 클래스를 상속받은 자식클래스를 정의하고 자식클래스에서 두 수를 빼는 클래스 메소드 정의


# 클래스는 상속이라는 특성을 가지는 이름공간
# 클래스에서 상속이란 어떤 클래스가 가지고 있는 모든 멤버나 메소드를 상속받는 클래스가 사용가능
# 상속을 하는 클래스는 부모클래스/슈퍼클래스
# 상속을 받는 클래스는 자식클래스/서브클래스
# 정의 법 : class 자식클래스(부모클래스)

# 다중상속 정의 법 : class 자식클래스(부모클래스1, 부모클래스2, ...)
print()

class Add2:
    def add2(self,m1,m2):
        return m1+m2

class Mul:
    def mul(self,m1,m2):
        return m1*m2

class Dev:
    def dev(self,m1,m2):
        return m1/m2

class Sub2(Add2,Mul,Dev):
    def sub2(self,m1,m2):
        return m1-m2

obj7=Sub2()
print(obj7.add2(1,2)) #3
print(obj7.mul(1,2)) #2
print(obj7.sub2(1,2)) #-1
print(obj7.dev(1,2)) #0.5
