import numpy as np
import math
import matplotlib.pyplot as plt
import sys

def somme(A,B,maxk,x,y):
	somme = 0
	for k in range(maxk):
		somme += A[y,k]*B[k,x]
	return np.sum(somme)

def cholesky(A):
	(X,Y) = A.shape
	B = np.zeros(A.shape)
	C = np.diag(np.ones(X),0)
	B[:,[0]] = A[:,0]
	C[[0],:] = A[0,:]/B[0,0]
	for y in range(Y):
		for x in range(X):
			if y >= x & x > 0:			
				s = somme(B,C,y,x,y)
				B[y,x] = A[y,x] - s
			if 0 < y & y < x:			
				s = somme(B,C,x,x,y)
				C[y,x] = (1/B[y,y])*( A[y,x] - s)
	return np.matrix(B),np.matrix(C)

def matToString(mat):
	a = mat[2:-2]

	text = ""
	hello = 0
	for i in range(len(a)):
		if (a[i] == ']'):
			hello = 1
		elif (a[i] == '[') & hello == 1:
			hello = 0
			text += ';'
		elif hello == 0:
			if (str(a[i]) == " ") & ((str(a[(i+1)%len(a)]) != " ") | (i+1 >= len(a))):
				text += "_"
			elif (str(a[i]) != " "):
				text += a[i]
			
	return text

if len(sys.argv) == 3:

	mode = sys.argv[1]
	argMat = sys.argv[2]
	mat = np.matrix(argMat)

	matInf,matSup = cholesky(mat)

	if mode == '1':
		print(matToString(str(matInf)))
	elif mode =='2':
		print(matToString(str(matSup)))
	elif mode == '3':
		print(matToString(str(np.dot(matInf,matSup))))
	else:
		print("e1")
else:
	print("e2")