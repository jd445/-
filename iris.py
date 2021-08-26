import numpy as np
import pandas as pd
import sklearn
import matplotlib
f = open("iris.data")
X=[]

Y_labele = []
lables = ["Iris-virginica","Iris-versicolor","Iris-setosa"]
for i in f:
    Y_labele.append(i.split(",")[4].replace("\n",""))
    X.append([float(i.split(",")[0].replace("'","")),float(i.split(",")[1].replace("'","")),float(i.split(",")[2].replace("'","")),float(i.split(",")[3].replace("'",""))])
X = np.array(X)
f.close()
from sklearn.cluster import KMeans
result = KMeans(3).fit_predict(X)
print(result)
df = pd.crosstab(result, Y_labele)
print(df)
L = []
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        if i != j:
            L.append(df.iloc[i, j])
print(L)
print("预测准确率为：", round((150 - sum(L)) / 150 * 100, 1), "%")


""" fuck = result.predict([np.array([5,3,1,0.5])])
center = result.cluster_centers_

print(fuck)
print(center) """



