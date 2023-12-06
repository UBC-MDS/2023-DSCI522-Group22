# Using the Jupyter minimal-notebook as base image
FROM quay.io/jupyter/minimal-notebook:2023-11-19

# Installing necessary packages to reproduce the analysis
RUN conda install -y \
    python=3.11.6 \
    pandas=2.1.3 \
    ipykernel=6.26.0 \
    scikit-learn=1.3.2 \
    requests=2.31.0 \
    altair=5.1.2 \
    notebook=7.0.6 \
    pytest=7.4.3 \
    click=8.1.7 \
    jupyter-book=0.15.1 \
    vl-convert-python=[version='>=0.14.0']