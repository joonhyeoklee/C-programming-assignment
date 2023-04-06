def rep_char(c,n):
    print(c*n)


def draw_line_string(msg1):
    nstr1 = len('Hello '+f'{msg1}')
    msg2 = 'Welcome to Seoul. '
    nstr2 = len(msg2)
    if nstr1>nstr2:
        rep_char('-', nstr1)
    else :
        rep_char('-', nstr2)
    print(' Hello', f'{msg1},')
    print(f' {msg2} ')
    if nstr1>nstr2:
        rep_char('-', nstr1)
    else :
        rep_char('-', nstr2)
   
    

name = input('Input his/her name:')
draw_line_string(name)
