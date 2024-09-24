#Importing the necessary libraries
#Random to help with the scrambleState function
#To generate random moves
#and sys to help parse the command (to get the txt file)
import random
import sys
from heapq import heappush,heappop
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
#Setting random seed to ensure consistency
seed = 23
random.seed(seed)
#Setting up the eight board as its default (goal state)
#To ensure you can start printing the board without setting it up
eightBoard = [0,1,2,3,4,5,6,7,8]
goal = [0,1,2,3,4,5,6,7,8]
#node_set = set()

#Function to print out the state
def printState(eightBoard=eightBoard):
  check = 1 #Checking how many times the number has been printed
  #If it it at more than 3
  #Print to a new line
  #Does not perform whether the board is valid, that is offloaded to setstate
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

#Function to set the state
#Takes in a string of numbers (separated by a space)
#Verbose is for internal use
#Used so that if the code sets the default state, it does not print the state too many times
def setState(state_str: str,verbose=True,eightBoard=eightBoard):
  temp = state_str.split(' ')
  #print(state_str)
  state = [int(i) for i in temp] #Split up the numbers and add them to a list called temp
  #Then convert them to integers
  check = set(state) #A quick check of the set for duplicate elements
  if len(check)!=len(state) or len(state)!=9:
    #Since the empty piece is 0, there should be nine elements 
    #Since there should not be any duplicates, the length of the set and list should be the same
    #If not, there is an error
    print('Error: invalid puzzle state')
    #print(state)
    #print
    return -1
  if 0 not in check:
    #No empty spaces, thus not a valid state
    print("Error: invalid puzzle state")
    return -1
  for i in check:
    #Run through all elements in list to make sure they are valid
    #Since the list should be short (longer ones are dealt in the code block above)
    #Running through it does not take up much time or space
    if i >8 or i <0:
      print("Error: invalid puzzle state")
      return -1
  #Setting up the eightboard
  #Making all element of the eightboard the one in set (the input)
  for i in range(len(eightBoard)):
    eightBoard[i] = state[i]
  if verbose:
    printState()
  return 1

#The move function
#Move is referring to the direction that the blanck space moves 
#If a move is not valid, the state is not changed
#Verbosity is to ensure that for scramblestate
#Every move the program is not outputting the result
def move(direction: str,verbose=True,eightBoard = eightBoard):
  #print(f'verbose is {verbose}')
  index = eightBoard.index(0)#Getting the index for manipulation
  if direction =='up':
    #print('in up')
    #For the up direction, the index of the space is essentially lessened by 3
    #Thus, if the index is less than 3
    #The move is invalid
    if index -3<0:
      if verbose:
        #print('in verbose')
        print("Error: Invalid move")
      return -1
    else:
      #Code to swap (creating a temporary variable to store the intermediate value)
      temp = eightBoard[index-3]
      eightBoard[index-3] = 0
      eightBoard[index] = temp
      if verbose:
        #print('in verbose')
        printState()
      return 1
  if direction =='down':
    #print('in down')
    #For the down direction, it is increasing the index by 3
    #Thus if it exceeds 8, the move is invalid
    if index +3>=9:
      if verbose:
        #print('in verbose')
        print("Error: Invalid move")
      return -1
    else:
      #For the valid ones, swap (same code as above)
      temp = eightBoard[index+3]
      eightBoard[index+3] = 0
      eightBoard[index] = temp
      if verbose:
        #print('in verbose')
        printState()
      return 1
  if direction == 'right':
    #To move the space right
    #We are adding one to the index
    #However as we assume it does not wrap around
    #If it exceeds the last element in the row, the move is invalid
    #print('in right')
    temp_index = index+1
    if temp_index == 3 or temp_index == 6 or temp_index ==9:
      if verbose:
        #print('in verbose')
        print('Error: Invalid move')
      return -1
    else:
      #Swap the elements if it is valid
      temp = eightBoard[index+1]
      eightBoard[index+1] = 0
      eightBoard[index] = temp
      if verbose:
        #print('in verbose')
        printState()
      return 1
  if direction == 'left':
    #print('in left')
    #To move the space left, the index is minus one
    #Thus if the space is at the end of its row, the move is invalid
    temp_index = index-1
    if temp_index == -1 or temp_index == 2 or temp_index ==5:
      if verbose:
        #print('in verbose')
        print('Error: Invalid move')
      return -1
    else:
      #If the move is valid, swap the places
      temp = eightBoard[index-1]
      eightBoard[index-1] = 0
      eightBoard[index] = temp
      if verbose:
        #print('in verbose')
        printState()
      return 1

#Function to scramble the goal state 
def scrambleState(n: str,verbosity=False,eightBoard=eightBoard):
  setState('0 1 2 3 4 5 6 7 8')#First set up the goal state
  print()
  movements = {0:'up',1:'down',2:'left',3:'right'} #Defining a dictionary of moves to allow generating random integers
  list_move = []
  print(f'n is {int(n)}')
  try:#To ensure that the input is an integer
    n = int(n)
    if n <=0:
      #Since scrambling 0 moves is equal to not moving
      #And you can't make negative moves 
      #Thus if the number of moves is negative or zero, make no move
      print('No movement required')
      printState()
      return None
    num = 0
    while num<n: #Repeat 
      temp = random.randint(0,3)
      detect = move(movements[temp],verbose = False) #Check if the move is valid
      while detect ==-1:
        #If not, repeat the move until it is
        temp = random.randint(0,3)
        detect = move(movements[temp],verbose = False)
      else:
        num +=1 #Increasing the move counter by 1
        list_move.append(movements[temp])
        #printState()
        #print()
    printState()
    return eightBoard
    if verbosity:
      n=0
      for i in list_move:
        if n%5==0:
          print()
          print()
        print(i,end=' ')
        n+=1
  except:
    #When the input is not an integer, which is invalid
    print("Cannot scramble non-integer times, no scrambling done")
    printState()
    return None

#Main function for the program
#Takes in a filename (specified when starting program)
def main(filename):
  #Opening the file, reading line by line, then stripping the white spaces to make it easier to process
  #To ensure that all other commands will work, the default state when opening up this program will be the goal state
  setState('0 1 2 3 4 5 6 7 8',verbose=False)
  with open(filename,'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()

  #Display the comment
  i = 1
  for line in lines:
    if line[0] == '#':
      print(line)
    elif line[0]=='/' and line[1]=='/':
      print(line)
    #Let's know deal with the actual moves
    else:
      print(line)
      words = line.split(' ')
      #Make the first word lower case so it can accept both upper and lower cases
      words[0] = words[0].lower()
      words[0] = words[0].strip()
      #print(words[0])
      if words[0] == 'setstate':
        inp = ' '.join(words[1:])
        #print(inp)
        detect = setState(inp,verbose=True)
        if detect == -1:
          print('Due to invalid state, defaulting back to the goal state')
          setState('0 1 2 3 4 5 6 7 8',verbose=True)
      elif words[0]=='move':
        #print(words[1])
        move(words[1].strip(),verbose=True)
      elif words[0] == 'scramblestate':

        scrambleState(words[1])
      elif words[0]=='printstate':
        printState()
      elif words[0].strip().lower()=='heuristic':
        if words[1].strip().lower()=='h1':
          print(f'Number of misplaced tiles is {h1()}')
        elif words[1].strip().lower()=='h2':
          print(f'The Manhattan distnace is {h2()}')
        else:
          print(f'Undefined heuristic at line{i}, please only input h1 (the number of misplaced tiles) or h2 (the manhattan distance)')
      elif words[0].strip().lower() == 'solve':
        node_num = 1000
        '''try:
          node_num = int(words[-1])
          if node_num <=0:
            print(f'Maximum node number cannot be less than 1, defaulting to 1,000')
            node_num = 1000
        except:
          node_num = 1000
          print(f'Invalid/no maximum node provided, defaulting to 1,000')'''
        if 'maxnode' in words[-1].strip().lower():
          node_num = 1000
          sub_words = words[-1].split('=')
          sub_words[-1] = sub_words[-1].strip()
          #print(sub_words)
          try:
            node_num = int(sub_words[-1].strip())
            #print('here')
            if node_num<=0:
              print(f'Maximum node number cannot be less than 1, defaulting to 1,000')
              node_num = 1000
            else:
              #node_num = 1000
              print(f'Setting maximum node number as {node_num}')
          except:
            print(f'Invalid/no maximum node number, defaulting to 1,000')
        if words[1].strip().lower() == 'bfs':
          BFS(node_num)
        elif words[1].strip().lower()=='dfs':
          DFS(node_num)
        elif words[1].strip().lower()=='a*':
          heuristic = words[2].strip().lower()
          if heuristic!='h1' and heuristic!='h2':
            #print(heuristic=='h2')
            print(f'Invalid/missing Heursitc in line {i}')
            print(f'Defaulting to the default, h2')
            heuristic = 'h2'
          if len(words)>=4:
            if 'maxnode' not in words[3]:
              #Testing for Ex 5 in HW3
              AStar(heuristic,maxnode=node_num,verbosity=True)
            else:
              AStar(heuristic,maxnode=node_num)
          else:
            AStar(heuristic,maxnode=node_num)
        else:
          print(f'Error: invalid command: {i}')
      else:
        print(f"Error: invalid command: {i}")
    i+=1

def check_solution(state):
  #check = True
  goal = [0,1,2,3,4,5,6,7,8]
  for i in range(len(state)):
    if goal[i] != state[i]:
      return False
  return True 
#implementing BFS as a for loop as it's easier 
def print_moves(moves):
  for i in moves:
    print(f'Move {i}')

def BFS(maxnode=1000,eightBoard=eightBoard):
  queue = [(eightBoard,[])]
  visited = set()
  node_num = 1
  repeated_num = 0
  #length = 0
  #sequence = []

  while queue:
    if node_num>=maxnode:
      print(f'Error: max node number {maxnode} reached')
      return
    current_state,path = queue.pop(0)
    if check_solution(current_state):
      print(f'Nodes created during search: {node_num}')
      print(f'Solution length {len(path)}')
      print(f'Found {repeated_num} duplicated')
      print_moves(path)
      return node_num,len(path)

    eightBoard=current_state.copy()
    #print(f'current_state is {current_state}')
    movements = {0:'left',1:'right',2:'up',3:'down'}
    for i in movements:
      #print()
      #print(f'eightBoard is {eightBoard}')
      #print(f'move is {movements[i]}')
      if move(movements[i],verbose=False,eightBoard=eightBoard) == 1:
        #print('in')
        #path.append(movements[i])
        if tuple(eightBoard) not in visited:
          visited.add(tuple(eightBoard))
          queue.append((eightBoard,path+[movements[i]]))
          node_num+=1
        else:
          repeated_num+=1
      eightBoard = current_state.copy()
        #print(f'queue is {queue}')
        #print(f'eightBoard is {eightBoard}')

def DFS(maxnode=1000,eightBoard = eightBoard):
  #print('In DFS (yay)')
  stack = [(eightBoard,[])]
  visited = set()
  node_num = 1
  repeated_num = 0
  while stack:
    #print('in here')
    if node_num>=maxnode:
      print(f'Error: max node number {node_num} reached')
      return
    current_state,path = stack.pop(-1)
    if check_solution(current_state):
      
      print(f'Nodes created during search: {node_num}')
      print(f'Checked {repeated_num} states that are duplicates')
      print(f'Solution length {len(path)}')
      #print_moves(path)
      return node_num,len(path)
    #eightBoard=current_state.copy()
    movements = {0:'up',1:'down',2:'right',3:'left'}
    #Temporary eightBoard to see the moves
    #temp = eightBoard.copy()
    for i in range(4):
      temp_board = current_state.copy()
      if move(movements[i], eightBoard=temp_board, verbose=False) != -1:

        if tuple(temp_board) not in visited:
          visited.add(tuple(temp_board))
          stack.append((temp_board,path+[movements[i]]))
          node_num+=1
        else:
          repeated_num+=1
    if node_num%1000==0:
      print(f'Evaluated {node_num} nodes')
  else:
    print('Stack is now empty (sad)')

def h1(eightBoard = eightBoard,goal=goal):
  #h1 is the number of tiles off of place
  num = 0
  for i in range(len(eightBoard)):
    if eightBoard[i]!=0:
      if eightBoard[i]!=goal[i]:
        num+=1
  return num

def h2(eightBoard = eightBoard,goal=goal):
  #h2 is the manhattan distance
  distance = 0
  for i in goal:
    if i!= 0:
      goal_col = i//3
      goal_row = i%3
      e_col = eightBoard.index(i)//3
      e_row = eightBoard.index(i)%3
      distance+=abs(goal_col-e_col)+abs(goal_row-e_row)
  return distance

def AStar(heuristic,maxnode = 1000, eightBoard=eightBoard,goal=goal,verbosity=False):
  movements = {0:'left',1:'right',2:'up',3:'down'}
  h=0
  if heuristic == 'h1':
    h = h1(eightBoard,goal)
  elif heuristic == 'h2':
    h = h2(eightBoard,goal)
  else:
    return
  queue = []
  visited = set()
  node_num = 1
  #first number being the priority
  #second element is the eightboard
  #third element is the path list
  heappush(queue,(h,eightBoard,[]))
  visited.add(tuple(eightBoard))
  length = 0
  #sequence = []

  while queue:
    if node_num>=maxnode:
      print(f'Error: max node number {maxnode} reached')
      return
    f,current_state,path = heappop(queue)
    #print(f'Expanding state {current_state}')
    #visited.add(tuple(current_state))
    if check_solution(current_state):
      print(f'Nodes created during search: {node_num}')
      print(f'Solution length {len(path)}')
      print_moves(path)
      return node_num,len(path)

    eightBoard=current_state.copy()
    #print(f'current_state is {current_state}')
    for i in movements:
      #length+=1
      #print()
      #print(f'eightBoard is {eightBoard}')
      #print(f'move is {movements[i]}')
      if move(movements[i],verbose=False,eightBoard=eightBoard) == 1:
        #print('in')
        #path.append(movements[i])
        if tuple(eightBoard) not in visited:
          h=0
          if verbosity:
            print(f'Expanding state {tuple(eightBoard)}')
          if heuristic == 'h1':
            h = h1(eightBoard,goal)
          elif heuristic == 'h2':
            h = h2(eightBoard,goal)
          else:
            return
          heappush(queue,(h+len(path)+1,eightBoard,path+[movements[i]]))
          #queue.append((eightBoard,path+[movements[i]]))
          node_num+=1
          visited.add(tuple(eightBoard))
        else:
          if verbosity:
            print(f'{tuple(eightBoard)} already in visited, visited is the set: ')
            print(visited)
        eightBoard = current_state.copy()
        #print(f'queue is {queue}')
        #print(f'eightBoard is {eightBoard}')

def f(x,d=2,n=2):
  sol = 1
  for i in range(1,d+1):
    sol+=x**i
  return sol-n
def df(x,d=2,n=2):
  sol = 1
  for i in range(1,d+1):
    sol+=i*x**(i-1)
  return sol
def Newton(f,df,guess,args=(),tol=1e-8,iter = 1, max_iter = 500,verbosity=False,x_k=[]):
  xn = guess
  xn1 = xn - (f(xn,*args)/df(xn,*args))
  if np.abs(xn1-xn)<tol or iter>=max_iter:
    if verbosity:
      print(f'At the {iter} iteration, the estimate is {xn1}')
      if iter>=max_iter:
        return {'val':xn1,'iterations':iter,'x_k':x_k,'maxed':True}
      return {'val':xn1,'iterations':iter,'x_k':x_k,'maxed':False}
    return xn1
  else:
    if verbosity:
      print(f'At the {iter} iteration, the estimate is {xn1}, and f(xn) is {f(xn)}')
      x_k.append(xn1)
    return Newton(f,df,xn1,args=args,tol=tol,iter=iter+1,max_iter=max_iter,verbosity=verbosity,x_k=x_k)

def EBF(d,n,tol=1e-2):
  guess = 1
  return Newton(f,df,guess,args=(d,n),tol=tol,max_iter=5000,verbosity=False)

'''def generate_boards(seed=seed):
  random.seed(seed)
  boards=[]
  seed = seed
  for t in range(1,11):
    i = str(t)
    #testing to if it is indeed the right depth
    temp = scrambleState(i,eightBoard=eightBoard)
    num_nodes,path=AStar('h2',maxnode=1e7)
    while path!=t:
      seed+=1
      random.seed(seed)
      temp = scrambleState(i,eightBoard=eightBoard)
      num_nodes,path=AStar('h2',maxnode=1e7)
    boards.append(temp)
  return boards'''
def truncate(number,digits):
  factor = 10**digits
  return int(number * factor) / factor
def compare(seed=seed):
  with open('dict.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Algorithm','Optimal Depth','# of Nodes','Depth','Effective Branching Factor'])
    #boards = generate_boards()
    n = 1
    for i in range(1,21):
      #Testing 
      temp = scrambleState(str(i))
      node_num,path = AStar('h2',maxnode=1e5)
      while path!=i:
        seed+=1
        random.seed(seed)
        temp = scrambleState(str(i))
        node_num,path=AStar('h2',maxnode=1e5)

      node_num,path=DFS(maxnode=1e10,eightBoard=temp)
      writer.writerow(['DFS',n,node_num,path,truncate(EBF(path,node_num),3)])
      #scrambleState(i)
      node_num,path=BFS(maxnode=1e10,eightBoard=temp)
      writer.writerow(['BFS',n,node_num,path,truncate(EBF(path,node_num),3)])
      #scrambleState(i)
      node_num,path=AStar('h1',maxnode=1e7,eightBoard=temp)
      writer.writerow(['A*(h1)',n,node_num,path,truncate(EBF(path,node_num),3)])
      #scrambleState(i)
      node_num,path=AStar('h2',maxnode=1e7,eightBoard=temp)
      writer.writerow(['A*(h2)',n,node_num,path,truncate(EBF(path,node_num),3)])
      n+=1
  #return master_dict



    
'''if __name__=='__main__':
  #A quick check to see if the instruction txt is included
  if len(sys.argv)!=2:
    if len(sys.argv)<2:
      print(f'Did not provide an instruction text, please insert the txt file after the python file in terminal')
      #main('Test1.txt')
    else:
      print(f'Too many arguments detected. Please only input one file.')
      sys.exit(1)
    #sys.exit(1)
  main(sys.argv[1])'''

#This has been commendted out as it takes a very long while to run
#compare

#loading data to plot
'''DFS_list = []
BFS_list=[]
h1_list = []
h2_list = []
with open('dict.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  for row in spamreader:
    if row[0]=='DFS':
      DFS_list.append(float(row[-1]))
    elif row[0]=='BFS':
      BFS_list.append(float(row[-1]))
    elif row[0]=='A*(h2)':
      h2_list.append(float(row[-1]))
    elif row[0]=='A*(h1)':
      h1_list.append(float(row[-1]))
#Plotting the result
#h1_list.pop(0)
fig = plt.figure()
ax = fig.subplots()
ax.plot(np.arange(1,21),DFS_list,label='DFS')
ax.plot(np.arange(1,21),BFS_list,label='BFS')
ax.plot(np.arange(1,21),h1_list,label='A*(h1)')
ax.plot(np.arange(1,21),h2_list,label='A*(h2)')
ax.set_title('Convergence of Branching Factor for Different Algorithms')
ax.set_xlabel('Depth')
ax.set_ylabel('Branching Factor')
ax.legend()
plt.savefig('Convergence.png',dpi=1200)'''

#Showing it works
print(f'For an effective branching factor of 2, I calculated {EBF(2,7,tol=1e-8)}')
print(f'For an effective branching factor of 3, I calcualted {EBF(3,40,tol=1e-8)}')
'''print('\n'*4)
#For DFS 
eightBoard=scrambleState(5)
DFS(maxnode=1e6,eightBoard=eightBoard)
#print(EBF(3,1))'''

