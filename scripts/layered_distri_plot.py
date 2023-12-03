import pandas as pd
import altair as alt

def layered_distri_plot(wine_train):
    """
    Generate a layered distribution plot using Altair for visualizing wine characteristics by color.

    Parameters:
    - wine_train (pandas.DataFrame): DataFrame containing wine data with columns representing characteristics 
                                     and 'color' column specifying wine type (e.g., 'red' or 'white').

    Returns:
    - Altair Chart: A layered distribution plot visualizing wine characteristics by color.
    """

    # Extract numeric columns (wine characteristics) excluding the 'color' column
    numeric_cols = wine_train.columns.tolist()[:-2]

    # Create a tick chart representing the distribution of wine characteristics by color
    tick_chart = alt.Chart(wine_train).mark_tick().encode(
        alt.X(alt.repeat(), type="quantitative").scale(zero=False),
        alt.Y("color", title=""),
        alt.Color(
            "color",
            legend=alt.Legend(title="Type of Wine"),
            scale=alt.Scale(domain=['red', 'white'], 
                            range=['red', 'peachpuff'])
        )
    )
    
    # Create a boxplot chart for each wine characteristic by color
    box_chart = alt.Chart(wine_train).mark_boxplot(
        extent="min-max", color="grey", opacity=0.6
    ).encode(
        alt.X(alt.repeat(), type="quantitative"),
        alt.Y("color", title="")
    )
    
    # Create a point chart representing mean values of each characteristic by color
    point_chart = alt.Chart(wine_train).mark_point(
        filled=True, color="black", size=10
    ).encode(
        alt.X(alt.repeat(), aggregate='mean', type="quantitative"),
        alt.Y("color", title="")
    )
    
    # Layer the charts (tick, boxplot, point) for each wine characteristic
    layer_chart = (tick_chart + box_chart + point_chart).properties(
        height=50, width=200
    ).repeat(
        repeat=numeric_cols, 
        columns=2, title='Comparative Distribution of Wine Characteristics by Color'
    )
    
    return layer_chart
