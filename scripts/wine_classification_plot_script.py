import click
import pandas as pd
import altair as alt
import os

'''
This script generates a visualization for a logistic regression model's coefficients, 
differentiating the features indicative of red and white wines. 

It reads a dataframe from a CSV file, performs validation checks, and processes the data 
to associate coefficients with wine predictions. The script uses the Altair library to create 
a bar chart that visualizes the importance of different properties in predicting 
wine type.

Parameters:
----------
dataframe_csv : str
    Path to the CSV file containing the dataframe with logistic regression coefficients.
red_wine_color : str, optional
    Color to represent features predicting Red Wine in the visualization (default is 'red').
white_wine_color : str, optional
    Color to represent features predicting White Wine in the visualization (default is 'peachpuff').
output_path : str, optional
    The output file path where the visualization will be saved as a PNG image (default is 
    '../results/figures/predict_visualization.png').

Raises:
------
ValueError:
    If the dataframe is empty, if 'Coefficient' column is missing from the dataframe, 
    or if the output path does not end with '.png'.
FileNotFoundError:
    If the directory specified in the output path does not exist.

Output:
------
A PNG image file of the visualization is saved to the provided output path. The image 
illustrates the logistic regression coefficients as bars, color-coded to represent their 
prediction for red or white wine based on the physicochemical properties of the wines.

Example:
-------
To run this script from the command line, you may use the following format:
$ python wine_classification_plot_script.py --dataframe-csv path/to/dataframe.csv 
--red-wine-color darkred --white-wine-color lightblue --output-path path/to/output.png

The above command will generate a visualization with customized colors for red and white wine predictions 
and save it to the specified output path.
'''

@click.command()
@click.option('--dataframe-csv', type=str, required=True, help="Path to the CSV file containing the dataframe")
@click.option('--red-wine-color', type=str, default='red', help="Color to use for bars predicting Red Wine")
@click.option('--white-wine-color', type=str, default='peachpuff', help="Color to use for bars predicting White Wine")
@click.option('--output-path', type=str, default='../results/figures/predict_visualization.png', help="The output path to save the results of the visualization")

def main(dataframe_csv, red_wine_color, white_wine_color, output_path):
    # Read the dataframe from CSV
    dataframe = pd.read_csv(dataframe_csv)

    # Input validation
    if dataframe.empty:
        raise ValueError("The 'dataframe' argument must be a non-empty pandas DataFrame.")
    
    if 'Coefficient' not in dataframe.columns:
        raise ValueError("The DataFrame must contain a 'Coefficient' column.")
    
    # Set default color for red wine if empty or only whitespace
    if not red_wine_color.strip():
        red_wine_color = "red"
        
    # Set default color for white wine if empty or only whitespace
    if not white_wine_color.strip():
        white_wine_color = "peachpuff"

    # Validate output path
    if not output_path.endswith('.png'):
        raise ValueError("The output path must end with '.png'.")
    
    output_directory = os.path.dirname(output_path)
    if output_directory and not os.path.exists(output_directory):
        raise FileNotFoundError(f"The directory '{output_directory}' does not exist.")

    # Add a new column for Wine Prediction based on the coefficient
    dataframe['Wine Prediction'] = dataframe['Coefficient'].apply(lambda x: 'Predicting White Wine' if x > 0 else 'Predicting Red Wine')

    # Create the chart
    chart = alt.Chart(dataframe).mark_bar().encode(
        x='Coefficient',
        y='Feature Name',
        color=alt.Color('Wine Prediction', 
                        legend=alt.Legend(title="Wine Prediction"), 
                        scale=alt.Scale(domain=['Predicting Red Wine', 'Predicting White Wine'], 
                                        range=[red_wine_color, white_wine_color])
                       )
    )  
    # Save the chart
    chart.save(output_path)

if __name__ == '__main__':
    main()


