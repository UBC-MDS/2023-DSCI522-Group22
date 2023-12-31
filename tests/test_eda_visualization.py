import pytest
import pandas as pd
import sys
import os
import altair as alt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.eda_visualization import create_distribution_detail_plot, create_numeric_hist_plots

def test_create_distribution_detail_plot():
    """
    Test function to validate the creation of a distribution detail plot.
    
    Creates a sample DataFrame and tests the function `create_distribution_detail_plot`.
    - Checks if the result returned is an Altair RepeatChart.
    """
    # Create a sample DataFrame
    sample_data = pd.DataFrame({
        'color': ['red', 'white'],
        'feature1': [1, 2],
        'feature2': [3, 4]
    })
    numeric_cols = ['feature1', 'feature2']

    # Test function
    result = create_distribution_detail_plot(sample_data, numeric_cols)
    assert str(type(result)) == "<class 'altair.vegalite.v5.api.RepeatChart'>"

def test_create_numeric_hist_plots():
    """
    Test function to validate the creation of numeric histogram plots.
    
    Creates a sample DataFrame and tests the function `create_numeric_hist_plots`.
    - Checks if the result returned is an Altair RepeatChart.
    """
    # Create a sample DataFrame
    sample_data = pd.DataFrame({
        'color': ['red', 'white'],
        'feature1': [1, 2],
        'feature2': [3, 4]
    })
    numeric_cols = ['feature1', 'feature2']

    # Test function
    result = create_numeric_hist_plots(sample_data, numeric_cols)
    assert str(type(result)) == "<class 'altair.vegalite.v5.api.RepeatChart'>"