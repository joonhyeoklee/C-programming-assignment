def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    s = r*r*3.14
    return s

r=get_radius('넓이를 구하고자 하는 원의 반지름은?')
result=get_circle_area(r)
print('반지름'+str(r)+'인 원의 넓이 = 3.14 x '+str(r)+' x '+str(r)+'='+str(result))  
