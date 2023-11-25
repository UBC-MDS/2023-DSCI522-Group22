FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y python=3.11.6
RUN conda install -y pandas=2.1.3
RUN conda install -y scikit-learn=1.3.1
RUN conda install -y altair=5.1.2
