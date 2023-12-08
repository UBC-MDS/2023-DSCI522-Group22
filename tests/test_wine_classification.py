import numpy as np
import pandas as pd
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.wine_classification_plot import create_wine_prediction_chart 


def test_valid_input():
    """
    Test function to validate valid input for chart creation.
    
    Asserts the creation of a wine prediction chart using valid input data.
    """
    data = {'Feature Name': ['Sugar', 'Alcohol'], 'Coefficient': [0.5, -0.3]}
    df = pd.DataFrame(data)
    chart = create_wine_prediction_chart(df, 'red', 'white')
    assert chart is not None  # basic check to ensure a chart is returned

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

def test_invalid_dataframe_input():
    """
    Test function for invalid DataFrame input in chart creation.
    
    Asserts the handling of invalid DataFrame input in 'create_wine_prediction_chart' function.
    """
    with pytest.raises(ValueError):
        create_wine_prediction_chart(None, 'red', 'white')  # None is not a valid DataFrame

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
