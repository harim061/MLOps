#!/usr/bin/env python3
from random import choices

def add(x,y):
    print(f"함수가 실행됩니다. {x}+{y} 연산 결과를 반환합니다.")
    return x+y

numbers = range(1,10)

for num in numbers:
    xx = choices(numbers)[0]
    yy = choices(numbers)[0]

print(add(xx,yy))