# 循环次数限制
luck_num = 19
input_num = -1



# 1.while循环
# guess_num = 0
# while luck_num!=input_num and guess_num < 3:
#     input_num = int(input("Input the guess num:"))
#     if input_num > luck_num:
#         print("the real number is smaller.")
#     elif input_num < luck_num:
#         print("this real num is bigger..")
#     guess_num +=1
# print("bingo!")


# 2.for循环
for i in range(3):
    input_num = int(input("Input the guess num:"))
    if input_num > luck_num:
        print("the real number is smaller.")
    elif input_num < luck_num:
        print("this real num is bigger..")
    else:
        print("Bingo!")
        break
else:
    print("Too many retrys!")











