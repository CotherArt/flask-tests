from flask import Flask, render_template, request, flash
from insert import insert_user

app=Flask(__name__)
app.config['SECRET_KEY'] = 'R4NokxMSLaC1ZvS47zMxME638QRLDHgp3QKv6KVK6I1mNioNcv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        user = request.form['tbUser']
        password = request.form['tbPassword']
        insert_user(user, password)
        flash('Login succesfull!')

    return render_template('login.html')

if __name__ == '__main__':
    # To be accesible on the network, change host=your_local_ip
    app.run(debug=True, port=5000, host='127.0.0.1')