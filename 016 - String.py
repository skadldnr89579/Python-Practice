# String

strdata1='I am studying Python'
strdata2="Sucks"
strdata3="""I love you.
you love me,too"""
strdata4="He's a teacher."
strdata5='string"abc"has 3 characters'
print(strdata5)
print(strdata4)
print('\n')

# String Formatting

txt1='JAVA';txt2='Python'
num1=5;num2=10
print('나는 %s보다 %s이 더 좋아요'%(txt1,txt2))
print('나는 %s를 %d배 더 잘해요'%(txt2,num2))
print('%d+%d=%d'%(num1,num2,num1+num2))
print('%d%% 완료'%(num2))
print('\n')
"""
%s : 문자열에 대응
%d : 정수에 대응
%c : 문자나 기호 하나에 대응
%f : 실수에 대응
%% : % 기호 표시
"""
# Loading Bar
"""
from time import sleep
for i in range(100):
    msg='\r진행률 %d%%'%(i+1)
    print(''*len(msg),end='')
    print(msg,end='')
    sleep(0.1)
"""

# Escape

print('I love Python.\nPython is easier than Java')
print('My name : A\tAge:22\tSex:M')
print('이 문장은 화면폭에 비해 너무 길어서 보기 힘들어요.\
그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했어요.')
print('작은 따옴표(\')와 큰 따옴표(\")는 문자열을 정의할때 씁니다')

"""
\n : 줄 바꾸기
\t : 탭
\Enter : 줄 계속(다음줄도 계속되는 줄이라는 표시)
\\ : '\' 이 기호를 표시
\' \" : ' 과 " 기호 표시
"""

