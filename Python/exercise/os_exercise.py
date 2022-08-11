import os

# 分割符
os.sep
# 工作平台
os.name
# 当前路径
dir = os.getcwd()
# 拼接路径
# new_dir = os.path.join(dir, 'test')
# new_dir2 = os.path.join(dir, 'test1', 'test2')
# 列出目录
# os.listdir(dir)
# 创建目录
# os.mkdir(new_dir)
# os.makedirs(new_dir2)
# 删除目录
# os.rmdir(new_dir)
# os.removedirs(new_dir2)
# 重命名目录
# os.rename(new_dir, os.path.join(dir, 'test2)
# 检查路径是否存在
# os.path.exists(new_dir)
# 是否是目录
# os.path.isdir(new_dir)
# 是否是文件
# os.path.isfile(os.path.join(new_dir, 'test.txt'))
# 文件名或目录名
# os.path.basename(os.path.join(new_dir, 'test.txt'))
# 父目录
# os.path.dirname(os.path.join(new_dir, 'test.txt'))
# 绝对路径
# os.path.abspath(os.path.join(new_dir, 'test.txt'))

# &&串行
# &并行
# os.system('ls && cd test && ls')
# os.system('ls & cd test && ls')
# os.system('ls && cd test & ls')
# os.system('python test_MLP.py')