import click
import pandas as pd
import altair as alt
import os

#To-do:Create doc string 

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


