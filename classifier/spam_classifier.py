import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Sample training data
emails = [
    ("Free money!!!", "You have won $1000. Claim now!", True),
    ("Meeting reminder", "Don't forget our meeting tomorrow.", False),
    # Add more training data here
]

# Prepare the data
X = [subject + " " + body for subject, body, is_spam in emails]
y = [is_spam for subject, body, is_spam in emails]

# Create a pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X, y)

# Save the model
with open('spam_classifier.pkl', 'wb') as f:
    pickle.dump(model, f)

def classify_email(subject, body):
    with open('spam_classifier.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([subject + " " + body])[0]