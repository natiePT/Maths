import numpy as np
import sys

def generateurDeMatriceAleatoire(dimension=3,min=0,max=1):
	return np.random.randn(dimension,dimension) * (max - min +1) + min

def matInverse(A1,A=None,B=None,n=1):
	(X,Y) = A1.shape
	if X == Y :
		if (np.linalg.det(A1) == 0.) & (X == 2):
			print("e0")
		else :
			
			if n==1:
				q = np.trace(A1)	
				B = A1 - np.dot(q,np.identity(len(A1)))
			else:
				Bold = B

				A = np.dot(A1,Bold)
				q = np.trace(A)/n
				B = A - np.dot(q,np.identity(len(A)))
			
			print(q)
			if estNul(B):
				return (np.divide(Bold,q),q)
			else:	
				return matInverse(A1,A,B,n+1)
	else :
		print("e4")
		
	return None


def estNul(A):
	(X,Y) = A.shape
	for i in range(Y):
		for j in range(X):
			if A[i,j] != 0:
				return False
	return True

def fadeev(A):
	dim=len(A)
	I=np.eye(dim)
	An=A
	q=-np.trace(An)
	B = An + q*I
	P=[1]

	for n in range(2,dim+1):
		Bold = B
		An=np.dot(A,Bold)

		q=-np.trace(An)/n
		P.append(q)

		B = An + q*I

	return ( np.divide(Bold,-q) , q * (-1)**(dim), P )

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


#mat = generateurDeMatriceAleatoire(dimension = 30,min=-1000000000000000000000000,max=1000000000000000000000000)
#i = np.linalg.inv(mat)
#matInv,det,pol = fadeev(mat)
#print("Déterminant Numpy : ",np.linalg.det(mat)," Notre déterminant :",det)
#print("Correction : \n",i)
#print("Résultat : \n",matInv)



if len(sys.argv) == 3:

	mode = sys.argv[1]
	argMat = sys.argv[2]
	mat = np.matrix(argMat)

	matInv,det,pol = fadeev(mat)

	if mode == '1':
		print(matToString(str(matInv)))
	elif mode == '2':
		print(str(det))
	elif mode == '3':
		tmp = str(pol)
		a = tmp[1:-1]
		text = ""
		for i in range(len(a)):
			if a[i] == ',':
				text += ";"
			else:
				text += a[i]
		print(text)
	else:
		print("e1")

else:
	print("e2")
