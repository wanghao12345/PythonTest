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

# 当用户输入错误操作三次将用户的用户名添加进黑名单文件
def deny_account(username):
    print("您的用户已被锁定!")
    with open(locked_file,'a') as deny_f:
        deny_f.write('\n'+username)
# 主文件
def main():
    retry_count = 0 # 计数器
    retry_limit = 3 # 次数限制
    while retry_count<retry_limit: # 循环输入
        username = input('请输入用户名:')
        with open(locked_file,'r') as lock_f: # 先检测黑名单是否有用户名
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
                sys.exit('用户 %s 已经被锁定!' % username)
        if len(username)==0:
            print('用户名不能为空，请重新输入')
            continue

        password = input('请输入密码:')
        with open(account_file,'r') as account_f: # 在用户信息文件中检测密码
            flag = False
            for line in account_f.readlines():
                user,pawd = line.strip().split()
                if username == user and password == pawd:
                    print("success!")
                    print("欢迎 %s 来到后台登录系统" %username)
                    flag=True
                    break # 退出当前for循环
        if flag == False:
            if retry_count<2:
                print("您的用户名或密码有误，请重新输入!")
            retry_count +=1
        else:
            print("欢迎进入后台管理系统")
            break # 跳出while循环
    else:
        deny_account(username)
if __name__ == '__main__': # Python主文件的判断,入口处
    main()

