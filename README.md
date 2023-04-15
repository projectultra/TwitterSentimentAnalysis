# Twitter Sentiment Analysis

This is my first project I made to delve into Machine Learning. It focuses on sentiment analysis of tweets using machine learning

It was built in Google Colaboratory which is a cloud-based Juptyer notebook environment which provides free access to GPUs and TPU suitable for machine learning

The dataset was obtained from Kaggle
The neural network model used for this project is a Convolutional Neural Network (CNN)  model with an embedding layer for word representation, followed by a convolutional layer to detect features, a max pooling layer for reducing dimensionality, a dense layer, and a final output layer.

The model was trained on the dataset with an accuracy of ~80%.

A Django App was also built and can be found in the respective folder

For future iterations of this project, the following improvements could be made:

Try different model architectures, such as Recurrent Neural Networks.
Explore the use of pre-trained word embeddings like Word2Vec to improve the performance of the model.
Use a different dataset to train the model.
Hyperparameter Tuning with Keras can help to find the best combination of hyperparameters.
