import numpy as np

"""
=======================================
结构
=======================================
"""
a = np.array([1,2,3], dtype='complex')
a = np.arange(6).reshape(2,3)
# 形状
a.shape
# 维数
a.ndim
# 数目
a.size
# 每个元素的字节
a.itemsize
# 迭代器
for x in np.nditer(a):
    x
# 一维切片
a = np.arange(10)
a[:5]
a[:-2]
a[::2]
a[::-1]
# 二维切片
a = np.array([[1,2,3],[4,5,6]])
a[:,:2]
# 索引
a = np.array([[1,2],[3,4],[5,6]])
rows = [0,1,2]
cols = [0,1,0]
a[rows,cols]
rows = [[0,0],[1,2]]
cols = [[0,1],[1,0]]
a[rows,cols]
# 布尔索引
a = np.arange(6)
print(a[a>=4])
# 合并
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.vstack([a,b])
np.hstack([a,b])
# 拆分
a = np.arange(6)
np.split(a, 3)
# 扁平化
a = np.array([[1,2,3],[4,5,6]])
a.flatten()


"""
=======================================
常用操作
=======================================
"""
# 算术运算
a = np.array([1,2,3])
b = np.array([4,5,6])
a+b
a-b
a*b
a/b
a%b
a**b
# 舍入
a = np.array([0.3, 0.5, 0.8])
np.floor(a)
np.ceil(a)
np.around(a)
# 排序
a = np.array([3,2,5,1,4,6])
np.sort(a,kind='quicksort')
np.argsort(a)
# 统计函数
a = np.array([1,3,5,7,9])
np.min(a)
np.max(a)
np.argmin(a)
np.argmax(a)
# 中位数
np.median(a)
# 算术平均数
np.mean(a)
# 加权平均数
np.average(a, weights=[1,1,1,1,1])
# 标准差
np.std(a)
# 方差
np.var(a)
# 去除重复元素
np.unique(a)
# 元数计数
np.bincount(a)
# 离散化
np.digitize(2.3, np.arange(10))
# 三角函数
a = np.array([np.sqrt(3)/2, 1/2, 0])
np.rad2deg(np.arcsin(a))


"""
=======================================
常用数组
=======================================
"""
np.empty([2,2], dtype='int8')
np.zeros([2,2])
np.ones([2,2])
np.eye(3,4)
np.identity(3)
np.arange(0,10,2)
np.linspace(1,10,10)
np.logspace(0, 10, num=10, endpoint=False, base=2)


"""
=======================================
随机数
=======================================
"""
np.random.seed(2)
# 正态分布
a = np.random.normal(loc=170,scale=30,size=[100000])
# 泊松分布
a = np.random.poisson(lam=2.5,size=[1000000])
# 均匀分布
a = np.random.uniform(low=0.0, high=1.0, size=[10000])
# 随机抽样
a = np.random.choice(np.arange(5),size=[3],replace=False,p=np.ones([5])/5)
# 随机整数
a = np.random.randint(low=0, high=100, size=10)