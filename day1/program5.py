# 循环控制

# luck_num = 19
# while True:
#     input_num = int(input("Input the guess num:"))
#     if input_num == luck_num:
#         print("bingo!")
#         break
#     elif input_num > luck_num:
#         print("the real number is smaller.")
#     else:
#         print("this real num is bigger..")

#优化
luck_num = 19
input_num = -1
while luck_num!=input_num:
    input_num = int(input("Input the guess num:"))
    if input_num > luck_num:
        print("the real number is smaller.")
    elif input_num < luck_num:
        print("this real num is bigger..")
print("bingo!")
