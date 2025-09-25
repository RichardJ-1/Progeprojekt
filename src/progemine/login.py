from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form["logi_sisse_nupp"] == "Logi sisse":
            try:
                kasutajanimi = request.form(["nimi"])
                parool = request.form(["parool"])
                return render_template('sisselogitud.html')
            except:
                return render_template('login_ekraan.html')
            
        elif request.form["uus_kasutaja_nupp"] == "Uus kasutaja":
            return render_template('uus_kasutaja.html')

if __name__ == '__main__':
    app.run()