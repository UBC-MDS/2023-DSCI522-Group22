import altair as alt

def create_wine_prediction_chart(dataframe, red_wine_color, white_wine_color):
    """
    Create a bar chart to display wine predictions based on coefficients.

    Args:
    dataframe (pd.DataFrame): The dataframe containing the features and coefficients.
    red_wine_color (str): Color to use for bars predicting Red Wine.
    white_wine_color (str): Color to use for bars predicting White Wine.

    Returns:
    alt.Chart: An Altair bar chart.

    Example usage:
    result_df = <your_dataframe>
    chart = create_wine_prediction_chart(result_df, 'red', 'peachpuff')
    chart
    """
    # Input validation
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("The 'dataframe' argument must be a pandas DataFrame.")
    
    if dataframe.empty:
        raise ValueError("The 'dataframe' argument must not be empty.")

    if not 'Coefficient' in dataframe.columns:
        raise ValueError("The DataFrame must contain a 'Coefficient' column.")
    
    if not isinstance(red_wine_color, str) or not isinstance(white_wine_color, str):
        raise ValueError("The color arguments must be strings.")
    
    if not red_wine_color.strip():
        red_wine_color = "darkred"
    
    if not white_wine_color.strip():
        white_wine_color = "darkred"

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

    return chart


