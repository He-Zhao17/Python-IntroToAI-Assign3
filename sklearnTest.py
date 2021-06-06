import dt
import sklearn as sk

from sklearn import tree
from sklearn.datasets import load_breast_cancer

from sklearn import model_selection
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression



cancer = load_breast_cancer()
print("len: ", len(cancer), '\n')
print('data: ', cancer.data, sep = '\n')
print('index: ', cancer.target, sep = '\n')
print('abrr: ', cancer.feature_names, sep = '\n')



cancerT = tree.DecisionTreeClassifier(criterion = 'gini')
cancerT = cancerT.fit(cancer.data, cancer.target)
t1 = LinearRegression()
scores = cross_val_score(t1, cancer.data, cancer.target, cv=5)
print('\nresult with gini:', scores.mean())

cancerT = tree.DecisionTreeClassifier(criterion = 'entropy')
cancerT = cancerT.fit(cancer.data, cancer.target)
t1 = LinearRegression()
scores = cross_val_score(t1, cancer.data, cancer.target, cv=5)
print('\nresult with entropy:', scores.mean())