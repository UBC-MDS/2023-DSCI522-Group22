import altair as alt

"""
    Creates a detailed distribution plot for two types of wine.

    This function generates a comparative distribution plot of wine characteristics by color. It combines tick, boxplot, and point plots using Altair.
    This function is used for exploratory data analysis for data comparing red and white wine.

    Parameters:
    - data (DataFrame): The DataFrame containing wine data.
    - numeric_cols (list of str): List of numeric column names in data to be used in the plot.

    Returns:
    altair.vegalite.v5.api.RepeatChart: An Altair RepeatChart object displaying the distribution detail plot.

    Example Usage:
    >>> wine_data = pd.DataFrame({
    ...     'color': ['red', 'white', 'red', 'white'],
    ...     'alcohol': [12.8, 13.4, 14.2, 12.9],
    ...     'sugar': [0.7, 0.2, 0.3, 0.6]
    ... })
    >>> numeric_cols = ['alcohol', 'sugar']
    >>> plot = create_distribution_detail_plot(wine_data, numeric_cols)
    >>> plot.display()
    """


def create_distribution_detail_plot(data, numeric_cols):
    distribution_detail = (
        alt.Chart(data).mark_tick().encode(
            alt.X(alt.repeat(), type="quantitative").scale(zero=False),
            alt.Y("color", title=""),
            alt.Color("color", legend=alt.Legend(title="Type of Wine"), 
                      scale=alt.Scale(domain=['red', 'white'], range=['red', 'peachpuff']))) 
        +
        alt.Chart(data).mark_boxplot(extent="min-max", color="grey", opacity=0.6).encode(
            alt.X(alt.repeat(), type="quantitative"),
            alt.Y("color", title=""))
        +   
        alt.Chart(data).mark_point(filled=True, color="black", size=10).encode(
            alt.X(alt.repeat(), aggregate='mean', type="quantitative"),
            alt.Y("color", title=""))
    ).properties(
        height=50, width=200
    ).repeat(repeat=numeric_cols, columns=2, title='Comparative Distribution of Wine Characteristics by Color')

    return distribution_detail



def create_numeric_hist_plots(data, numeric_cols):
    """
    Create histogram plots for numeric features of wine data.

    This function generates histogram plots for each numeric feature in the wine data to compare the distribution of these features across different types of wine.
    This function is used for exploratory data analysis for data comparing red and white wine.

    Parameters:
    - data (DataFrame): The DataFrame containing wine data.
    - numeric_cols (list of str): List of column names in 'data' that are numeric and will be used in the plot.

    Returns:
    altair.vegalite.v5.api.RepeatChart: An Altair RepeatChart object displaying the numeric histogram plots.

    Example Usage:
    >>> wine_data = pd.DataFrame({
    ...     'color': ['red', 'white', 'red', 'white'],
    ...     'alcohol': [12.8, 13.4, 14.2, 12.9],
    ...     'sugar': [0.7, 0.2, 0.3, 0.6]
    ... })
    >>> numeric_cols = ['alcohol', 'sugar']
    >>> histogram_plots = create_numeric_hist_plots(wine_data, numeric_cols)
    >>> histogram_plots.display()
    """

    numeric_hist_plots = alt.Chart(data).mark_bar(opacity=0.6).encode(
        alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=30)),
        y='count()',
        color=alt.Color('color', 
                        legend=alt.Legend(title="Type of Wine"), 
                        scale=alt.Scale(domain=['red', 'white'], 
                                        range=['red', 'peachpuff'])
                       )
    ).properties(height=150, width=250
                ).repeat(repeat=numeric_cols, columns=2, title='Comparative Distribution of Wine Characteristics by Color')

    return numeric_hist_plots