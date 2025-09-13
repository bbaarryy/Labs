import matplotlib.pyplot as plt
import seaborn as sns

raw = [1,2,3,4,5,6,7,1,2,3,1,2,1]
x = [1,2,3,4,5,6,7,8,9]
y = [0,0,0,0,0,0,0,0,0]
for i in range(len(raw)):
    if(raw[i] != 0):
        y[raw[i]-1]+=1
sns.barplot(x=x, y=y)
plt.show()

