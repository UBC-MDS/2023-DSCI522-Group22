import numpy as np
import pandas as pd
import pytest
import os
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.helper_func_model_selection import model_selection
from src.helper_func_wine_classification_plot import create_wine_prediction_chart 

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

# Test with valid input
def test_valid_input():
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', 'white')
    assert chart is not None  # basic check to ensure a chart is returned

# Test default red wine color
def test_empty_red_wine_color():
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, '', 'white')
    # Check if chart uses the default color for red wine 
    chart_dict = chart.to_dict()
    color_scale_range = chart_dict['encoding']['color']['scale']['range']
    assert 'red' in color_scale_range, "Default white wine color is not set to 'red'"

# Test with invalid dataframe input
def test_invalid_dataframe_input():
    with pytest.raises(ValueError):
        create_wine_prediction_chart(None, 'red', 'white')  # None is not a valid DataFrame

# Test with empty white wine color
def test_empty_white_wine_color():
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', '')  # empty string for white wine color
    chart_dict = chart.to_dict()
    color_scale_range = chart_dict['encoding']['color']['scale']['range']
    assert 'peachpuff' in color_scale_range, "Default white wine color is not set to 'peachpuff'"

# Function to test if the output chart is a bar chart
def test_output_is_bar_chart():
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', 'white')
    
    # Check if the mark type of the chart is 'bar'
    assert chart.mark == 'bar', "The chart is not a bar chart"