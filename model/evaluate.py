import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

model = joblib.load("model/fhe_model.joblib")
df = pd.read_csv("data/adhd.csv")

X = df.drop("ADHD", axis=1)
y = df["ADHD"]

y_pred = model.predict(X)
print("Accuracy:", accuracy_score(y, y_pred))
