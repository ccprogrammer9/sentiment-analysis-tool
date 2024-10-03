import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load training data from CSV
data = pd.read_csv('train_travel_data.csv')

# Assuming the CSV has two columns: 'text' and 'label'
# Adjust the column names as necessary
training_data = data['text'].tolist()  # List of texts
labels = data['label'].tolist()         # List of corresponding labels

# Initialize the vectorizer and classifier
vectorizer = TfidfVectorizer()
classifier = MultinomialNB()

# Fit the vectorizer on training data
X_train = vectorizer.fit_transform(training_data)

# Fit the classifier on the transformed training data
classifier.fit(X_train, labels)

# Save the vectorizer and classifier to disk (optional, for later use)
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(classifier, 'classifier.pkl')

def predict_sentiment(text):
    # Load the fitted vectorizer and classifier (if needed)
    # vectorizer = joblib.load('vectorizer.pkl')
    # classifier = joblib.load('classifier.pkl')

    X = vectorizer.transform([text])  # Transform the input text
    prediction = classifier.predict(X)  # Predict the sentiment
    return prediction[0]  # Return the sentiment
