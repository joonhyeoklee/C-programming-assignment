import os
import pickle

def input_scores(s):
    i=1
    print("[점수 입력]")
    while True:
      n = int(input(f'#{i}? '))
      if n < 0:
        return False
      s.append(n)
      i += 1

def show(s):
  sum = 0
  print()
  for i in s:
    sum += i

  print('개인점수: ', end = '')
  for i in s:
    print(i, end = ' ')
  print()
  print(f'평균:{sum / len(s):.1f}')

def save_data(s,filepath):
  with open(filepath,'wb') as file:
    pickle.dump(s,file)

def load_data(filepath):
  with open(filepath,'rb') as file:
    s = pickle.load(file)
    return s

filename="score.bin"

if os.path.exists(filename):
  print('[파일읽기]')
  print()
  print('[점수출력]', end ='')
  s = load_data(filename)

else:
  s = []
  while True:
    if input_scores(s) == False:
      break
  save_data(s,filename)
  
show(s)
