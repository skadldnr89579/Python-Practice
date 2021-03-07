#Sequence data
strdata='abcd' #String
listdata=[1,[2,3],'hello'] #List
tupledata=(100,200,300) #Tuple

"""
Sequence data characteristic

1. 인덱싱 : 인덱스를 통해 해당값에 접근 가능 0부터 시작
2. 슬라이싱 : 특정 구간의 값을 취할수 있음 구간은 첫 인덱스와 끝 인덱스
3. 연결 : '+'연산자를 통해 두 시퀀스 자료를 연결하여 새로운 시퀀스 자료로 생성
4. 반복 : '*'연산자를 통해 시퀀스 자료를 여러번 반복하여 새로운 시퀀스 자료로 생성
5. 멤버체크 : 'in'키워드를 이용 특정 값이 시퀀스 자료의 요소로 속해 있는지 확인 가능
6. 크기정보 : len()을 이용해 시퀀스 자료의 크기 확인 가능,
문자열의 경우 문자 개수, 리스트와 튜플은 멤버의 개수
"""

# 인덱싱
strdata2='Time is money!!'
listdata2=[1,2,[1,2,3]]
print(strdata2[5])
print(strdata2[-2])
print(listdata2[0])
print(listdata2[-1])
print(listdata2[2][-1])
print('\n')
# 슬라이싱
print(strdata2[1:5])
print(strdata2[:7])
print(strdata2[9:])
print(strdata2[:-3])
print(strdata2[-3:])
print(strdata2[:])
print(strdata2[::2])
print('\n')
"""
m:n 시퀀스 자료의 인덱스가 m이상 n미만인 요소를 슬라이싱
:n 시퀀스 자료가 처음부터 인덱스 n미만인 요소까지 슬라이싱
m: 시퀀스 자료의 인덱스가 m인 요소부터 끝까지 슬라이싱
:-n 시퀀스 자료의 자료의 처음부터 끝에서 n번째 미만인 요소까지 슬라이싱
-m: 시퀀스 자료의 끝에서 m번째 요소부터 시퀀스 자료의 끝까지 슬라이싱
"""

# 시퀀스 자료 연결(+)

strdata3='I love '; strdata4='Python.';strdata5='you.'
listdata3=[1,2,3];listdata4=[4,5,6]
print(strdata3+strdata4)
print(strdata3+strdata5)
print(listdata3+listdata4)
print('\n')

# 시퀀스 자료 반복(*)

artist = 'TWICE'
sing = 'TT '
disp=artist+'가 부르는 '+sing*2+'명곡중 하나'
print(disp)
print('\n')

# 시퀀스 자료 크기 이해 len()

strdata6='HI'
strdata7='I Love You~!!!'
listdata5=['a','b','c',strdata6,strdata7]
print(len(strdata6))
print(len(strdata7))
print(len(listdata5))
print(len(listdata5[3]))
print('\n')

# 시퀀스 멤버체크 확인

ret1=5 in listdata5
ret2='b' in listdata5
print(ret1)
print(ret2)
ret3='H' in strdata6 # <값> in <자료>
ret4='h' in strdata6
print(ret3)
print(ret4)
print('\n')

