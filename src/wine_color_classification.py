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
    """
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

# Example usage:
# result_df = <your_dataframe>
# chart = create_wine_prediction_chart(result_df, 'red', 'peachpuff')
# chart
