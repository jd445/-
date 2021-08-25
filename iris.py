import numpy as np
import sklearn
import matplotlib
f = open("iris.data")
X=[]
for i in f:
    X.append([float(i.split(",")[0].replace("'","")),float(i.split(",")[1].replace("'","")),float(i.split(",")[2].replace("'","")),float(i.split(",")[3].replace("'",""))])
X = np.array(X)
f.close()
print(X)

nice = sklearn.cluster.KMeans(3).fit(X)
