from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form["logi_sisse_nupp"] == "Logi sisse":
            try:
                #teen sõnastiku abil siia töötava logini
                #praegu lihtsalt viib local kasutaja treeningplaani
                kasutajanimi = request.form["nimi"]
                parool = request.form["parool"]
                return render_template('trennileht.html')
            except:
                return render_template('login_ekraan.html')
            
        elif request.form["uus_kasutaja_nupp"] == "Uus kasutaja":
            return render_template('uus_kasutaja.html')
        
        elif request.form["form"] == "form":
            try:
                #siia need arvutused ja numbrid skoori jaoks
                return render_template("Score.html")
            except:
                return render_template("trennileht.html")
    
    #getrequest
    return render_template('login_ekraan.html')

def save_results():
    data = request.form.to_dict()

    # Kirjuta kõik väljad faili
    with open('tulemus.txt', 'w', encoding='utf-8') as f:
        f.write("TREENINGU TULEMUSED:\n\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

    return "<h2>Tulemus salvestatud faili 'tulemus.txt'!</h2><br><a href='/'>Tagasi</a>"    


if __name__ == '__main__':
    app.run()