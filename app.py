from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('pipe.pkl', 'rb') as model_file:
    pipe = pickle.load(model_file)

# Define teams and cities
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

@app.route('/')
def home():
    return render_template('index.html', teams=teams, cities=cities)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        selected_city = request.form['selected_city']
        target = float(request.form['target'])
        score = float(request.form['score'])
        overs = float(request.form['overs'])
        wickets_out = float(request.form['wickets_out'])

        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets = 10 - wickets_out
        crr = score / overs
        rrr = (runs_left * 6) / balls_left

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        return render_template('result.html', batting_team=batting_team, win=round(win * 100),
                               bowling_team=bowling_team, loss=round(loss * 100))
    except Exception as e:
        return render_template('error.html', error_message=str(e))
