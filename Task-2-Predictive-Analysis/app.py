from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoders
rfg_model = joblib.load("rfg_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
feature_order = joblib.load("feature_order.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from form
    input_data = {
        "Opponent": request.form['Opponent'],
        "Venue": request.form['Venue'],
        "Format": request.form['Format'],
        "Match Type": request.form['Match_Type'],
        "New Ball Faced": request.form['New_Ball_Faced'],
        "Pitch Type": request.form['Pitch_Type'],
        "Batting Position": int(request.form['Batting_Position'])
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Apply label encoding
    for column in input_df.columns:
        if column in label_encoders:
            encoder = label_encoders[column]
            input_df[column] = encoder.transform(input_df[column])

    # Reorder columns to match training
    input_df = input_df[feature_order]

    # Predict
    predicted_runs = rfg_model.predict(input_df)[0]
    predicted_runs = int(predicted_runs)

    return render_template('index.html', prediction=predicted_runs)

if __name__ == '__main__':
    app.run(debug=True)
