# Operator Abbreviation

a=0
a+=1 # 0+1
a-=5 # 1-5
a*=2 # -4*2
a/=4 # -8/4
print(a)
print('\n')

# True/False

b=True
c=False
print(b==1)
print(c!=0)
print('\n')

# Relational Operator

d=1;e=3
f='abc';g='python'
print(d==e)
print(d<=e)
print(d!=e)
print(d>=e)
print(f==g)
print(f=='def')
print(f!='def')
print(f<g)
print(f>g)
print('\n')    
        
    
# Logical Operator

bool1=True;bool2=False;bool3=True;bool4=False
"""
A and B : A와B 둘다 참이어야 True
A or B : A또는B 둘 중에 하나만 참이어도 True
not A : A의 반대 
"""
print(bool1 and bool2)
print(bool1 or bool2)
print(bool1 or bool3)
print(bool1 and bool3)
print(bool2 and bool4)
print(bool2 or bool4)
print(not bool1)
print(not bool2)
print('\n')

# Bit Operator
bit1=0x61
bit2=0x62
print(hex(bit1&bit2))
print(hex(bit1|bit2))
print(hex(bit1^bit2))
print(hex(bit1>>1))
print(hex(bit1<<2))
print(hex(bit2>>1))
print(hex(bit2<<2))
print('\n')

"""
A&B : A와B 비트간 and 연산 수행
A|B : A와B 비트간 or 연산 수행
A^B : A와B 비트간 베타적 논리합 xor 연산 수행
~A : A의 비트를 반전시킴, 즉, A의 1의 보수를 만듬
A>>n : A의 모든 비트를 n만큼 오른쪽으로 이동
A<<n : A의 모든 비트를 n만큼 왼쪽으로 이동

61(hex) = 16*6+1*1(97/decimal) = 0110 0001(binary)
62(hex) = 16*6+2*1(98/decimal) = 0110 0010(binary)

& Operator : 0110 0001 & 0110 0010 = 0110 0000 (다르면 0)
| Operator : 0110 0001 | 0110 0010 = 0110 0011 (다르면 1)
^ Operator : 0110 0001 ^ 0110 0010 = 0000 0011 (같으면 0, 다르면 1)
>>n Operator : 0110 0001 >>1 = 0011 0000(맨 오른쪽에서 n만큼 제거후 앞에 0기록)
<<n Operator : 0110 0001 <<2 = 1000 0100(왼쪽에서 n만큼 제거후 뒤에 0기록)
단, 왼쪽 시프트 연산자는 제거할때 1이 있다면 남겨둔다 그리고 부족한 숫자만큼 0을 기록한다
쉽게 말하면 '1 1000 0100'이 형태인데, 이걸 정확히 풀면 0001 1000 0100

ex. 0110 0010 << 2
1000 1000 근데 앞에 1이 하나 있으므로 1 1000 1000 이걸 풀면 0001 1000 1000(binary)
0001 1000 1000 (binary)
8+128+256 = 136+256 = 392 (decimal)
188 (hex)
"""
x=10
y=15
z=5
x,z,y=x,y,z
print(x+z)

set_A={'A','G','F',1,5}
set_B=set_A.copy()
set_B.add(23)
print(set_A)
