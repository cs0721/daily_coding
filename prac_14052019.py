"""
Q1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. """

def three_five():
    for i in range(1000):
        total = 0
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(three_five())

"""
Q2. A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다. A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.
A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오. """

def tab_to_space(string):
    return string.replace("\t", "    ")
    
print(tab_to_space('abcd    efg'))

"""
Q3. A씨는 게시판 프로그램을 작성하고 있다.
A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.
입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수
A씨가 필요한 프로그램을 작성하시오.
"""
def page_generate(m, n):
    page = m // n
    if m % n != 0:
        page += 1
    return page

print(page_generate(0, 1)) # 0
print(page_generate(1, 1)) # 1
print(page_generate(2, 1)) # 2 
print(page_generate(1, 10)) # 0 
print(page_generate(10, 10)) # 1
print(page_generate(11, 10)) # 1

"""
Q4.이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

김씨와 이씨는 각각 몇 명 인가요?
"이재영"이란 이름이 몇 번 반복되나요?
중복을 제거한 이름을 출력하세요.
중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
"""
names = ['이유덕', '이재영', '권종표', '이재영', '박민호', '강상희', '이재영', '김지완', '최승혁', '이성연', '박영서', 
'박민호', '전경헌', '송정환', '김재성', '이유덕', '전경헌']

# 김씨와 이씨는 각각 몇 명인가요?
count_lee = 0
count_kim = 0
for i in range(len(names)):
    if names[i][0] == '이':
        count_lee += 1 
    if names[i][0] == '김':
        count_kim += 1
print('김씨는 {}명, 이씨는 {}명 입니다.'.format(count_kim, count_lee))

# "이재영"이란 이름이 몇 번 반복되나요?
count_ljy = 0
for i in range(len(names)):
    if names[i] == '이재영':
        count_ljy += 1

print("이재영씨는 {}번 반복 되었습니다".format(count_ljy))

# 중복을 제거한 이름을 출력하세요.
new_names = list(dict.fromkeys(names))
print(new_names)

# 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
print(sorted(new_names))