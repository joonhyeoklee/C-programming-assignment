def read_single_digit(num):
    if num == 1:
        a = '일'
        print(a,end=' ')
    elif num == 2:
        b = '이'
        print(b,end=' ')
    elif num == 3:
        c = '삼'
        print(c,end=' ')
    elif num == 4:
        d = '사'
        print(d,end=' ')
    elif num == 5:
        e = '오'
        print(e,end=' ')
    elif num == 6:
        f = '육'
        print(f,end=' ')
    elif num == 7:
        g = '칠'
        print(g,end=' ')
    elif num == 8:
        h = '팔'
        print(h,end=' ')
    elif num == 9:
        i = '구'
        print(i,end=' ')
    elif num == 0:
        j = '영'
        print(j,end=' ')

def read_number(f,s,t):
    read_single_digit(f),read_single_digit(s),read_single_digit(t)



read_int = input('세자리 정수 입력:')
first = int(read_int[0])
second = int(read_int[1])
third = int(read_int[2])
read_number(first,second,third)
