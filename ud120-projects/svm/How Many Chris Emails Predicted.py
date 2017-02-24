#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
from sklearn.svm import SVC

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
#C = [10.0,100.0,1000.0,10000.0]
#accuracy = list(tuple())
#for c in C:
clf = SVC(kernel="rbf",C=10000.0)
#########################################################

to = time()
clf.fit(features_train,labels_train)
print "learn",round(time()-to,3),"s"
#### store your predictions in a list named pred
#features_test = features_test[:len(features_test)/100]
t1 = time()

pred = clf.predict(features_test)
print "predict",round(time()-t1,3),"s"

print len(pred),len(labels_test)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc
chris = 0
for i in pred:
	if i==1:
		chris+=1
print chris
#########################################################


