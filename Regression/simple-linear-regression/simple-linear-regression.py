import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('dataset.txt', delimiter=',')

print(data)

X = data[:, 0].reshape(-1, 1)
ones = np.ones([X.shape[0], 1])
X = np.concatenate((ones, X), axis=1)
print(X.shape)
# Shape of X is (data(rows), 2)

y = data[:,1].reshape(-1, 1)
print(y.shape)
# Shape of y is (data(rows), 1)

# plots column 0(input) along column 2(output)
plt.scatter(data[:, 0].reshape(-1,1), y)
plt.show()

# Hyper-Parameters
alpha = 0.0001 # learning rate
iters = 1000 # number of iterations or Epochs

theta = np.zeros([1,2]) # row vector


def computeCost(X, y, theta):
    temp = np.power(((X @ theta.T) - y), 2) # @ means matrix multiplication and .T means transpose
    return np.sum(temp) / (2 * len(X))

def gradientDescent(X, y, theta, alpha, iters):
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum((X @ theta.T - y) * X, axis=0)
        cost = computeCost(X, y, theta)
    return (theta, cost)

new_theta, cost = gradientDescent(X, y, theta, alpha, iters)  

print('Final Theta Values: ',new_theta)
print('Final Cost: ',cost)

plt.scatter(data[:, 0].reshape(-1,1), y)
axes = plt.gca()
x_vals = np.array(axes.get_xlim()) 
y_vals = new_theta[0][0] + new_theta[0][1]* x_vals #the line equation
plt.plot(x_vals, y_vals, '--')
plt.show()

