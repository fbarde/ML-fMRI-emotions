# ML-fMRI-emotions
Machine Learning for emotion prediction from brain fMRI data.

Date: Sep-Dec 2021\
Course: CS-433 - Machine Learning (Prof. Flammarion Bernard, Prof. Jaggi Martin)\
Collaborators: Manon Bechaz, Laura Maria\
Supervisor: Dr. Elenor Morgenroth\

## General aim of the code

The code is part of a project aiming at using different machine learning methods to map functional magnetic resonance imaging (fMRI) data to associated emotions.
The provided code gathers the different methods used, the functions used for their optimization as well as scripts to reproduce the obtained results.

## Structure of the code

The code is divided in different sections, or folders. 
### data --> not available for confidentiality
This folder contains the preprocessed data. 
- **preprocessed_brain_data**: this subfolder gathers the results of the preprocessing of the brain images (i.e. outputs of the code "preprocessing_brain.ipynb")
- **preprocessed_emotion_data**: this subfolder gathers the results of the preprocessing of the emotion annotations (i.e. outputs of the code "preprocessing_emotions.ipynb" )
- **combined_data**: this subfolder gathers the final results of the preprocessing, after combination of the two previous datasets (i.e. outputs of the code "preprocessing_split_people.py" )

### data_analysis
This folder gathers some prior studies and analysis of the dataset.

### preprocessing
This folder contains the code to preprocess the brain and emotion data, and to concatenate them. 
- **preprocessing_emotions.ipynb** : preprocess the emotion data,
- **preprocessing_brain.ipynb** : preprocess the brain data,
- **preprocessing_combine_brain_emotions.py** : concatenate the preprocessed brain and emotion data
- **preprocessing_split_people_48.py**, **preprocessing_split_people.py** : concatenate the preprocessed brain and emotion data, for the 48 and 400 brain regions datasets, and splits it in test and training data

### processing
This gathers all machine learning methods applied
- **Find_Hyperparameters_________.ipynb** :  Uses GridsearchCV to optimize the parameters of the Neural Networks used.
- **MCC_Laura.ipynb** : Tests a multiclass classification model.
- **regression_analysis.ipynb** : Tests several regression models.
- **Optimization_Models.ipynb**  optimizing the parameters of the different machine learning methods.
- **Models.ipynb** :  Implements the different machine learning methods tested for the classification of the emotions.

## results_analysis_and_plots
This final folder contains scripts to analyse the data and reproduce the figures present in the report. 

