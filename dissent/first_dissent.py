"""
https://wikidocs.net/134909
"""
from time import sleep


# 먼저 이 위키는 한개의 함수에 대해서 설명한다.
def longtime_job():
    print("job start")
    sleep(1)
    return "done"


# 이게 이터레이터라고 한다
# >>> list_job = iter([longtime_job() for i in range(5)])

# 이게 제너레이터라고 한다.
# >>> list_job = (longtime_job() for i in range(5))

# 그런데 나는 이게 잘못되었다고 생각한다.
# 리스트 컴프리헨션, 제너레이터 컴프리헨션 모두 제너레이터로 작동한다.
# 그런데 이터레이터를 입히기 위해서 longtime_job 바깥에 list를 씌우면
# list는 모든 원소를 계산해서 가지고 있으려고 하기때문에 모두 계산한다.
# 결과적으로 이터레이로 변하긴 했지만, 리스트를 써서 강제적으로 제너레이터 -> 리스트 -> 이터레이터 변환과정을 거친다.
# 그러면 당연히 함수는 5번 한꺼번에 실행된다.
# 올바르게 이터레이터를 고쳐보자


class MyIterator:
    """
    구현한 이터레이터
    1. 클래스 구현
    2. __iter__는 자기 자신 반환
    3. __next__에 다음 반환할 값 정의
    """

    def __iter__(self):
        return self

    def __next__(self):
        return longtime_job()


def myGenerator():
    """
    구현한 제너레이터
    """
    yield longtime_job()


print(type(MyIterator))  # <class type>
mi = MyIterator()
print(type(mi))  # <class __main.MyIterator>
print(type(myGenerator))  # <class function>
f = myGenerator()
print(type(f))  # <class generator>

mi.__next__()  # 이터레이터

# 결과적으로 __next__() 를 호출하면 한번 함수가 실행될 뿐이다.
# 위키의 설명은 마치 이터레이터로 변경하면 모든 걸 계산한 다음 하나씩 돌려주는 것처럼 설명한다.
# 하지만 제대로 이터레이터를 설계하면 하나씩 메모리에 올리는 이터레이터가 된다.

# 첫번쨰 반박 종료
