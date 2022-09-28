import copy

def tilepuzzle(start, goal):
  return reverse (statesearchTile([start], goal, path =[]))


def statesearchTile(unexplored, goal, path, depth = 32): 

    print("-------------")
    print("Path so far:")
    print(path)
    print("Unexplored states remaining:")
    print(unexplored)
    print()
    #input()
    
    if len(path) >= depth:
        return []
    
    #python doesn't do well if delete original unexplored list in loop
    newunexplored = [x for x in unexplored] #copy of list
    for state in newunexplored:
      if state in path:
        print("Deleting option from unexplored:")
        unexplored.remove(state)
    #append to new path, iterate to new path, then remove it  

    if unexplored == []: #[RR_BB]
        print("Unexplored is empty")
        return []
    
    if goal == unexplored[0]: # does the goal == first element in the list
      print("Goal found!")
      print()
      return cons(goal,path) # inserts goal at beginning of path
    else:
      print("Current state is not the goal state")
      print(unexplored[0])
      print()
      print("Generating new states")
      print()
      newStates = generateNewStates(unexplored[0])
      result = statesearchTile(
        newStates,
        goal,
        cons(unexplored[0], path)
      )
    if result != []:
      return result
    else: 
     return statesearchTile(unexplored[1:], goal,path)



def swapTiles(old_matrix,zero_pos,_dir):
    ''' 
    Swaps two tiles
    zero_pos is a tuple (row,column) of a tile.
    _dir is the direction to swap it: up, down, left, right (string)
    '''
    
    # determine coordinates of other tile
    zero_row,zero_col = zero_pos       #position of 0 (row, column)
    if _dir == 'up':
        other_row,other_col = zero_row-1,zero_col # r2,c2 f tile to switch with
    elif _dir == 'down':
        other_row,other_col = zero_row+1,zero_col
    elif _dir == 'right':
        other_row,other_col = zero_row,zero_col+1
    else:
        other_row,other_col = zero_row,zero_col-1

    # *************************NOTE**************************************
    # There was a bug here. The current state was being updated "in place"
    # which meant that once you moved right, the initial state was lost
    # and replaced by that right move. We can fix that by making a deep
    # copy of the matrix before updating it.
    # *************************NOTE**************************************

    # perform swap
    new_matrix = copy.deepcopy(old_matrix)
    new_matrix[zero_row][zero_col],new_matrix[other_row][other_col] = old_matrix[other_row][other_col],old_matrix[zero_row][zero_col]
    
    return new_matrix

def generateNew(currState,_dir):
    result = []
    # look through the matrix for the 0 and see if it can be moved in the requested direction. If so, then do the swap, and append it to the result
    
    # find the position of the zero in the currentState of the test matrix
    for row in range(3):
        for column in range(3):
            if currState[row][column] == 0:
                zero_row,zero_col = row,column
    
    # *************************NOTE**************************************
    # Because of the bug in swapTiles, after moving right, currState
    # was immediately changed. Rather than restarting at the initial
    # state and trying a different direction, it's like we moved right
    # and THEN AFTER THAT immediately moved left, and then moved up.
    # *************************NOTE**************************************
    if _dir == "right":
        if zero_col < 2:
          print("Moving right")
          print("Starting state:")
          print(currState)
          newState = swapTiles(currState, (zero_row, zero_col), _dir)
          result.append(newState)
          print("Ending state:")
          print(newState)
          print()
    elif _dir == "left":
        if zero_col > 0:
          print("Moving left")
          print("Starting state:")
          print(currState)
          newState = swapTiles(currState, (zero_row, zero_col), _dir)
          result.append(newState)
          print("Ending state:")
          print(newState)
          print()
    elif _dir == "up":
        if zero_row > 0:
          print("Moving up")
          print("Starting state:")
          print(currState)
          newState = swapTiles(currState, (zero_row, zero_col), _dir)
          result.append(newState)
          print("Ending state:")
          print(newState)
          print()
    elif _dir == "down":
        if zero_row < 2:
          print("Moving down")
          print("Starting state:")
          print(currState)
          newState = swapTiles(currState, (zero_row, zero_col), _dir)
          result.append(newState)
          print("Ending state:")
          print(newState)
          print()

    return result


def reverse(st):
    return st[::-1]
    
# def head(lst):
#     return lst[0]

# def tail(lst):
#     return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst


def generateNewStates(currState):
    return (generateNew(currState,"right") + generateNew(currState,"up") + generateNew(currState,"left") + generateNew(currState,"down"))


solution = tilepuzzle([[2,8,3],[1,0,4],[7,6,5]],[[2,8,3],[1,4,0],[7,6,5]])
print("Solution:")
print(solution)