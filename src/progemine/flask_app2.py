from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

users = {"admin": "password"}

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            form_keys = request.form.keys()

            if "logi_sisse_nupp" in form_keys:
                kasutajanimi = request.form.get("nimi", "")
                parool = request.form.get("parool", "")

                if kasutajanimi in users and users[kasutajanimi] == parool:
                    return render_template("trennileht.html")
                else:
                    return render_template("login_ekraan.html", error="Kasutajanimi või parool on valed")

            # uue kasutaja loomine
            elif "uus_kasutaja_nupp" in form_keys:
                return render_template("uus_kasutaja.html")

            # treeningu lõpetamine
            else:
                harjutused = {}
                kordused_kokku = 0
                seeriad_kokku = 0

                # harjutuste nimed
                for key, value in request.form.items():
                    if key.startswith("harjutuse_nimi_"):
                        idx = key.split("_")[-1]
                        harjutused[idx] = {"nimi": value, "seeriad": 0, "kordused": 0}

                # seeriad ja kordused
                for key, value in request.form.items():
                    if key.startswith("kordused_"):
                        parts = key.split("_")
                        if len(parts) == 3 and value.strip().isdigit():
                            ex_idx = parts[1]
                            kordused = int(value)
                            if ex_idx in harjutused:
                                harjutused[ex_idx]["kordused"] += kordused
                                harjutused[ex_idx]["seeriad"] += 1
                                kordused_kokku += kordused
                                seeriad_kokku += 1

                skoor = kordused_kokku + seeriad_kokku

                # Salvestamine
                salvestus_aeg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("tulemus.txt", "a", encoding="utf-8") as f:
                    f.write(f"--- TREENINGU TULEMUS ---\n")
                    f.write(f"Aeg: {salvestus_aeg}\n")
                    for ex_idx, data in harjutused.items():
                        f.write(f"{data['nimi']}: {data['seeriad']} seeriat, {data['kordused']} kordust\n")
                    f.write(f"Kokku: {seeriad_kokku} seeriat, {kordused_kokku} kordust\n")
                    f.write(f"Skoor: {skoor}\n")
                    f.write("-" * 30 + "\n\n")

                return render_template(
                    "Score.html",
                    harjutused=harjutused,
                    seeriad=seeriad_kokku,
                    kordused=kordused_kokku,
                    skoor=skoor
                )

        return render_template("login_ekraan.html")

    except Exception as e:
        # Kui midagi läheb valesti, logi viga ja tagasta trennileht
        print("Viga POST päringus:", e)
        return render_template("trennileht.html")


if __name__ == "__main__":
    # Thonny serveri jaoks – debug=False ja host='127.0.0.1'
    app.run(host="127.0.0.1", port=5000, debug=False)
