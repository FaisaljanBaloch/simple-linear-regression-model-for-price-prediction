from flask import Flask
from flask import render_template, request, redirect, url_for, flash

# import linear regression model
from models.linear_regression import LinearRegression

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you will definately guess me'
model = LinearRegression() # create instance of linear model

@app.route('/')
def index():
	""" Render the index view """
	return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_price():
	if request.method == 'POST':
		size_of_house = int(request.form['size_of_house'])
		predicted_price = model.predict(size_of_house)
		flash(f'Size of house: {size_of_house} Predicted price: {predicted_price}')
		return redirect(url_for('index'))

	else:
		flash('Error: Invalid request')
		return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)