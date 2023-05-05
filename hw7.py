shopping_bag = {}

print('[구입]')
while True:
  item = input('상품명? ')
  if item == '':
    break
  num = input('수량은? ')
  shopping_bag[item] = int(num)
  
  print(f'장바구니에 {item} {num}개가 담겼습니다')
  print()
print(f'>>> 장바구니 보기 {shopping_bag}')

print()
print('[검색]')
s = input('장바구니에서 확인하고자하는 상품은? ')
print(f'{s}은(는) {shopping_bag.get(s)}개 담겨 있습니다.')
