import numpy as np
import pandas as pd
import pytest
import sys
import os
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.helper_func_model_selection import model_selection

def test_single_model():
    # Test with a single model
    models = model_selection("dummy")
    assert len(models) == 1
    assert isinstance(models['Dummy Classifier'], DummyClassifier)

def test_multiple_models():
    # Test with multiple models
    models = model_selection("dtree", "knn", "svm")
    assert len(models) == 3
    assert isinstance(models['Decision Tree'], DecisionTreeClassifier)
    assert isinstance(models['KNN'], KNeighborsClassifier)
    assert isinstance(models['RBF SVM'], SVC)

def test_multiple_models_with_extra_input():
    # Test with multiple models with invalid inputs
    # Invalid inputs here are "a" and 1
    models = model_selection("dtree", "knn", "svm", "a", 1)
    assert len(models) == 3
    assert isinstance(models['Decision Tree'], DecisionTreeClassifier)
    assert isinstance(models['KNN'], KNeighborsClassifier)
    assert isinstance(models['RBF SVM'], SVC)

def test_no_models():
    # Test with no models (should return empty dictionary)
    models = model_selection()
    assert models == {}

def test_all_models():
    # Test with all models
    models = model_selection("dummy", "dtree", "knn", "svm", "nb", "lr", "lc")
    assert len(models) == 7
    assert isinstance(models['Dummy Classifier'], DummyClassifier)
    assert isinstance(models['Decision Tree'], DecisionTreeClassifier)
    assert isinstance(models['KNN'], KNeighborsClassifier)
    assert isinstance(models['RBF SVM'], SVC)
    assert isinstance(models['Naive Bayes'], BernoulliNB)
    assert isinstance(models['Logistic Regression'], LogisticRegression)
    assert isinstance(models['Ridge'], Ridge)
