import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
def fun (theta0,theta,x):
    return theta0+theta1*x;


def gradient_descent(x, y, theta, alpha, num_iters):

    theta0=0
    theta1=0
    M=float(len(x))
    for i in range(0,num_iters):
        th1=theta1;
        th0=theta0
        theta0= th0 -alpha *(1/M)*((( th1* x) + th0)-y).sum()
        theta1= th1 -alpha * (1/M)*(x*((th1 * x) + th0)-y).sum()
    return theta0,theta1


#Load the dataset
data = pandas.read_csv('data.csv')

scatter_matrix(data[['population','profit']])
plt.show()

X = data['population']
y = data['profit']
#number of training samples
m = y.size
#Initialize theta parameters
theta0 = 0
theta1 =0
#Some gradient descent settings
iterations = 1500
alpha = 0.01
#compute and display initial cost
theta= gradient_descent(X, y, [theta0,theta1], alpha, iterations) #To be completed by students
print theta
print(fun(theta[0],theta[1],3.9))

#Predict values for population sizes of 3.5 and 7.0
#Students write prediction code
