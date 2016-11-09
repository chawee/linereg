import numpy as np
import matplotlib.pyplot as pl
from sklearn import linear_model

n=100


x=np.arange(1,n+1,1,int)
t=np.arange(0,n+1,0.1)

#Adding Variability with normal distribution
mu, sigma = 0 , 5
var1=np.random.normal(mu,sigma,n)
var2=np.random.normal(mu,sigma,n)
x_1=x+var1
x_2=x+var2


#print ('x_2',len(x_2.reshape(-1,1)), x_2.shape())

#print (x_1.reshape(1,-1))

regr= linear_model.LinearRegression()
regr.fit(x_1.reshape(-1,1),x_2.reshape(-1,1))
print  np.shape(t)
print regr.coef_
fig=pl.figure(1)
ax=fig.add_subplot(111)
#ax.scatter(x_1,x_1, color='r')
predicted=[i[0] for i in regr.predict(t.reshape(-1,1))]

ax.scatter(x_1,x_2,color='cyan')
ax.plot(t, predicted,'k')
#ax.scatter(x_1,predicted,'y')
pl.show()



'''pl.scatter(x_1,x_2)
pl.title('Data Scattered using Normal Distribution')
pl.xlabel('X Axis')
pl.ylabel('Y Axis')
pl.show()'''
