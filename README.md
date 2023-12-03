# 2023-DSCI522-Group22
# A Practical Exploration of the Wine Quality Dataset
### By Jordan Cairns, Chris Gao, Yingzi Jin, and Chun Li

## Project Overview
Our analysis aimed to develop a predictive model to distinguish between red and white wines based on various physicochemical properties. This study employed logistic regression, a model renowned for its balance between predictive power and interpretability.

The regression result suggested that residual sugar and total sulfur dioxide had high positive coefficients, indicating a strong association with white wine, whereas density showed the most substantial negative impact, followed by alcohol and volatile acidity, suggesting these are key indicators of red wine.

The logistic regression model not only achieved high accuracy but also provided valuable insights into the features most indicative of wine type. This model can assist vintners in quality control and classification tasks. Moreover, the interpretability of the model offers a foundation for further research into wine composition and its impact on sensory attributes. Future studies might explore more complex models or delve deeper into feature engineering to enhance predictive accuracy and understanding.

## Report
The full report can be viewed online [here](https://github.com/UBC-MDS/2023-DSCI522-Group22/blob/main/notebooks/wine_color_classification_report.ipynb) or locally at `../html/wine_color_classification_report.html`

## Dependencies
The [Docker](https://www.docker.com/) image utilized for this project, sourced from `quay.io/jupyter/minimal-notebook:notebook-7.0.6`, serves as a container solution designed to handle the software dependencies required for this project. For more detail, please refer to our [Dockerfile](https://github.com/UBC-MDS/2023-DSCI522-Group22/blob/main/Dockerfile)

## Usage

#### Setup

1. [Install](https://www.docker.com/get-started/) 
and launch Docker on your computer.

2. Clone this GitHub repository.

#### Running the analysis

1. Navigate to the root of this project on your computer using the
   command line and enter the following command:

``` 
docker compose up
```
2. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=` 
Copy and paste that URL into your browser.

3. To run the analysis,
enter the following commands in the terminal in the project root:

```
# Step 1: download and extract data
python download_file.py --url "https://archive.ics.uci.edu/static/public/186/wine+quality.zip" --destination "../data/raw"


# Step 2: basic data wrangling
python basic_data_wrangling.py \
  --raw-data-white "../data/raw/winequality-white.csv" \
  --raw-data-red "../data/raw/winequality-red.csv" \
  --processed-data "../data/processed" \
  --train-data "../data/processed" \
  --test-data "../data/processed" \
  --seed 522


# Step 3: EDA
# This step saves several graphs in PNG format as a part of EDA
# The following 3 files are required to run this script. Make sure they exist under the src folder
# helper_func_eda_visualization.py
# cor_matrix_plot.py
# layered_distri_plot.py
python eda.py --train-data "../data/processed" --plot-path "../results/figures"


# Step 4: Preprocessing
# This step saves the preprocessor to a pickle object under "results/models"
python preprocess.py --data-to "../data/processed" --preprocessor-to "../results/models"


# Step 5: Analysis
# This step uses a machine learning model to study the scaled data
# Result tables and model object will be saved locally
python model.py \
  --scaled-data "../data/processed" \
  --results-dir "../results/tables" \
  --model-save-dir "../results/models"


# Step 6: Visualize the result
# This step, by default, will generate predict_visualization.png under "results/figures/"
python wine_classification_plot_script.py \
  --dataframe-csv "../results/tables/logistic_regression_feature_importance.csv"
```

#### Clean up

1. To shut down the container and clean up the resources, 
type `Cntrl` + `C` in the terminal
where you launched the container, and then type `docker compose rm`

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
  - pytest=7.4.3
  - notebook=7.0.6
  - click=8.1.7

## Reference
This README.md file was largely inspired by and constructed upon [This version by Prof. Tiffany Timbers](https://github.com/ttimbers/breast_cancer_predictor_py/blob/v1.0.0/README.md).
Additional references are found under the full report
