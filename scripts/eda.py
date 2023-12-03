import click
import os
import sys
import altair as alt
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.layered_distri_plot import layered_distri_plot
from src.helper_func_eda_visualization import create_numeric_hist_plots
from src.cor_matrix_plot import cor_matrix_plot

@click.command()
@click.option('--train-data', type=str, help="Path to read in training data CSV file")
@click.option('--plot-path', type=str, help="Path to directory where the plot will be written to")

def main(train_data, plot_path):

    # Ensure that the plot_path directory exists
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)

    # Read the training data CSV file
    wine_train = pd.read_csv(train_data, index_col='Unnamed: 0')

    layerd_distribution_plot = layered_distri_plot(wine_train)
    layerd_distribution_plot.save(os.path.join(
        plot_path, "comparative_distribution.png"),
              scale_factor=2.0)

    numeric_cols = wine_train.columns.tolist()[:-2]
    histogram_plot = create_numeric_hist_plots(wine_train, numeric_cols)
    histogram_plot.save(os.path.join(
        plot_path, "numeric_histogram.png"),
              scale_factor=2.0)
    
    corr_data = wine_train[numeric_cols].corr(
    'spearman'
    ).corr().stack().reset_index()
    corr_data['correlation_text'] = corr_data[0].map('{:.2f}'.format) 
    corr_data = corr_data.rename(columns={0: 'correlation'})
    corr_matrix = cor_matrix_plot(corr_data)
    corr_matrix.save(os.path.join(
        plot_path, "correlation_matrix_heatmap.png"),
              scale_factor=2.0)
    
if __name__ == '__main__':
    main()