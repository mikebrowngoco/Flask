from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name=None)

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['name']
    return render_template('index.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
