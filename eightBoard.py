#Using a list to store the eightBoard. 
import random
random.seed(123)
eightBoard = [0,1,2,3,4,5,6,7,8]

def printState():
  check = 1
  for i in eightBoard:
    if i != 0:
      if check ==3:
        print(i)
        check = 1
      else:
        print(i,end=' ')
        check+=1
    else:
      if check ==3:
        print(' ')
        check =1
      else:
        print(' ',end = ' ')
        check +=1
def setState(state_str: str) -> list:
  temp = state_str.split(' ')
  state = [int(i) for i in temp]
  check = set(state)
  if len(check)!=len(state) or len(state)!=9:
    print('Error: invalid puzzle state')
    return -1
  if 0 not in check:
    print("Error: invalid puzzle state")
    return -1
  for i in check:
    if i >8:
      print("Error: invalid puzzle state")
      return -1
  for i in range(len(eightBoard)):
    eightBoard[i] = state[i]
  printState()
  return 1


def move(direction: str,verbose=True)->list:
  index = eightBoard.index(0)
  if direction =='up':
    if index -3<0:
      if verbose:
        print("Error: Invalid move")
      return -1
    else:
      temp = eightBoard[index-3]
      eightBoard[index-3] = 0
      eightBoard[index] = temp
      printState()
      return 1
  if direction =='down':
    if index +3>=9:
      if verbose:
        print("Error: Invalid move")
      return -1
    else:
      temp = eightBoard[index+3]
      eightBoard[index+3] = 0
      eightBoard[index] = temp
      printState()
      return 1
  if direction == 'right':
    temp_index = index+1
    if temp_index == 3 or temp_index == 6 or temp_index ==9:
      if verbose:
        print('Error: Invalid move')
      return -1
    else:
      temp = eightBoard[index+1]
      eightBoard[index+1] = 0
      eightBoard[index] = temp
      printState()
      return 1
  if direction == 'left':
    temp_index = index-1
    if temp_index == -1 or temp_index == 2 or temp_index ==5:
      if verbose:
        print('Error: Invalid move')
      return -1
    else:
      temp = eightBoard[index-1]
      eightBoard[index-1] = 0
      eightBoard[index] = temp
      printState()
      return 1

def scrambleState(n: int) -> list:
  eightBoard.clear()
  eightBoard.extend([0,1,2,3,4,5,6,7,8])
  movements = {0:'up',1:'down',2:'left',3:'right'}
  if n <=0:
    print('No movement required')
    printState()
    return None
  for i in n:
    num = random.randint(0,3)
    detect = move(movements[move])
    while detect == -1:
      detect = move(movements[random.randint(0,3)])
  printState()
  return None

setState('1 0 2 3 4 5 6 7 8')
scrambleState(0)
