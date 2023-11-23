import pandas as pd
import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression, RidgeClassifier

def model_selection(*abbreviations):
    """
    Constructs a dictionary of machine learning models based on the provided abbreviations.

    This function takes any number of string arguments representing abbreviations for specific machine learning models. It returns a dictionary mapping the full model name to its corresponding initialized model object from scikit-learn. The function supports a predefined set of models, each identified by a unique abbreviation.

    Supported Model Abbreviations:
    - 'dummy': Dummy Classifier
    - 'dtree': Decision Tree Classifier
    - 'knn': K-Nearest Neighbors Classifier
    - 'svm': Support Vector Classifier (RBF Kernel)
    - 'nb': Naive Bayes Classifier (Bernoulli)
    - 'lr': Logistic Regression
    - 'lc': Ridge Regression

    Parameters:
    - *abbreviations (str): Variable number of string arguments representing model abbreviations.

    Returns:
    - dict: A dictionary where keys are full model names and values are the initialized model objects.

    Example Usage:
    >>> models_dict = model_selection("dummy", "dtree", "knn")
    >>> print(models_dict)
    {'Dummy Classifier': DummyClassifier(random_state=123),
     'Decision Tree': DecisionTreeClassifier(random_state=123),
     'KNN': KNeighborsClassifier()}

    >>> models_dict = model_selection("svm", "nb")
    >>> print(models_dict)
    {'RBF SVM': SVC(random_state=123), 'Naive Bayes': BernoulliNB()}
    """
    
    # Mapping of abbreviations to model constructors
    model_mapping = {
        "dummy": DummyClassifier(random_state=123),
        "dtree": DecisionTreeClassifier(random_state=123),
        "knn": KNeighborsClassifier(),
        "svm": SVC(random_state=123),
        "nb": BernoulliNB(),
        "lr": LogisticRegression(max_iter=1000),
        "lc": RidgeClassifier()
    }

    # Building the dictionary of models based on provided abbreviations
    models = { 
        "dummy": "Dummy Classifier",
        "dtree": "Decision Tree",
        "knn": "KNN",
        "svm": "RBF SVM",
        "nb": "Naive Bayes",
        "lr": "Logistic Regression",
        "lc": "Ridge"
    }
    selected_models = {models[abbr]: model_mapping[abbr] for abbr in abbreviations if abbr in model_mapping}
    
    return selected_models