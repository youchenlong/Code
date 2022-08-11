import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def plot(x, y, *args):
    ax, title, xlabel, ylabel, legend = args
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(x[0]-0.05,x[-1]+0.05)
    ax.set_ylim(-0.05,1.05)
    ax.plot(x,y,'.')
    ax.legend([legend],loc='upper right')

fig, axes = plt.subplots(8,2)

# 伯努利分布
# print(stats.bernoulli.rvs(p=0.5,size=10))
x = np.arange(2)
plot(x,stats.bernoulli.pmf(k=x,p=0.8),axes[0,0],'bernoulli', 'k', 'p', 'pmf')
plot(x,stats.bernoulli.cdf(k=x,p=0.8),axes[0,1],'bernoulli', 'k', 'p', 'cdf')

# 二项分布
# print(stats.binom.rvs(n=10,p=0.5,size=10))
x = np.arange(20)
plot(x,stats.binom.pmf(k=x,n=10,p=0.5),axes[1,0],'binom', 'k', 'p', 'pmf')
plot(x,stats.binom.cdf(k=x,n=10,p=0.5),axes[1,1],'binom', 'k', 'p', 'cdf')

# 几何分布
# print(stats.geom.rvs(p=0.5,size=10))
x = np.arange(20)
plot(x,stats.geom.pmf(k=x,p=0.5),axes[2,0],'geom', 'k', 'p', 'pmf')
plot(x,stats.geom.cdf(k=x,p=0.5),axes[2,1],'geom', 'k', 'p', 'cdf')


# 超几何分布
# print(stats.hypergeom.rvs(M=10,n=4,N=6,size=10))
x = np.arange(20)
plot(x,stats.hypergeom.pmf(k=x,M=10,n=4,N=6),axes[3,0],'hypergeom', 'k', 'p', 'pmf')
plot(x,stats.hypergeom.cdf(k=x,M=10,n=4,N=6),axes[3,1],'hypergeom', 'k', 'p', 'cdf')

# 泊松分布
# print(stats.poisson.rvs(mu=5,size=10))
x = np.arange(20)
plot(x,stats.poisson.pmf(k=x,mu=5),axes[4,0],'poisson', 'k', 'p', 'pmf')
plot(x,stats.poisson.cdf(k=x,mu=5),axes[4,1],'poisson', 'k', 'p', 'cdf')

# 正态分布
# print(stats.norm.rvs(loc=0,scale=1,size=10))
x = np.linspace(-10, 10, num=100)
plot(x,stats.norm.pdf(x=x,loc=0,scale=1),axes[5,0],'norm', 'k', 'p', 'pdf')
plot(x,stats.norm.cdf(x=x,loc=0,scale=1),axes[5,1],'norm', 'k', 'p', 'cdf')

# 均匀分布
# print(stats.uniform.rvs(loc=0,scale=1,size=10))
x = np.linspace(0, 1, num=100)
plot(x,stats.uniform.pdf(x=x,loc=0,scale=1),axes[6,0],'uniform', 'k', 'p', 'pdf')
plot(x,stats.uniform.cdf(x=x,loc=0,scale=1),axes[6,1],'uniform', 'k', 'p', 'cdf')

# 指数分布
# print(stats.expon.rvs(scale=2,size=10))
x = np.linspace(0, 10, num=100)
plot(x,stats.expon.pdf(x=x,scale=2),axes[7,0],'expon', 'k', 'p', 'pdf')
plot(x,stats.expon.cdf(x=x,scale=2),axes[7,1],'expon', 'k', 'p', 'cdf')

plt.show()