import pandas as pd
import numpy as np
import pytest
import sys
import os
import altair as alt



test_data = pd.read_csv("data/test/test_data_alt_distri.cvs", index_col="Unnamed: 0")

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.layered_distri_plot import layered_distri_plot

test_graph = layered_distri_plot(test_data)

def test_input_data():
    assert isinstance(test_data, pd.DataFrame), "The data input should be a dataframe"
    assert len(test_data) < 5000, "Dataframe should have less than 3000 entries"
    assert len(test_data.columns) == 13, "The input Data has wrong format, \
        should include 13 columns in total"
    assert len(test_data.select_dtypes(include=np.number).columns.tolist()) == 12,\
        "The input Data has wrong format, should have all 12 numeric  columns"
    assert test_data.columns[-1] == "color", "Wrong input, the last column \
        shoud be wine color"    
    
def test_output_structure():
    assert isinstance(test_graph, alt.RepeatChart), "The graph should be Altair repeat chart"
