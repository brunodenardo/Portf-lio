from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/experiencias')
def experiencias():
    return render_template('curiosidades.html')

@app.route('/trabalhos')
def trabalhos():
    return render_template('trabalhos.html')

if __name__ == '__main__':
    app.run(debug = True)