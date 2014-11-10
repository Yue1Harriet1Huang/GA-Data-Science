#Lab: Matrices in Python

#1. vectorMatrix multiplication funtion

def vectorMatrixMultiplication(matrix,vector):
	mvResult = [0]*len(matrix)
	for i in range(len(matrix)):
		for j in range(len(vector)):
			mvResult[j] += matrix[i][j] * vector[j]
	print '\n', "Matrix x Vector:"
	print mvResult

matrix = [ [1,2,3],
		   [4,5,6],
		   [7,8,9] ]

vector = [1,2,3]

vectorMatrixMultiplication(matrix,vector)

#2. matrixMultiplication function

def matrixMultiplication(matrix1,matrix2):
	mmResult = [[0 for col in range(len(matrix2[0]))] for row in range(len(matrix1))]
	for i in range(len(matrix1)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix2)):
				mmResult[i][j] += matrix1[i][k] * matrix2[k][j]
	print '\n', "Matrix1 x Matrix2:"
	for r in mmResult:
		print(r)

matrix1 = [ [1,2,3],
			[4,5,6],
			[7,8,9] ]

matrix2 = [ [1,2,1,2],
			[3,4,3,4],
			[5,6,5,6] ]

matrixMultiplication(matrix1,matrix2)