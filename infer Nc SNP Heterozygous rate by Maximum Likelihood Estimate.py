import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

μ=float(input("mean of Heterozygous rate:"))
σ=float(input("standard deviation of Heterozygous rate:"))
nc=int(input("Numbers of census pop size:"))
fig = plt.figure()


x = μ + σ * np.random.randn(nc)

def mle(x):
    u = np.mean(x)
    return u, np.sqrt(np.dot(x - u, (x - u).T) / x.shape[0])

print(mle(x))
plt.hist(x)
plt.show()
