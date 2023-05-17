def buy(i):
    print('[구입]')
    i = input('상품명? ')
    if i== '':
        return False
    num = input('수량은? ')
    shopping_bag[i] = int(num)
    print(f'장바구니에 {i} {num}개가 담겼습니다.')
    print()


def show(a):
    print()
    print(f'>>> 장바구니 보기 {a}')
    print()

def find(e):
    print('[검색]')
    s = input('장바구니에서 확인하고자하는 상품은? ')
    if s in e:
        print(f'{s}은(는) {e.get(s)}개 담겨 있습니다.')
    else:
        print(f'{s}은(는) 없습니다.')
        
   
shopping_bag = {}
while True :
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)


    
