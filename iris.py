import numpy as np
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
result = KMeans(3).fit(X)
fuck = result.predict(X)
center = result.cluster_centers_

print(fuck)


