# 编写登录接口
#     输入用户名密码
#     认证成功后显示欢迎信息
#     输错三次后锁定

# 思路:
#     一共需要两个文件：
#         黑名单的文件：黑名单里检测,不让登录
#         用户信息文件

import sys

account_file = 'D:\match.txt'
locked_file = 'D:\locked.txt'

def deny_account(username):
    print("您的用户已被锁定!")
    with file(locked_file,'a') as deny_f:
        deny_f.write('\n'+username)

def main():
    retry_count = 0
    retry_limit = 3
    while retry_count<retry_limit:
        username = input('\033[32;lm请输入用户名:\033[0m')
        with file(locked_file,'r') as lock_f:
            #方式一
            # for line in lock_f.readlines():
            #     if len(line)==0:
            #         continue
            #     if username == line.strip():
            #         sys.exit('\033[32:lm用户 %s 已经被锁定!\033[0m' % username)
            #方式二
            lines = []
            for line in lock_f.readlines():
                lines.append(line.strip())
            if username in lines:
                sys.exit('\033[32:lm用户 %s 已经被锁定!\033[0m' % username)
        if len(username)==0:
            print('用户名不能为空，请重新输入')
            continue

        password = input('\033[32;lm请输入密码:\033[0m')
        with file(account_file,'r') as account_f:
            flag = False
            for line in account_f.readlines():
                user,pawd = line.strip().split()
                if username == user and password == pawd:
                    print("success!")
                    print("欢迎 %s 来到后台登录系统" %username)
                    flag=True
                    break
        if flag == False:
            if retry_count<2:
                print("您的用户名或密码有误，请重新输入!")
            retry_count +=1
