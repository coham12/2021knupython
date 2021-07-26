# 기본 문자열
s2 = 'hello, Sunghun!'
print(s2)

S2= "hello, Sunghun!"
print(S2)

s6 = '''hello, Sunghun!'''
print(s6)

# 이스케이프 코드
# \n, \t, \\, \', \"

longtext1 = """Hello, Sunghun!
my name is Sunghun JJAng Man"""
print(longtext1)

longtext2 = 'Hello, Sunghun!\smy name is Sunghun JJAng Man'
print(longtext2)

# string interpolation
a=123
new_q=f'{a}'
print(new_q)

# 문자열 옛날 방식
print(f'%s %s'% ('one', 'two'))

#pyformat
print('{} {}'. format('one', 'two'))

# f-string
a,b = 'one', 'two'
print(f'{a} {b}')

print(f'{b} {b}')

# example
name= "해달"
eng_name="Haedal"

print("안녕하세요. {1}입니다. my name is {0}". format(eng_name, name))
print(f'안녕하세요 {name}입니다.')

# 문자열 인덱싱
a = "Hello, Haedal!"
print(a[1])

#문자열 슬라이싱
a= 'hello, Haedal!'
print(a[4:9])

# 문자열의 길이를 구하는 len()
print(len(a))

#문자열의 최대, 최소를 구하는 max(), min()

a= '312'
b= 'bac'
print(min(a))
print(max(a))
print(min(b))
print(max(b)) 
print(a+b) #숫자다음 문자가옴
print(min(a+b))

#소문자, 대문자로 변환해주는 lower(), upper()
a= 'This is  Apple'
b= 'THIS IS  APPLE'
print(a.upper())
print(a.lower())
print(b.lower())

# 문자열을 구분자에 따라 나누는 splint()
a= "안녕, 나는, 수빈이양"
print(a.split(sep=','))
print(a.split())

b= "안녕 나는 수빈이 남자친구 성훈이야"
print(b.split())

# 여러개의 문자열 사이에 구분자를 넣어주는 join()

mylist= ['안녕', '나는', '성훈']

mystring ='//'.join(mylist)
print(mystring)