from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def save_workout():
    data = request.form.to_dict()
    with open('tulemus.txt', 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    return "Tulemus salvestatud!"


