from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            kaal = float(request.form['kaal'])
            kordused = float(request.form['kordused'])
        except:
            return render_template('avaleht.html')
    else:
        return render_template('avaleht.html')

if __name__ == '__main__':

    app.run()
