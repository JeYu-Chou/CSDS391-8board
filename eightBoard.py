#Importing the necessary libraries
#Random to help with the scrambleState function
#To generate random moves
#and sys to help parse the command (to get the txt file)
import random
import sys
#Setting random seed to ensure consistency
seed = 321
random.seed(seed)
#Setting up the eight board as its default (goal state)
#To ensure you can start printing the board without setting it up
eightBoard = [0,1,2,3,4,5,6,7,8]

#Function to print out the state
def printState():
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
def setState(state_str: str,verbose=True):
  temp = state_str.split(' ')
  state = [int(i) for i in temp] #Split up the numbers and add them to a list called temp
  #Then convert them to integers
  check = set(state) #A quick check of the set for duplicate elements
  if len(check)!=len(state) or len(state)!=9:
    #Since the empty piece is 0, there should be nine elements 
    #Since there should not be any duplicates, the length of the set and list should be the same
    #If not, there is an error
    print('Error: invalid puzzle state')
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
def move(direction: str,verbose=True):
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
def scrambleState(n: str):
  setState('0 1 2 3 4 5 6 7 8')#First set up the goal state
  print()
  movements = {0:'up',1:'down',2:'left',3:'right'} #Defining a dictionary of moves to allow generating random integers
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
      detect = move(movements[random.randint(0,3)],verbose = False) #Check if the move is valid
      while detect ==-1:
        #If not, repeat the move until it is
        detect = move(movements[random.randint(0,3)],verbose = False)
      else:
        num +=1 #Increasing the move counter by 1
        #printState()
        #print()
    printState()
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
      else:
        print(f"Error: invalid command: {i}")
    i+=1
    
#Main function to run 
if __name__=='__main__':
  #A quick check to see if the instruction txt is included
  if len(sys.argv)!=2:
    if len(sys.argv)<2:
      print(f'Did not provide an instruction text, please insert the txt file after the python file in terminal')
      #main('Test1.txt')
    else:
      print(f'Too many arguments detected. Please only input one file.')
      sys.exit(1)
    #sys.exit(1)
  main(sys.argv[1])
    
#setState('1 0 2 3 4 5 6 7 8')
#move('up')
