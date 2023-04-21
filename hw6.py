def multiple(dan, i):
    print(f'{dan}x{i}={dan*i:2d}', end = '  ')
    if dan < 5 :
        multiple(dan +1, i)
        
for i in range(1, 10):
    multiple(2, i)
    print()

print()

def multiple(dan, i):
    print(f'{dan}x{i}={dan*i:2d}', end = '  ')
    if dan <9:
        multiple(dan + 1, i)
        
for i in range(1, 10):
    multiple(6, i)
    print()
