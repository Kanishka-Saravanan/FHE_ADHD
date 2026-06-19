# NeuroShield: Privacy-Preserving ADHD Prediction System using Concrete ML and Fully Homomorphic Encryption

## Overview

NeuroShield is a secure healthcare analytics application that predicts Attention Deficit Hyperactivity Disorder (ADHD) risk while preserving patient data privacy. The system integrates Machine Learning with Fully Homomorphic Encryption (FHE) using Concrete ML, enabling predictions to be performed directly on encrypted data without exposing sensitive information.

Unlike conventional machine learning applications where patient data must be decrypted before processing, NeuroShield ensures that data remains encrypted throughout the inference pipeline, providing a privacy-preserving and secure AI solution suitable for healthcare environments.

## Problem Statement

Healthcare datasets contain highly sensitive personal information, and traditional machine learning systems may expose this data during processing. This creates privacy and security concerns, especially in applications involving psychological and medical diagnosis.

NeuroShield addresses this challenge by implementing Fully Homomorphic Encryption, allowing secure ADHD prediction without revealing the user's raw data to the prediction server.

## Key Features

- Secure ADHD prediction using Fully Homomorphic Encryption (FHE)
- Machine learning model built using Concrete ML
- Logistic Regression based binary classification
- Encrypted inference with zero plaintext exposure
- User authentication system with registration and login
- Data preprocessing using Label Encoding and Standard Scaling
- Professional Flask-based web interface
- Privacy-preserving healthcare analytics architecture

## System Architecture

```
User Input
     |
     v
Data Preprocessing
     |
     v
Client-Side Encryption
     |
     v
Concrete ML FHE Model
     |
     v
Encrypted Prediction Execution
     |
     v
Secure Prediction Result
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| Flask | Web application framework |
| Concrete ML | FHE-based machine learning |
| Scikit-learn | Data preprocessing and ML utilities |
| Logistic Regression | ADHD classification model |
| HTML/CSS/JavaScript | Frontend user interface |
| Joblib | Model serialization |
| Pandas & NumPy | Data processing |

## Dataset Information

The project uses a structured ADHD behavioral dataset containing demographic, behavioral, and medical attributes.

### Features

- Age
- Gender
- Education Stage
- Inattention Score
- Hyperactivity Score
- Impulsivity Score
- Symptom Sum
- Daydreaming
- Rejection Sensitive Dysphoria (RSD)
- Sleep Hours
- Screen Time Hours
- Comorbid Anxiety
- Comorbid Depression
- Family History of ADHD
- Medication Status
- School Support
- Academic Score

### Target Variable

- `0` → No ADHD
- `1` → ADHD

## Data Preprocessing

The following preprocessing techniques were applied:

- Label Encoding for categorical features
- Standard Scaling for numerical normalization
- Feature extraction and target separation
- Training and testing dataset split

## Machine Learning Model

**Model:** Logistic Regression  
**Library:** `concrete.ml.sklearn.LogisticRegression`

The model was selected because it provides:

- Efficient binary classification
- Fast computation suitable for FHE
- Low computational overhead
- Better interpretability for healthcare applications

## Security Implementation

NeuroShield uses Fully Homomorphic Encryption to maintain data confidentiality.

### Security Pipeline

- Input data encryption
- FHE model compilation
- Encrypted inference execution
- Secure result decryption

### Security Benefits

- No exposure of patient data
- Protection against server-side data leakage
- Privacy-by-design machine learning architecture
- Suitable for secure healthcare deployments

## Application Modules

### Authentication Module

- User registration
- Secure login
- Session management
- Logout functionality

### Prediction Module

- User-friendly ADHD assessment form
- Automatic symptom score calculation
- Data preprocessing
- FHE-based prediction execution
- ADHD prediction result display

## Model Performance

| Metric | Result |
|--------|--------|
| Plain Model Accuracy | 77% |
| FHE Compilation | Successfully Compiled |

## Project Structure

```
NeuroShield/
│
├── app.py                      # Flask application
├── model/
│   ├── model_training.py       # Training and FHE compilation
│   └── model_runtime.py        # Secure prediction execution
│
├── templates/
│   ├── login.html              # User login page
│   ├── register.html           # User registration page
│   ├── index.html              # ADHD prediction form
│   └── result.html             # Prediction output page
│
├── static/                     # Images and CSS assets
├── data/
│   └── adhd.csv                # ADHD dataset
│
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/NeuroShield.git
cd NeuroShield
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

## Future Enhancements

- Support for advanced machine learning models with FHE
- Cloud deployment with secure encrypted inference
- Integration with electronic health record systems
- Enhanced model performance and optimization
- Multi-user healthcare management dashboard

## Conclusion

NeuroShield demonstrates a practical implementation of privacy-preserving artificial intelligence in healthcare. By combining Flask, Concrete ML, and Fully Homomorphic Encryption, the system enables secure ADHD prediction while ensuring that sensitive medical information remains protected during computation.

This project showcases how cryptographic techniques can be integrated with modern machine learning to develop trustworthy and secure AI applications for real-world healthcare scenarios.


---

