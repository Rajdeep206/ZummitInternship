import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[77,92,14,52,58,29,33,60,12,27]
plt.subplot(2,2,1)
plt.scatter(x,y)
plt.subplot(2,2,2)
plt.bar(x,y)
plt.subplot(2,2,3)
plt.pie(y,labels=x)
plt.show()