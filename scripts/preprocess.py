# split_n_preprocess.py
# author: Chun Li
# date: 2023-12-01

import click
import os
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import make_column_transformer

@click.command()
@click.option('--data-to', type=str, help="Path to processed data storage folder", default='data/processed')
@click.option('--preprocessor-to', type=str, help="Path to directory housing the preprocessor object", default='results/models')

def main(data_to, preprocessor_to):

    """
    Preprocessing Script for Wine Dataset

    This script preprocesses the wine quality dataset, preparing it for machine learning model training. 
    It reads the training and testing data, applies a column transformer for data normalization and encoding, 
    and saves the preprocessed data along with the transformer object.

    The script uses the Click library to handle command-line arguments, allowing users to specify custom paths 
    for input data and output files.

    Usage:
        Run this script from the command line using Python. You can specify the paths for the data and where 
        to save the preprocessed files and the transformer. Example usage:

        python preprocess.py --data-to path/to/data --preprocessor-to path/to/preprocessor

    Arguments:
        --data-to: The path to the folder containing 'wine_train.csv' and 'wine_test.csv'. 
                Default is 'data/processed'.
        --preprocessor-to: The path to the directory where the preprocessor object ('wine_preprocessor.pickle') 
                        will be saved. Default is 'results/models'.

    Functionality:
        1. Reads 'wine_train.csv' and 'wine_test.csv' from the specified 'data-to' directory.
        2. Constructs a column transformer to process numeric and categorical features.
        3. Fits the transformer on the training data and applies it to both training and testing data.
        4. Saves the fitted column transformer as a pickle file named 'wine_preprocessor.pickle'.
        5. Outputs the transformed training and testing data as 'scaled_wine_train.csv' and 
        'scaled_wine_test.csv' in the specified 'data-to' directory.

    Output:
        - 'scaled_wine_train.csv': Preprocessed training data.
        - 'scaled_wine_test.csv': Preprocessed testing data.
        - 'wine_preprocessor.pickle': Pickled file of the fitted column transformer.

    Note:
        Ensure that all necessary Python packages are installed and the input data files are in the correct 
        format and located in the specified directory.

    Example:
    python preprocess.py --data-to ../data/processed --preprocessor-to ../results/models
    """
    wine_train = pd.read_csv(os.path.join(data_to, "wine_train.csv"))
    wine_test = pd.read_csv(os.path.join(data_to, "wine_test.csv"))

    numeric_features = wine_train.columns.tolist()[:-2]
    categorical_features = wine_train.columns.tolist()[-2:-1]
    columns_to_passthrough = ['color']

    wine_preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        (OrdinalEncoder(), categorical_features),
        ('passthrough', columns_to_passthrough)
    )

    wine_preprocessor.fit(wine_train)

    preprocessor_directory = os.path.join(preprocessor_to, "wine_preprocessor.pickle")
    os.makedirs(os.path.dirname(preprocessor_directory), exist_ok=True)
    pickle.dump(wine_preprocessor, open(preprocessor_directory, "wb"))

    # Transform the data
    scaled_wine_train_array = wine_preprocessor.transform(wine_train)
    scaled_wine_test_array = wine_preprocessor.transform(wine_test)

    # Convert the transformed arrays back to pandas DataFrames
    scaled_wine_train = pd.DataFrame(scaled_wine_train_array, columns=wine_train.columns)
    scaled_wine_test = pd.DataFrame(scaled_wine_test_array, columns=wine_test.columns)

    # Save the transformed data to CSV files
    scaled_wine_train.to_csv(os.path.join(data_to, "scaled_wine_train.csv"), index=False)
    scaled_wine_test.to_csv(os.path.join(data_to, "scaled_wine_test.csv"), index=False)

if __name__ == '__main__':
    main()
