from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

app.secret_key = b'\xf2\x9a\xbb\x19\x12\xbd\xaa\xe2K\xae/V\xbaV\x11\x0f\xa2~\x99\xacU\x1a\xd1\x99\x0c\x1e\x1e[\xb3N\xd4\x8c'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Welcome')
def welcome():
    return render_template('welcome.html') #render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'Post':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/about')
def about():
    flash('Thanks for reading useless information!!!', 'info')
    return render_template('/about.html', company_name='gearmindsacademy.com')

@app.route('/add_stock' , methods=['GET' , 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']

        flash(f"added new stock ({ request.form['stock_symbol'] })", 'success')

        return redirect(url_for('list_stocks'))  #NEW!!
        
    return render_template('add_stock.html')

@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')

    
if __name__ == '__main__':
    app.run(debug=True)