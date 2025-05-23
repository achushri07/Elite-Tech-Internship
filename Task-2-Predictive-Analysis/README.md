# 🏏 Task 2 – Predictive Analysis using Machine Learning

This project is part of the Elite Tech Intern **Data Analytics Internship**. The goal was to build a Machine Learning model to predict outcomes based on the dataset.
This is a Flask-based web application that predicts the number of runs a cricketer might score based on various match conditions like venue, opponent, pitch type, toss decision, and more. The prediction is powered by a trained **Random Forest Regressor** model.

---

## ⚙️ Technologies Used

- **Python**
- **Flask**
- **HTML / CSS**
- **Scikit-learn**
- **Pandas / NumPy**
- **Random Forest Regressor (Sklearn)**

---


---

## 🧠 How It Works

1. The user selects match inputs via a form (format, pitch, opponent, etc.).
2. The data is processed and passed to a trained Random Forest model.
3. The model returns a predicted number of runs.
4. The prediction is displayed on the same page in real time.

---

## 📊 Model Training (Summary)

- Dataset: 500+ synthetic yet realistic player records
- Features used:
  - Match Format, Venue, Opposition, Pitch Type, Toss Decision, Innings, Match Time
- Target: Runs scored
- Model: `RandomForestRegressor(n_estimators=100, random_state=42)`
- Evaluation: Trained for variability (low runs on green pitches, high on flat pitches, etc.)

---

## 🛠️ Setup Instructions

# Clone the repository
git clone https://github.com/yourusername/cricket-run-predictor.git
cd cricket-run-predictor

# Create virtual environment
python -m venv env
source env/bin/activate     # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

---

## ✅ Status

✅ Task completed and ready for evaluation.
