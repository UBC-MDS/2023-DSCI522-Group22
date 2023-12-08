import pandas as pd
import numpy as np
import pytest
import sys
import os
import altair as alt

test_data = pd.read_csv("data/test/test_data_corr_heatmap.csv", index_col="Unnamed: 0")
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.cor_matrix_plot import cor_matrix_plot

test_graph = cor_matrix_plot(test_data)

def test_input_data():
    assert isinstance(test_data, pd.DataFrame), "The data input should be a dataframe"
    assert len(test_data) < 5000, "Dataframe should have less than 3000 entries"
    assert len(test_data.columns) == 4, "The input Data has wrong format, \
        should include 4 columns in total"
    assert list(test_data.columns) == ['level_0', 
                                       'level_1', 
                                       'correlation', 
                                       'correlation_text'], \
        "The input Data has wrong column names. They should be level_0,level_1m,\
            correlation, correlation_text"
    
def test_output_graph():
    assert isinstance(test_graph, alt.LayerChart), "The graph output should be an \
        altair layered chart"
    assert len(test_graph.layer) == 2, "The graph should have two layesrs"

