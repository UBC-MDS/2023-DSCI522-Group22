import click
import os
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.option('--raw-data-white', type=str, help="Path to processed training data white")
@click.option('--raw-data-red', type=str, help="Path to processed training data red")
@click.option('--processed-data', type=str, help="Path to directory to save processed data")
@click.option('--train-data', type=str, help="Path to directory where the train data will be written to")
@click.option('--test-data', type=str, help="Path to directory where the test data will be written to")


def main(raw_data_white, raw_data_red, processed_data, train_data, test_data):
    
    df_white = pd.read_csv(raw_data_white, sep = ";")
    df_red = pd.read_csv(raw_data_red, sep = ";")

    df_white['color'] = 'white'
    df_red['color'] = 'red'
    df_wine = pd.concat([df_white, df_red], ignore_index=True)
    
    df_wine.to_csv(os.path.join(
        processed_data, "wine_processed.csv"))

    wine_train, wine_test = train_test_split(
        df_wine, train_size=0.70, stratify=df_wine["color"])
   
    wine_train.to_csv(os.path.join(
        train_data, "wine_train.csv"))
    wine_test.to_csv(os.path.join(
        test_data, "wine_test.csv"))
    

if __name__ == '__main__':
    main()

