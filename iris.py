import numpy as np
import pandas as pd
from collections import Counter
import sklearn
import matplotlib
def bidaxiao():
    if a > (b | c):
        return a
    elif b > c:
        return b
    else:
        return c
f = open("iris.data")
X=[]

Y_labele = []
lables = ["Iris-virginica","Iris-versicolor","Iris-setosa"]
for i in f:
    Y_labele.append(i.split(",")[4].replace("\n",""))
    X.append([float(i.split(",")[0].replace("'","")),float(i.split(",")[1].replace("'","")),float(i.split(",")[2].replace("'","")),float(i.split(",")[3].replace("'",""))])
X = np.array(X)
f.close()


'''num = np.random.randint(1, 151, 20)
a = X[num]
del X[num]

print(X)'''

from sklearn.cluster import KMeans
result = KMeans(3).fit_predict(X)
print(result)
a1 = result[0:50]
b1 = result[50:100]
c1 = result[100:150]
print('Counter(a1)\n',Counter(a1))
print('Counter(b1)\n',Counter(b1))
print('Counter(c1)\n',Counter(c1))

a = Counter(a1)[0]
b = Counter(a1)[1]
c = Counter(a1)[2]
sum = bidaxiao()

a = Counter(b1)[0]
b = Counter(b1)[1]
c = Counter(b1)[2]

sum += bidaxiao()

a = Counter(c1)[0]
b = Counter(c1)[1]
c = Counter(c1)[2]

sum += bidaxiao()

print('正确率为',round((sum/150)*100,2),'%')





'''df = pd.crosstab(result, Y_labele)
print(df)
L = []
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if i != j:
            L.append(df.iloc[i, j])




print(L)
print("预测准确率为：", round((150 - sum(L)) / 150 * 100, 1), "%")'''

''' fuck = result.predict([np.array([5,3,1,0.5])])
center = result.cluster_centers_

print(fuck)
print(center)'''



