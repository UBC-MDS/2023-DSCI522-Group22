import click
import requests
import os
import zipfile
from urllib.parse import urlparse
import io, sys
import pandas as pd

def concatenate_csv_files(file1, file2, delimiter, output_file):
    """
    Reads two CSV files, concatenates them vertically, ensuring only 12 columns,
    and saves the result to a new CSV file without the index column.
    
    :param file1: Path to the first CSV file, assumed to have headers and an index column.
    :param file2: Path to the second CSV file, assumed to not have headers and an index column.
    :param output_file: Path where the concatenated CSV will be saved.
    """
    # Read the first CSV file (with headers), dropping the index column if present
    df1 = pd.read_csv(file1, delimiter=delimiter,index_col=False)
    df1["color"]='red'
    # Read the second CSV file (without headers), and drop the index column if present
    df2 = pd.read_csv(file2, header=None, skiprows=1, delimiter=delimiter, index_col=False)
    df2["color"]='white'
    # Ensure df2 has the same column names as df1
    df2.columns = df1.columns
    
    # Concatenate the dataframes
    combined_df = pd.concat([df1, df2], ignore_index=True)
    # Ensure that the combined DataFrame has only 13 columns
    #combined_df = combined_df.iloc[:, :13]

    # Save the combined dataframe to a new CSV file without the index
    combined_df.to_csv(output_file, index=False)


def save_or_extract_file(content, filename, destination):
    """Save the content to a file or extract it if it's a zip and `unzip` is True."""
    file_path = os.path.join(destination, filename)
    if filename.endswith('.zip'):
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            z.extractall(destination)
        click.echo(f"Zip file extracted to {destination}")
    else:
        with open(file_path, 'wb') as f:
            f.write(content)
        click.echo(f"File saved to {file_path}")

@click.command()
@click.option('--url', type=str, required=True, help='The URL of the file to download.')
@click.option('--destination', type=click.Path(file_okay=False, dir_okay=True, writable=True), default='.', help='The directory to save the downloaded file.')
def main(url, destination):
    """Simple program that downloads a file from a given URL and handles it based on its file extension."""

    # Check and create the destination directory
    if not os.path.exists(destination):
        os.makedirs(destination)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        result = urlparse(url)
        filename = os.path.basename(result.path)
        save_or_extract_file(response.content, filename, destination)

        file1 = os.path.join(destination, 'winequality-red.csv')
        file2 = os.path.join(destination, 'winequality-white.csv')
        output_file = os.path.join(destination, 'winequality.csv')
        concatenate_csv_files(file1, file2, ";", output_file)
        
    except requests.exceptions.HTTPError as http_err:
        click.echo(f"HTTP error occurred: {http_err}", err=True)
        sys.exit(1)  # Exit with a non-zero status code
    except Exception as err:
        click.echo(f"An error occurred: {err}", err=True)
        sys.exit(1)  # Exit with a non-zero status code


if __name__ == '__main__':
    main()

