# Naive-Bayes-classifier

# Overview
A naive Bayes classifier to identify hotel reviews as either true or fake, and either positive or negative. You will be using the word tokens as features for classification.


# Programs

Two programs: nblearn.py will learn a naive Bayes model from the training data, and nbclassify.py will use the model to classify new data. If using Python 3, you will name your programs nblearn3.py and nbclassify3.py. The learning program will be invoked in the following way:

> python nblearn.py /path/to/input

The argument is a single file containing the training data; the program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt. The format of the model is up to you, but it should follow the following guidelines:

The model file should contain sufficient information for nbclassify.py to successfully label new data.
The model file should be human-readable, so that model parameters can be easily understood by visual inspection of the file.
The classification program will be invoked in the following way:

> python nbclassify.py /path/to/input

The argument is a single file containing the test data file; the program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each entry in the test data, and write the results to a text file called nboutput.txt in the same format as the answer key.

