# 杨辉三角
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1

L = [[1],[1,1],[1,2,1],[1,3,3,1]]

def triangles():
	L = []
	n = 1
	while n<3:
		L.append([ i for i in range(1,n+1)])
		n = n + 1
	return L

for t in triangles():
	print(t)







# def fib(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		yield b
# 		a, b = b,a+b
# 		n = n+1
# 	return 'done'
# f = fib(6)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))











