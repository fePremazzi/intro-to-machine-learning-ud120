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

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score as acc

t0 = time()
print 'Fitting features: '
clf = SVC(C = 10000, gamma = 'auto', kernel = 'rbf')
clf.fit(features_train,labels_train)
print 'End of fitting in ', round(time()-t0,3), ' s'

t1 = time()
print 'Start predcting'
pred = clf.predict(features_test)
print 'End of predcting in ', round(time()-t1,3), ' s'

#print pred

print 'Accuracy:'
print acc(y_true = labels_test,y_pred = pred)

print 'Prediction for lesson:'
print '10 = ',pred[10]
print '26 = ',pred[26]
print '50 = ',pred[50]

Eu, osvaldo de rg tal e cpf tal, atesto que nao foi emitido o holerite referente ao mesm de oututbro, pois, a empresa onde trabalho AFA Plasticos de cnpj tal econtra-se em 
recuperação judicial.No entenato, o salario bruto referente ao mes de outubro foi credito normalmente no valor de XYZ.