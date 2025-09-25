from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            km = float(request.form['km'])
            kutus = float(request.form['kutus'])
            vastus = kutus / km *100
            return render_template('avaleht.html', vastus = str(vastus), km = str(km), kutus = str(kutus))
        except:
            return render_template('avaleht.html')
    else:
        return render_template('avaleht.html')

if __name__ == '__main__':
    app.run()