def get_fixed_price(price):
    real = 100/(100-discount)*price
    return real

discount = int(input("할인율은?"))
a = int(input("A상품의 할인된 가격은?"))
b = int(input("B상품의 할인된 가격은?"))
result=get_fixed_price(a)
print('A상품의 정가는',result,'원')
result=get_fixed_price(b)
print('B상품의 정가는',result,'원')
