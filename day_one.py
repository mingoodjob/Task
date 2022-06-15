# 과제

#  1. args, kwargs를 사용하는 예제 코드 짜보기

class Example():
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f'args: {self.args}, kwargs: {self.kwargs}'

#  2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
# mutable은 값이 변한다는 뜻이고, immutable은 값이 변하지 않는다는 의미이다.         

class Example2():
    def __init__(self, x):
        self.x = x
        self.z = [1,2,3]

    def immutable(self):
        self.y = self.x
        self.y += '코딩클럽'        

        return f'{self.y}'

    def mutable(self,*args):
        self.z.append(args)

        return f'{self.z}'


if __name__ == '__main__':
    ex = Example(1, 2)
    print(ex)
    ex2 = Example2('스파르타')
    print('immutable(값이 변하지 않음) : ' + ex2.immutable())
    print('mutable(값이 변함) : ' + ex2.mutable(4,5,6))

#  3. DB Field에서 사용되는 Key 종류와 특징 서술하기    

# Primary Key (기본키 , 다른 항목과 중복 불가 , 기본키는 절대 Null 이 될수 없음.)
# Foring Key (외래키 , 부모 테이블의 기본키, 고유키를 외래키로 지정할 수 있다. , 외래키는 Null 가능)
# Unique Key (고유키 , 다른 항목과 중복 불가 , 고유키는 Null 가능)

#  4. django에서 queryset과 object는 어떻게 다른지 서술하기

# 쿼리셋은 쿼리를 실행하고 나서 반환되는 객체이다.

# 데이터베이스로 부터 읽고 필터를 걸거나 정렬 가능

# 리스트 구조 이지만, 기본 자료 구조가 아니라 읽고 쓰기 위해선 자료형 변환 해야함

# 오브젝트는 특정한 형식의 데이터를 저장하고 읽을 수 있다.

# 오브젝트를 이용하면 자료형을 변환하지 않고 자료를 읽고 쓸 수 있다.
