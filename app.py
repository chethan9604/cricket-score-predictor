 # Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'odimodel.pkl'
print(filename)
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'England':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'India':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0]
        elif batting_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0]
        elif batting_team == 'Srilanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0]
        elif batting_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0]
        elif batting_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0]
        elif batting_team == 'Newzeland':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0]
        elif batting_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0]
        elif batting_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0]
        elif batting_team == 'Ireland':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0]
        elif batting_team == 'Zimbambwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1]
    

        bowling_team = request.form['bowling-team']
        if bowling_team == 'England':
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'India':
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Pakistan':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0]
        elif bowling_team == 'Srilanka':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0]
        elif bowling_team == 'Australia':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0]
        elif bowling_team == 'South Africa':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0]
        elif bowling_team == 'Newzeland':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0]
        elif bowling_team == 'Bangladesh':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0]
        elif bowling_team == 'West Indies':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0]
        elif bowling_team == 'Ireland':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0]
        elif bowling_team == 'Zimbambwe':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1]
            
            
        overs = float(request.form['overs'])
        runs = int(request.form['score'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_last5'])
        wickets_in_prev_5 = int(request.form['wickets_in_last5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == '__main__':
	app.run(debug=True)