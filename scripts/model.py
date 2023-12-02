import pandas as pd
import numpy as np
import os
import pickle
import click
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate

# Dictionary of models
models = { 
    "dummy": DummyClassifier(strategy="most_frequent"),
    "dtree": DecisionTreeClassifier(),
    "knn": KNeighborsClassifier(),
    "svm": SVC(),
    "nb": GaussianNB(),
    "lr": LogisticRegression(max_iter=1000),
}

@click.command()
@click.option('--scaled-data', type=str, help="Path to directory containing scaled data", default='../data/processed')
@click.option('--results-dir', type=str, help="Path to base results directory", default='../results')

def main(scaled_data, results_dir):
    # Paths for tables and models directories
    tables_dir = os.path.join(results_dir, 'tables')
    models_dir = os.path.join(results_dir, 'models')
    os.makedirs(tables_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)

    # Read the scaled data
    scaled_wine_train = pd.read_csv(os.path.join(scaled_data, 'scaled_wine_train.csv'), index_col=0)
    scaled_wine_test = pd.read_csv(os.path.join(scaled_data, 'scaled_wine_test.csv'), index_col=0)

    # Preparing data for machine learning model
    X_train = scaled_wine_train.drop(columns=['color'])
    y_train = scaled_wine_train['color']

    X_test = scaled_wine_test.drop(columns=['color'])
    y_test = scaled_wine_test['color']

    results_list = []

    for name, model in models.items():
        pipeline = make_pipeline(model)
        cv_results = cross_validate(pipeline, X_train, y_train, cv=5,
                                    return_train_score=True,
                                    scoring='accuracy',
                                    n_jobs=-1)
        results_list.append({
            "model": name,
            "fit_time": np.mean(cv_results['fit_time']),
            "score_time": np.mean(cv_results['score_time']),
            "test_score": np.mean(cv_results['test_score']),
            "train_score": np.mean(cv_results['train_score']),
        })

    results_df = pd.DataFrame(results_list)
    results_df.set_index('model', inplace=True)

    # Save cross-validation results
    results_df.to_csv(os.path.join(tables_dir, 'model_cv_results.csv'))

    # Test score reporting and feature importance
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)
    test_score = logistic_model.score(X_test, y_test)

    # Save the test score
    test_score_df = pd.DataFrame([{"model": "Logistic Regression", "test_score": test_score}])
    test_score_df.to_csv(os.path.join(tables_dir, 'logistic_regression_test_score.csv'), index=False)

    # Feature importance
    reg_data = {
        'Feature Name': logistic_model.feature_names_in_,
        'Coefficient': logistic_model.coef_[0]
    }
    result_df = pd.DataFrame(reg_data)
    result_df['Feature Name'] = result_df['Feature Name'].str.replace('standardscaler__', '').str.replace('ordinalencoder__', '')
    result_df.to_csv(os.path.join(tables_dir, 'logistic_regression_feature_importance.csv'), index=False)

    # Save the Logistic Regression model as a pickle file
    with open(os.path.join(models_dir, 'logistic_regression_model.pkl'), 'wb') as f:
        pickle.dump(logistic_model, f)

    # Print the results for quick viewing
    print("Cross-validation results:")
    print(results_df)
    print("\nLogistic Regression test score:", test_score)
    print("\nLogistic Regression feature importance:")
    print(result_df)

if __name__ == '__main__':
    main()
