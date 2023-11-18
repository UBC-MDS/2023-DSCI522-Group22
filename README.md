# 2023-DSCI522-Group22
# A Practical Exploration of the Wine Quality Dataset
### By Jordan Cairns, Chris Gao, Yingzi Jin, and Chun Li

## Project Overview
In the intricate world of oenology, the distinction between red and white wines extends beyond color, embedding itself in the nuanced spectrum of their physicochemical properties. This project embarks on a data-driven journey to unravel these complexities by leveraging statistical models to classify wines as red or white based on their inherent characteristics. Utilizing a rich dataset that encapsulates key attributes like acidity, sugar content, sulfur dioxide levels, alcohol concentration, and more, we aim to build a predictive model that not only accurately classifies the wines but also sheds light on the influential factors that underpin this classification. Through this analysis, we intend to blend the art of winemaking with the precision of data science, offering insights that could prove valuable to vintners, sommeliers, and wine enthusiasts alike in understanding the subtle distinctions between these two celebrated categories of wine!

## Licenses
This project is licensed under the [MIT License] [LICENSE.md](https://github.com/UBC-MDS/2023-DSCI522-Group22/blob/main/LICENSE).

## Environment Setup
To recreate our computational environment, please use conda and the provided `env-group-project.yml` file in the root directory. Run the following command in the command line:
conda env create -f env-group-project.yml

dependencies:
    - python==3.10
    - ipykernel
    - matplotlib>=3.8.0
    - pandas>=2.1.1
    - scikit-learn>=1.3.1    
    - requests>=2.24.0
    - ipython
    - graphviz
    - python-graphviz
    - lightgbm
    - altair=5.1.2
    - vl-convert-python  # For saving altair charts as static images
    - vegafusion  # For working with charts > 5,000 graphical objects
    - vegafusion-python-embed  # Same as the previous one
    - vegafusion-jupyter  # For working with charts > 100,000 graphical objects
    - vega_datasets  # Example data    
    - jinja2
    - pip>=23.2.1    
    - pip:
        - mglearn
        - graphviz
        - psutil>=5.7.2

