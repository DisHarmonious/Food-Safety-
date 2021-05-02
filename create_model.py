import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.utils import shuffle
import pickle

#read dataset
data=pd.read_csv("ready_for_ml.txt")

#shuffle
data = shuffle(data)

#get x and y
X=data.iloc[:,1:]
y=data.iloc[:,0]

#train
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

#predict
predictions=clf.predict(X)

#find accuracy
accuracy=accuracy_score(y, predictions)
print('accuracy: ', 100*accuracy, "%")

#store model
pickle.dump(clf, open('final_model.sav', 'wb'))

#load stored model
#stored_model = pickle.load(open('C:/Users/Euelpis/Desktop/agroknow/final_model.sav', 'rb'))









