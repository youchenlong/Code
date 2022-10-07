import numpy as np
# matplotlib
import matplotlib.pyplot as plt
def plot(x,y,*args):
    ax, title, xlabel, ylabel, label = args
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x,y,'.',label=label)
    ax.legend()
fig, axes = plt.subplots(3,2)
# 点线图
x = np.linspace(-np.pi, np.pi, 100)
axes[0,0].plot(x, np.sin(x), '.', color='red')
# 柱状图
x = np.arange(1,10)
# axes[0,1].bar(x, x, color='green', align='center')
axes[0,1].barh(x, x, color='green', align='center')
# 饼图
x = np.array([1,2,3])
axes[1,0].pie(x, explode=[0.1,0,0] , labels=['A', 'B', 'C'])
# 直方图
x = np.array([1,2,2,3,3,3])
axes[1,1].hist(x, color = 'yellow', align='left')
# 箱线图
x = np.array([1,2,3,4,5,6])
axes[2,0].boxplot(x)
# 散点图
x = np.array([1,2,3,4,5,6])
axes[2,1].scatter(x, x)
# 保存图片
# plt.savefig('test.png')
plt.show()