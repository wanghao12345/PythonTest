# 杨辉三角
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1
#L = [[1],[1,1],[1,2,1],[1,3,3,1]]
# def triangles():
# 	L = []
# 	n = 1
# 	while n<3:
# 		L = [L[int(i)] for i in range(1,n+1)]
# 		print(L)
# 		n = n + 1
# 	return L

# for t in triangles():
# 	print(t)


# def fun1():
# 	sum = 0
# 	for x in range(1,5,1):
# 		for y in range(1,5,1):
# 			for z in range(1,5,1):
# 				if (x!=y & y!=z):
# 					sum = sum + 1;
# 					print(x,y,z)
# 	print(sum)
# fun1()



# def fun2():
# 	bonus1=100000*0.1
# 	bonus2=bonus1+100000*0.75
# 	bonus4=bonus2+200000*0.5
# 	bonus6=bonus4+200000*0.3
# 	bonus10=bonus6+400000*0.15
# 	mon = int(input("请输入月利润:\n"))
# 	if mon<=100000:
# 	    bonus=mon*0.1
# 	else:
# 	    if mon<=200000:
# 	        bonus=bonus1+(mon-100000)*0.075
# 	    else:
# 	        if mon <= 400000:
# 	            bonus = bonus2 + (mon - 200000) * 0.05
# 	        else:
# 	            if mon <= 600000:
# 	                bonus = bonus4 + (mon - 400000) * 0.03
# 	            else:
# 	                if mon <= 1000000:
# 	                    bonus = bonus6 + (mon - 600000) * 0.015
# 	                else:
# 	                    if mon > 1000000:
# 	                        bonus = bonus10 + (mon - 1000000) * 0.01
# 	print(bonus)
# 	return fun2()
# fun2()






























