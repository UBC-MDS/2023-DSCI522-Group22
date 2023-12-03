import pandas as pd
import altair as alt

# The following block of code was inspired by online resources and 531 Lecture
# of creating correlation heatmap via Altair 
def cor_matrix_plot(corr_data):
    """
    Generates a correlation heatmap visualizing the pairwise correlation between variables.

    Parameters:
    -----------
    corr_data : pandas DataFrame
        The input DataFrame containing correlation values between variables.

    Returns:
    --------
    alt.Chart
        An Altair chart representing the correlation heatmap with text descriptions.
    """
    # Base chart for x and y values 
    base = alt.Chart(corr_data).encode(
        alt.X('level_1:O', title="variable name"),
        alt.Y('level_0:O', title="variable name")
    )
    # Correlation heatmap
    cor_plot = base.mark_rect().encode(
        color='correlation:Q'
    )
    # Add Text decription for every correlation
    labels = base.mark_text().encode(
        text='correlation_text',
        color=alt.condition(
            alt.datum.correlation > 0.5, 
            alt.value('white'),
            alt.value('black')))
    # Adding layers together
    final_output = (cor_plot + labels).properties(
            height=400, width=400,
            title='Correlation Heatmap: numeric features')
    
    return final_output