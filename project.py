import copy


def Grid(spot):
   print(spot[0],spot[1],spot[2])
   print(spot[3],spot[4],spot[5])
   print(spot[6],spot[7],spot[8])
   global nodeentries
   print('spot:', nodeentries)
   print('Depth:', len(spot[9:]))
   print('Moves:', spot[9:])
   print('........')
   nodeentries=nodeentries+1
def Goal(spot):
   if spot[:9]==goalstate:
       Grid(spot)
       return True
   if spot[:9] not in checked:
       Grid(spot)
       stack.append(spot)
       checked.append(spot[:9])
   return False


if True:
   initialstate = [1,4,2, 0,3,5, 6,7,8]
   goalstate = [0,1,2, 3,4,5, 6,7,8]
   goalreached = False
   nodeentries = 0
   checked = []
   stack = []
   stack.append(initialstate)
   checked.append(initialstate)
   Grid(initialstate)
   while (not goalreached and not len(stack)==0):
       currentspot = stack.pop(0)
       blankpoint = currentspot.index(0)
       if blankpoint!=0 and blankpoint!=1 and blankpoint!=2:
           upspot = copy.deepcopy(currentspot)
           upspot[blankpoint] = upspot[blankpoint-3]
           upspot[blankpoint-3] = 0
           upspot.append('up')
           goalreached = Goal(upspot)
       if blankpoint!=0 and blankpoint!=3 and blankpoint!=6 and goalreached==False:
           leftspot = copy.deepcopy(currentspot)
           leftspot[blankpoint] = leftspot[blankpoint-1]
           leftspot[blankpoint-1] = 0
           leftspot.append('left')
           goalreached = Goal(leftspot)
       if blankpoint!=6 and blankpoint!=7 and blankpoint!=8 and goalreached==False:
           downspot = copy.deepcopy(currentspot)
           downspot[blankpoint] = downspot[blankpoint+3]
           downspot[blankpoint+3] = 0
           downspot.append('down')
           goalreached = Goal(downspot)    
       if blankpoint!=2 and blankpoint!=5 and blankpoint!=8 and goalreached==False:
           rightspot = copy.deepcopy(currentspot)
           rightspot[blankpoint] = rightspot[blankpoint+1]
           rightspot[blankpoint+1] = 0
           rightspot.append('right')
           goalreached = Goal(rightspot)
print('We finally reached goal state')
