from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html', home=True)

@app.route("/products")
def products():
    return render_template('backbone-products.html')

if __name__ == "__main__":
    app.run(debug=True)