import os
import pandas as pd
from sklearn.model_selection import train_test_split
import click

@click.command()
@click.option('--raw-data-white', type=str, help="Path to processed training data white")
@click.option('--raw-data-red', type=str, help="Path to processed training data red")
@click.option('--processed-data', type=str, help="Path to directory to save processed data", default='../data/processed')
@click.option('--train-data', type=str, help="Path to directory where the train data will be written to", default='../data/processed')
@click.option('--test-data', type=str, help="Path to directory where the test data will be written to", default='../data/processed')
@click.option('--seed', type=int, default=522, help="Seed for random number generator to ensure reproducibility")

def main(raw_data_white, raw_data_red, processed_data, train_data, test_data, seed):

    """
    Data Wrangling Script for Wine Dataset

    This script processes raw wine quality data, handling separate datasets for white and red wines. It 
    merges these datasets, adds a color label, and splits the combined dataset into training and testing 
    sets in a reproducible manner using a specified random seed.

    The script uses the Click library for command-line argument handling, allowing specification of custom 
    paths for input and output data, as well as the seed for reproducibility.

    Usage:
        Execute this script from the command line using Python, with options to define custom paths for the 
        raw data files, output directories, and the seed. Example usage:

        python basic_data_wrangling.py --raw-data-white path/to/white_wine_data.csv 
        --raw-data-red path/to/red_wine_data.csv --processed-data path/to/processed_data --seed 522

    Arguments:
        --raw-data-white: Path to the raw data file for white wine.
        --raw-data-red: Path to the raw data file for red wine.
        --processed-data: Directory path to save the combined processed data. Default is '../data/processed'.
        --train-data: Directory path to save the training data split. Default is '../data/processed'.
        --test-data: Directory path to save the testing data split. Default is '../data/processed'.
        --seed: Seed for the random number generator to ensure reproducibility. Default is 522.

    Functionality:
        1. Reads the raw white and red wine data from the specified file paths.
        2. Adds a 'color' feature to distinguish between white and red wines.
        3. Concatenates the two datasets into a single dataframe.
        4. Splits the combined dataset into training and testing sets, stratified by wine color, using the 
        provided random seed.
        5. Saves the processed complete dataset, training set, and testing set as CSV files in the specified 
        directories.

    Output:
        - 'wine_processed.csv': The complete processed dataset including both white and red wines.
        - 'wine_train.csv': The training subset of the dataset.
        - 'wine_test.csv': The testing subset of the dataset.

    Note:
        Ensure the specified raw data files are in the correct format (CSV) and the necessary Python 
        packages (pandas, sklearn, etc.) are installed. The script expects semicolon-separated values 
        in the raw data files.

    Example:
    python basic_data_wrangling.py --raw-data-white ../data/raw/winequality-white.csv --raw-data-red ../data/raw/winequality-red.csv
    """


    if not os.path.exists(processed_data):
        os.makedirs(processed_data)
  
    df_white = pd.read_csv(raw_data_white, sep=";")
    df_red = pd.read_csv(raw_data_red, sep=";")

    df_white['color'] = 'white'
    df_red['color'] = 'red'
    df_wine = pd.concat([df_white, df_red], ignore_index=True)
    
    df_wine.to_csv(os.path.join(processed_data, "wine_processed.csv"))

    wine_train, wine_test = train_test_split(
        df_wine, train_size=0.70, stratify=df_wine["color"], random_state=seed)
   
    wine_train.to_csv(os.path.join(train_data, "wine_train.csv"))
    wine_test.to_csv(os.path.join(test_data, "wine_test.csv"))

if __name__ == '__main__':
    main()