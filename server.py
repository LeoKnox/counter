from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def create_user():
    print("Got Post Info")
    if 'usercount' in session:
        session['usercount'] += 1
    else:
        session['usercount'] = 1
    #return redirect('/show')
    return render_template('count.html')

@app.route('/destroy')
def remove_user():
    session['usercount'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True) 
