# Twitter Sentiment Analysis

This project focuses on sentiment analysis of tweets using machine learning techniques. It utilizes a Convolutional Neural Network (CNN) model with an embedding layer for word representation. The model was trained on a dataset obtained from Kaggle, achieving an accuracy of approximately 80%.

## Requirements

To run this project, you will need the following:

- Python
- Django
- TensorFlow
- Keras

Additionally, please ensure that you have the necessary dependencies installed by running the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

To get started with the Twitter Sentiment Analysis app, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/projectultra/TwitterSentimentAnalysis.git
```

2. Change into the project directory:

```bash
cd Django-app
```

3. Run the Django development server:

```bash
python manage.py runserver
```

4. Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

Once the application is running, you can use it to analyze the sentiment of tweets. Enter a tag in the provided input field and click the search button. The app will then classify the sentiment of the tweets as positive or negative.

## Project Structure

The project structure is organized as follows:

- `Neural Network Model`: This directory contains the machine learning model implementation.
- `Django-app`: This is the Django project directory.
## Future Improvements

To further enhance this project, consider implementing the following improvements:

1. **Exploring Different Model Architectures:** Try using Recurrent Neural Networks (RNNs) or other architectures to compare their performance with the current CNN model.

2. **Utilizing Pre-trained Word Embeddings:** Experiment with pre-trained word embeddings like Word2Vec to improve the model's ability to understand the context and nuances of tweets.

3. **Using Alternative Datasets:** Explore the use of different datasets to train the model, as different datasets may contain unique characteristics and biases that can impact the model's performance.

4. **Hyperparameter Tuning:** Utilize techniques like grid search or random search to find the best combination of hyperparameters for the model, improving its overall accuracy and performance.

Please note that deploying the app may require additional steps, as the Twitter API is no longer free. Adjustments may be needed to accommodate changes in the API's usage policies or to find alternative data sources for sentiment analysis.

Feel free to experiment and build upon this project to further enhance your understanding of machine learning and sentiment analysis techniques.
