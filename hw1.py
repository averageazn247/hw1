#     14
#    13 12
#   11 10 9
#  8  7  6  5
# 4  3  2  1  0
#


    
j='jump'
l='land'
 
totalmoves=[]
pegs=[]
for i in range(0,14):
    pegs.append(True)
    #print i
pegs.append(False)
#fills board with pieces   leave 14 open 
moves0= [ [j,1] ,[l, 2] , [ [j, 5] , [l , 9] ] ]
totalmoves.append(moves0)

moves1= [ [[j,2] ,[l,3]] , [ [j,6] , [l , 10]] ]
moves2= [ [[j,1] ,[l,0]] , [ [j,3] , [l , 4]]  , [ [j,6] ,[l,9]], [[j,7], [l,11]] ]
moves3 = [[j,2, l,1], [j,7, l,10]]
moves4 = [[j,3, l,2], [j,8, l,11]]


moves5 = [[j,6, l,7], [j,9,  l,12]]
moves6 = [[j,7, l,8], [j,10, l,13]]
moves7 = [[j,6, l,5], [j,10, l,12]]
moves8 = [[j,7, l,6], [j,11, l,13]]

moves9 =  [[j,5,  l,0],  [j,6,  l,2], [j,10, l,11], [j,12, l,14]]
moves10 = [[j,6,  l,1],  [j,7,  l,3]]
moves11 = [[j,7,  l,2],  [j,8,  l,4], [j,10, l,9],  [j,13, l,14]]

moves12 = [[j,9,  l,5], [j,10, l,7]]
moves13 = [[j,10, l,6], [j,11, l,8]]


moves14 = [[j,12, l,9], [j,13, l,11]]

totalmoves.append(moves1)
totalmoves.append(moves2)
totalmoves.append(moves3)
totalmoves.append(moves4)
totalmoves.append(moves5)
totalmoves.append(moves6)
totalmoves.append(moves7)
totalmoves.append(moves8)
totalmoves.append(moves9)
totalmoves.append(moves10)
totalmoves.append(moves11)
totalmoves.append(moves12)
totalmoves.append(moves13)
totalmoves.append(moves14)

def isvalid(start,end):
    #takes [][]
    s=start[0][1]
    e= end[0][1]
    if s & e==False:
        return True
    else :
        return False
     
    

print  isvalid(totalmoves[0][0],totalmoves[1][0])



