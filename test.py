### Description
# 이것은 그냥 테스트를 위한 것이다.

import time
import itertools
import math
import functools
from typing import Optional, Union

# 함수 수행시간을 측정하는 데코레이터
def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print(f"함수 수행시간: {end - start:.6f} 초")
        return result
    return wrapper

# 역순 반복자 클래스
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result

if __name__ == '__main__':

    print('B')
    print('c')

    # f-string 예제
    age = 22
    mystr = f'my age is: {age:^10}'
    print(mystr)

    # 문자열 메서드 예제
    a = ','.join('abcd')
    print(a)
    print(a.replace(',', 'b'))
    print(a.split(','))
    print(a.isalpha())
    print(a.startswith('a'))

    # 리스트와 튜플 예제
    a = [1, 2]
    print(a)
    b = (3, 4)
    a.extend(b)
    print(a)
    a.reverse()
    print(a)

    # 문자열 zip, map 예제
    a = 'abc'
    b = 'def'
    for i, j in zip(map(str.upper, a), b):
        print(i, j)

    # 시간 관련 예제
    print(time.time())
    t = time.localtime()
    print(t)
    print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    print(time.ctime())

    print(chr(14))

    # 데코레이터 사용 예제
    @elapsed
    def myfunc():
        print("함수가 실행됩니다.")

    myfunc()

    @elapsed
    def myfunc_with_msg(msg):
        """ 데코레이터 확인 함수 """
        print(f"'{msg}'을 출력합니다.")

    myfunc_with_msg("You need python")

    # ReverseIterator 사용 예제
    i = ReverseIterator([1, 2, 3])
    for item in i:
        print(item)

    # 제너레이터 예제
    gen = (i * i for i in range(1, 1000))
    for _ in range(6):
        print(next(gen))

    # 타입 애너테이션 예제
    a: int = 1
    print(a)
    a = 'a'
    print(a)
