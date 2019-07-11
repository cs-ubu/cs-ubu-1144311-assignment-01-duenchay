def readm( fname = 'A.csv'):
    f= open ('A.csv','r')
    A=[]
    for line in f.readline():
        A.append( [ float(x) for x in line.strip().split(',')  ] )
    f.close()
    return A

# # 1. read mt A from 'A.csv'
# # import pandas as pd
# # A = pd.read_csv('A.csv')
# A= readm('A.csv')
# # 2. read mt b from'b.csv  
# # b = pd.read_csv('b.csv')
# b= readm('b.csv')

# # 3. find the result of c = A*b

def matmul(A,b):
    m,n = len[A],len(b[0])
    J =len(A[0]) #A ~ mxJ #b ~ Jxn
    if len(A[0]) ==len(b):
        C=[ [0]*n for i in range(m)]
        # A[0][0]*b[0][0] +A[0][1]*b[1][0] +A[0][2]*b[2][0]
        for r in range (m):
            for c in range(n):
                C[r][c] = sum([ A[c][j]*b[j][c] for j in range(J)])
           
        return C
    return[]
print(matmul(A,b))
  

# c = A*b
# 4.print C
# print(c)
C= matmul(A,b)
print('----')
for row in C:
    print(row)
print('----')
import numpy as numpy
D =np.dot(np.array(A),np.array(b))
print(D)