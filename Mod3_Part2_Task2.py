''' Дана матрица размера n на n, найдите в ней
максимальный элемент.'''

from random import randint
n=5
m=[[randint(0,100) for i in range(n)] for j in range(n)]
print (m)

for matrix in range(n):
	M=(max(max(m[x]) for x in range(n)))
print(M)