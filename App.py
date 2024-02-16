from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/erreur')
def erreur():
    return render_template('erreur.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Vérifier les informations de connexion
    if email == 'gnziengi@gmail.com' and password == '@Kimbila99':
       return render_template('dashboard.html')

    else:
        return  render_template('erreur.html')
    from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status')
def status():
    response = {
        'status': 'OK',
        'code' : 200
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port="5000")


    
