from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()

        # salvesta
        existing_data = []
        if os.path.exists('andmed.json'):
            with open('andmed.json', 'r', encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []

        existing_data.append(data)
        with open('andmed.json', 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

        return redirect(url_for('index'))  # pärast salvestamist tagasi lehele

    return render_template('trennileht.html')


if __name__ == '__main__':
    app.run(debug=True)

