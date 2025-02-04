# FDS-Epi-Project

## Overview
This machine learning project was a collaboration with Sandia National Labs aimed at predicting COVID-19 hotspots during the early stages of the pandemic. The goal was to enable public health authorities to proactively allocate resources and implement preventative measures such as social distancing and masking. Our team designed a machine learning classifier using county-level data, incorporating both disease testing and demographic data.

The definition of a "hotspot" was based on the CDC's criteria, classifying areas with high transmission rates. The model considered spatial and temporal factors, acknowledging that the spread of infectious diseases is influenced by human contact and the disease prevalence in neighboring regions.

To ensure the model's reliability, especially for policy-making and national security, the project emphasized the need for trustworthy machine learning techniques. The main computational methods used included Residual Neural Networks deep learning-based modeling, which combined demographic, spatial, and temporal data to forecast potential hotspots up to two weeks in advance.

## Packages Used
The following Python packages are required:
- `pytorch`: For neural network modeling.
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `scikit-learn`: For data splitting.

## Running the model
After further machine learning coursework and work experience, I built a new model that employs better practices. For example, categorical variables are handled differently depending on whether they are ordinal or nominal, data splitting is done sequentially since the data is sequential, and I use a simpler Neural Network model. The improved model can be found in the Jupyter Notebook: [Epi_NN_Model_Improved.ipynb](https://github.com/ecthompsoncodes/FDS-Epi-Project/blob/main/Epi_NN_Model_Improved.ipynb).

The model architecture, training and evaluation for the original model is contained in Neural_Network_Epi_Model.ipynb. You can read the final report here: [Trustworthy_AI_for_Epidemiology_Applications.pdf](https://github.com/ecthompsoncodes/FDS-Epi-Project/files/15179439/Trustworthy_AI_for_Epidemiology_Applications.pdf)
