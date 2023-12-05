# Define variables
DATA_DIR = data
RAW_DATA_DIR = $(DATA_DIR)/raw
PROCESSED_DATA_DIR = $(DATA_DIR)/processed
RESULTS_DIR = results
FIGURES_DIR = $(RESULTS_DIR)/figures
MODELS_DIR = $(RESULTS_DIR)/models
TABLES_DIR = $(RESULTS_DIR)/tables

# Seed for reproducibility
SEED = 522

.PHONY: all data wrangling eda preprocess analysis visualize clean

all: data wrangling eda preprocess analysis visualize

# Step 1: Download and extract data
data:
	python scripts/download_file.py --url="https://archive.ics.uci.edu/static/public/186/wine+quality.zip" --destination=$(RAW_DATA_DIR)/

# Step 2: Basic data wrangling
wrangling:
	python scripts/basic_data_wrangling.py --raw-data-white=$(RAW_DATA_DIR)/winequality-white.csv --raw-data-red=$(RAW_DATA_DIR)/winequality-red.csv --processed-data=$(PROCESSED_DATA_DIR)/ --train-data=$(PROCESSED_DATA_DIR)/ --test-data=$(PROCESSED_DATA_DIR)/ --seed=$(SEED)

# Step 3: EDA
eda:
	python scripts/eda.py --train-data=$(PROCESSED_DATA_DIR)/wine_train.csv --plot-path=$(FIGURES_DIR)/

# Step 4: Preprocessing
preprocess:
	python scripts/preprocess.py --data-to=$(PROCESSED_DATA_DIR)/ --preprocessor-to=$(MODELS_DIR)/

# Step 5: Analysis
analysis:
	python scripts/model.py --scaled-data=$(PROCESSED_DATA_DIR)/ --results-dir=$(TABLES_DIR)/ --model-save-dir=$(MODELS_DIR)/

# Step 6: Visualize the result
visualize:
	python scripts/wine_classification_plot_script.py --dataframe-csv=$(TABLES_DIR)/logistic_regression_feature_importance.csv --output-path=$(FIGURES_DIR)/predict_visualization.png

# Clean up
clean:
	rm -rf $(RAW_DATA_DIR)/*
	rm -rf $(PROCESSED_DATA_DIR)/*
	rm -rf $(FIGURES_DIR)/*
	rm -rf $(MODELS_DIR)/*
	rm -rf $(TABLES_DIR)/*

