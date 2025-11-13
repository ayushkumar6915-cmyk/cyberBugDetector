import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

code_samples = [
    "eval('print(123)')",
    "password = 'admin123'",
    "pickle.loads(data)",
    "print(f'Hello {user}')",
    "json.loads(data)",
    "query = 'SELECT * FROM users WHERE username = %s'"
]

labels = [1, 1, 1, 0, 0, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(code_samples)

model = RandomForestClassifier()
model.fit(X, labels)

joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ ML model and vectorizer saved in 'models/' folder.")

def predict_code_snippet(code):
    model = joblib.load("models/model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    
    lines = code.split('\n')
    bugs = []
    for i, line in enumerate(lines, 1):
        X_line = vectorizer.transform([line])
        prediction = model.predict(X_line)[0]
        if prediction == 1:
            bugs.append((i, "Potential bug detected by ML model"))
    return bugs