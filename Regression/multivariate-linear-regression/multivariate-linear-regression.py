import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

# Importing data from the dataset
data = pd.read_csv('dataset.txt', names=['house_size','no_of_bedrooms','price'])

print('\nOriginal Data\n', data)
# Prints data, as we see the data varies alot, we should normalize it to
# have all values below 1

# Normalizes across columns
data = (data - data.mean())/data.std()

print('\n\nNormalized Data\n', data)

# X - Input
# Y - output

X = data.iloc[:,0:2] # copies column 0 and 1 to X
ones = np.ones([X.shape[0],1]) # genrates a matrix of 1's of size ( data(rows), 1 )
X = np.concatenate((ones, X), axis=1) # concatenates ones and X along the column
print(X.shape)
# new size of X is ( data(rows), 3)

y = data.iloc[:,2:3].values # copies column 2 to Y , .values converts panda to numpy
print(y.shape)
# Size of y is ( data(rows), 1)

theta = np.zeros([1,3])
print(theta.shape)

# Hyper-parameters
alpha = 0.01 # learning rate
iters = 1000 # number of iterations/Epochs

# Cost Function
def computeCost(X, y, theta):
	# root mean square of terms
	temp = np.power(((X @ theta.T)-y),2)

	# @ means matrix multiplication and .T means transpose of a matrix
	return np.sum(temp)/(2 * len(X))
	# 1/2m of the summation

def gradientDescent(X, y, theta, iters, alpha):
	cost = np.zeros(iters)
	for i in range(iters):
		theta = theta - (alpha/len(X)) * np.sum(X * (X @ theta.T - y), axis=0)
		cost[i] = computeCost(X, y, theta)

	return theta, cost

new_theta, cost = gradientDescent(X, y, theta, iters, alpha)
print('\nFinal Theta Values: ',new_theta)

# computes cost using values of theta after gradient descent
finalCost = computeCost(X, y, new_theta)
print('\nFinal Cost: ', finalCost)

# Plotting
fig, ax = plt.subplots()  
ax.plot(np.arange(iters), cost, 'r')  
ax.set_xlabel('Iterations')  
ax.set_ylabel('Cost')  
ax.set_title('Error vs. Training Epoch')
plt.show()  