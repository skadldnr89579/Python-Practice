# Python Module

import time
print('5초간 스톱')
time.sleep(5)
print('5초가 지났음')


import mylib
ret1=mylib.add_txt('Korea','First')
ret2=mylib.reverse(1,2,3)
print(ret1)
print(ret2)

# Python Package

#import mypackage.mylib

#ret1-mypackage.mylib.add_txt('Korea','First')
#ret2=mypackage.mylib.reverse(1,2,3)

# Python Module import

import time
import mylib
import mypackage.mylib

time.sleep(1)
mylib.add_txt('I am','Python')
mypackage.mylib.reverse(1,2,3)

"""
import 모듈이름
import 패키지이름.모듈이름
"""

# Pythom Module import (from~import)

from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)
mylib.add_txt('I am','Python')
reverse(1,2,3)

# Python Module import (import~as)

import mypackage as mp
import mypackage.mylib as ml

ret1=mp.mylib.add_txt('Korea','First')
ret2=ml.reverse(1,2,3)

"""
import 이름이 긴 모듈명 as 별명
"""

# open, close
"""
open(파일이름,모드) 
"""
f1=open('text.txt','r')
f2=open('d:/myimages/mypicture1.jpg','rb')

# 오픈 파일을 처리하는 코드를 작성함

f1.close()
f2.close()

"""
텍스트 모드로 읽고,쓰기 (r/rt, w/wt)
텍스트 모드로 파일 마지막에 추가 (a/at)
바이너리 모드로 읽기, 쓰기 (rb,wb)
바이너리 모드로 파일 마지막에 추가 (ab)
"""
