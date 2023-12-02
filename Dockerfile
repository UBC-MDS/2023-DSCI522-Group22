FROM quay.io/jupyter/minimal-notebook:2023-11-19

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

RUN conda install -y python=3.11.6
RUN conda install -y pandas=2.1.3
RUN conda install -y ipykernel=6.26.0
RUN conda install -y scikit-learn=1.3.1
RUN conda install -y requests=2.31.0
RUN conda install -y altair=5.1.2
RUN conda install -y notebook=7.0.6
RUN conda install -y pytest=7.4.3
