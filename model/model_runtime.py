import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from concrete.ml.sklearn import LogisticRegression

# =============================
# LOAD DATASET
# =============================
df = pd.read_csv("data/adhd.csv")

# =============================
# ENCODE CATEGORICAL FEATURES
# =============================
categorical_cols = ["Gender", "EducationStage", "Medication", "SchoolSupport"]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# =============================
# FEATURES & TARGET
# =============================
X = df.drop("ADHD", axis=1)
y = df["ADHD"]

# =============================
# SPLIT
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =============================
# SCALE
# =============================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =============================
# TRAIN MODEL
# =============================
model = LogisticRegression(n_bits=8)
model.fit(X_train_scaled, y_train)

print("Plain Accuracy:", model.score(X_test_scaled, y_test))

# =============================
# COMPILE MODEL ONCE
# =============================
model.compile(X_train_scaled)

print("FHE Model Compiled Successfully!")

# =============================
# FUNCTION FOR PREDICTION
# =============================
def predict_adhd(input_dict):

    # Convert dict → DataFrame
    input_df = pd.DataFrame([input_dict])

    # Encode categorical
    for col in categorical_cols:
        input_df[col] = encoders[col].transform(input_df[col])

    # Scale
    input_scaled = scaler.transform(input_df)

    # FHE prediction
    prediction = model.predict(input_scaled, fhe="execute")[0]

    return int(prediction)
