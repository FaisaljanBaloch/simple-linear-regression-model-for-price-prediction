from flask import Flask
from flask import render_template

# import linear regression model
from models.linear_regression import LinearRegression

app = Flask(__name__)
model = LinearRegression()

@app.route('/')
def index():
	return render_template('index.html', result=model.predict(2500))

if __name__=='__main__':
	app.run(debug=True)