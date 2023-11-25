# 2023-DSCI522-Group22
# A Practical Exploration of the Wine Quality Dataset
### By Jordan Cairns, Chris Gao, Yingzi Jin, and Chun Li

## Project Overview
Our analysis aimed to develop a predictive model to distinguish between red and white wines based on various physicochemical properties. This study employed logistic regression, a model renowned for its balance between predictive power and interpretability.

The regression result suggested that residual sugar and total sulfur dioxide had high positive coefficients, indicating a strong association with white wine, whereas density showed the most substantial negative impact, followed by alcohol and volatile acidity, suggesting these are key indicators of red wine.

The logistic regression model not only achieved high accuracy but also provided valuable insights into the features most indicative of wine type. This model can assist vintners in quality control and classification tasks. Moreover, the interpretability of the model offers a foundation for further research into wine composition and its impact on sensory attributes. Future studies might explore more complex models or delve deeper into feature engineering to enhance predictive accuracy and understanding.

## Licenses
This project is licensed under the [MIT License] [LICENSE.md](https://github.com/UBC-MDS/2023-DSCI522-Group22/blob/main/LICENSE).

## Environment Setup
To recreate our computational environment, please use conda and the provided `env-group-project.yml` file in the root directory. Run the following command in the command line:
conda env create -f env-group-project.yml

dependencies:
  - python=3.11.6
  - ipykernel=6.26.0
  - pandas=2.1.3
  - requests=2.31.0
  - altair=5.1.2
  - scikit-learn=1.3.2
