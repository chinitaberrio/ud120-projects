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




#########################################################
### your code goes here ###

#########################################################

from sklearn import svm

#to speed up the training
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]


clf = svm.SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train,labels_train) #features and labels
print ("training time:", round(time()-t0, 3), "s")
pre = clf.predict(features_test)  
print (pre[10], pre[26], pre[50])
print (sum(pre))
accuracy = clf.score(features_test,labels_test)
print (accuracy)
