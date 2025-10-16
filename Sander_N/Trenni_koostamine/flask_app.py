from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('trennileht.html')

@app.route('/', methods=['POST'])
def save_results():
    data = request.form.to_dict()

    # Kirjuta kõik väljad faili
    with open('tulemus.txt', 'w', encoding='utf-8') as f:
        f.write("TREENINGU TULEMUSED:\n\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

    return "<h2>Tulemus salvestatud faili 'tulemus.txt'!</h2><br><a href='/'>Tagasi</a>"

if __name__ == '__main__':
    app.run(debug=True)



