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

from src.model_selection import model_selection
from src.wine_classification_plot import create_wine_prediction_chart 

def test_single_model():
    """
    Test function for single model selection.
    
    Asserts the creation of a single model and its type using 'model_selection' function.
    """
    # Test with a single model
    models = model_selection("dummy")
    assert len(models) == 1
    assert isinstance(models['Dummy Classifier'], DummyClassifier)

def test_multiple_models():
    """
    Test function for multiple model selection.
    
    Asserts the creation of multiple models and their types using 'model_selection' function.
    """
    # Test with multiple models
    models = model_selection("dtree", "knn", "svm")
    assert len(models) == 3
    assert isinstance(models['Decision Tree'], DecisionTreeClassifier)
    assert isinstance(models['KNN'], KNeighborsClassifier)
    assert isinstance(models['RBF SVM'], SVC)

def test_multiple_models_with_extra_input():
    """
    Test function for multiple model selection with invalid inputs.
    
    Asserts the creation of multiple models while handling invalid inputs using 'model_selection' function.
    """
    # Test with multiple models with invalid inputs
    # Invalid inputs here are "a" and 1
    models = model_selection("dtree", "knn", "svm", "a", 1)
    assert len(models) == 3
    assert isinstance(models['Decision Tree'], DecisionTreeClassifier)
    assert isinstance(models['KNN'], KNeighborsClassifier)
    assert isinstance(models['RBF SVM'], SVC)

def test_no_models():
    """
    Test function with no models.
    
    Asserts the behavior of 'model_selection' function when no models are provided.
    """
    # Test with no models (should return empty dictionary)
    models = model_selection()
    assert models == {}

def test_all_models():
    """
    Test function for all available models.
    
    Asserts the creation of all available models using 'model_selection' function.
    """
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
    """
    Test function for valid input data for chart creation.
    
    Asserts the creation of a wine prediction chart using valid input data.
    """
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', 'white')
    assert chart is not None  # basic check to ensure a chart is returned

# Test default red wine color
def test_empty_red_wine_color():
    """
    Test function for the default red wine color in chart creation.
    
    Asserts the default color setting for red wine in the created chart.
    """
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, '', 'white')
    # Check if chart uses the default color for red wine 
    chart_dict = chart.to_dict()
    color_scale_range = chart_dict['encoding']['color']['scale']['range']
    assert 'red' in color_scale_range, "Default white wine color is not set to 'red'"

# Test with invalid dataframe input
def test_invalid_dataframe_input():
    """
    Test function for invalid DataFrame input in chart creation.
    
    Asserts the handling of invalid DataFrame input in 'create_wine_prediction_chart' function.
    """
    with pytest.raises(ValueError):
        create_wine_prediction_chart(None, 'red', 'white')  # None is not a valid DataFrame

# Test with empty white wine color
def test_empty_white_wine_color():
    """
    Test function for empty white wine color in chart creation.
    
    Asserts the default color setting for white wine in the created chart.
    """
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', '')  # empty string for white wine color
    chart_dict = chart.to_dict()
    color_scale_range = chart_dict['encoding']['color']['scale']['range']
    assert 'peachpuff' in color_scale_range, "Default white wine color is not set to 'peachpuff'"

# Function to test if the output chart is a bar chart
def test_output_is_bar_chart():
    """
    Test function to check if the output chart is a bar chart.
    
    Asserts that the created chart is of type 'bar' using 'create_wine_prediction_chart' function.
    """
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', 'white')
    
    # Check if the mark type of the chart is 'bar'
    assert chart.mark == 'bar', "The chart is not a bar chart"