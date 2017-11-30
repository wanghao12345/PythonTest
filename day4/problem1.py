# Python编码

# 1.python内部执行过程
#
#     Python文件            Python核心(解释器)           运行环境
#
#     内置模块               -->词法分析                 对象和类型
#
#     类库                   -->语法分析                 内存管理
#
#     自定义模块             -->编译                     状态
#
#                            -->执行

# 2.解释器
#
#     在执行python文件的时候，使用命令执行index.py文件：
#         >>>python  index.py
#     这里明确指出index.py脚本文件由python解释器来执行。
#     如果想要类似shell脚本一样执行index.py,那么需要在index.py的头部指定解释器:
#     #!/usr/bin/env python

# 3.内容编码
#     python解释器在加载Python文件时,会对内容进行编码
#     python2:需要在python文件头部加上:
#             #-*-coding:utf-8 -*-
#     python3:已经默认转码了，不需要像python2一样需要在头部加转码

# 4.pyc文件
#     执行Python代码时，如果导入了其他的.py文件，那么，执行过程中会自动生成一个与其同名的.pyc文件,该文件就是Python解释器变异之后产生的字节码。
