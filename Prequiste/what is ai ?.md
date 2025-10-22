

## AI Foundations: What Is AI?

### Concept Definition

Artificial Intelligence (AI) is the science of making computers do things that normally require human intelligence, such as understanding language, recognizing images, making decisions, and learning from experience.

### Why It Matters

AI powers many modern technologies, from chatbots and recommendation systems to self-driving cars and medical diagnosis. It helps automate tasks, solve complex problems, and create new possibilities in every industry.

### Analogy

Think of AI as a robot assistant that learns from examples and helps you with tasks, just like a helpful coworker who gets better with practice.

### Architecture \& Workflow Diagram

```
+-------------------+
|   User Input      |
+-------------------+
          |
          v
+-------------------+
|   AI System       |
+-------------------+
          |
          v
+-------------------+
|   Output/Action   |
+-------------------+
```


### Code Example

Here’s a simple Python example using a basic AI model (text classification):

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = ["I love AI", "AI is amazing", "I dislike bugs"]
labels = [1, 1, 0]  # 1 = positive, 0 = negative

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Predict new text
test_text = ["AI helps me"]
X_test = vectorizer.transform(test_text)
prediction = model.predict(X_test)
print("Prediction:", prediction)
```


### Line-by-Line Code Explanation

- Import libraries for text processing and machine learning.
- Prepare training data: texts and their labels (positive/negative).
- Convert text to numbers using `CountVectorizer`.
- Train a Naive Bayes model on the data.
- Predict the sentiment of a new text.


### Real-World Use Case

Text classification is used in spam detection, sentiment analysis, and customer support automation.

### Practice Task

- Write a Python script that classifies texts as positive or negative using your own examples.
- Change the training data and see how predictions change.


### Common Mistakes \& Debugging Tips

- Not preprocessing text (removing punctuation, lowercasing).
- Using too little training data.
- Forgetting to transform new text with the same vectorizer.


### Best Practices

- Use clean, well-labeled data.
- Test your model on new examples.
- Start simple, then try more advanced models.


### Key Takeaways

- “Start” means to begin something; in AI, it’s about starting to learn and build intelligent systems.[^4][^1]
- AI uses data and models to make predictions and automate tasks.


### Practice Time

- Try building a simple text classifier in Python.
- List three ways AI is used in everyday life.

