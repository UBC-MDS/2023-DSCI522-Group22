import pandas as pd
import numpy as np
import pytest
import sys
import os
import altair as alt



test_data = pd.read_csv("data/test/test_data_alt_distri.csv", index_col="Unnamed: 0")

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.layered_distri_plot import layered_distri_plot

test_graph = layered_distri_plot(test_data)

def test_input_data():
    """
    Test function to validate input data.
    
    Asserts conditions about the structure and format of the input DataFrame `test_data`.
    - Should be a Pandas DataFrame.
    - Should have less than 5000 entries.
    - Should include a total of 13 columns.
    - Should contain exactly 12 numeric columns.
    - The last column should be named "color".
    """
    assert isinstance(test_data, pd.DataFrame), "The data input should be a dataframe"
    assert len(test_data) < 5000, "Dataframe should have less than 3000 entries"
    assert len(test_data.columns) == 13, "The input Data has wrong format, \
        should include 13 columns in total"
    assert len(test_data.select_dtypes(include=np.number).columns.tolist()) == 12,\
        "The input Data has wrong format, should have all 12 numeric  columns"
    assert test_data.columns[-1] == "color", "Wrong input, the last column \
        shoud be wine color"    
    
def test_output_structure():
    """
    Test function to validate output structure.
    
    Asserts conditions about the output graph `test_graph`.
    - Should be an Altair RepeatChart.
    """
    assert isinstance(test_graph, alt.RepeatChart), "The graph should be Altair repeat chart"
