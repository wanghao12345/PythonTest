# continue:跳出本次循环进行下一次循环
# break:跳出整个循环

for i in range(5):
    for j in range(10):
        if j < 5:
            continue
        if i > 3:
            break
        print(j)