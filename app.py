# ============================================================
# app.py — Flask Web Server
# ============================================================
# Flask ek Python ka web framework hai — iska matlab hai ki
# hum Python se hi ek website bana sakte hain!
#
# Yeh file kaise kaam karti hai:
#   1. Flask ek local server start karta hai (aapke computer pe)
#   2. Aap browser mein http://127.0.0.1:5000 open karte ho
#   3. Browser form submit karta hai → Flask password check karta hai
#   4. Result wapas browser ko bhejta hai
# ============================================================

# flask se Flask class aur render_template + request tools import karo
# - Flask      : web app banane ke liye
# - render_template : HTML file load karne ke liye (templates/ folder se)
# - request    : browser ne jo data bheja usse padhne ke liye
from flask import Flask, render_template, request

# password_checker.py se hamara existing function import karo
# Ab hume yeh function dobara likhne ki zaroorat nahi!
from password_checker import check_password_strength

# ============================================================
# Flask App banao
# ============================================================
# __name__ Flask ko batata hai ki project ka root folder kahan hai.
app = Flask(__name__)


# ============================================================
# ROUTE: Home Page  →  "/"
# ============================================================
# @app.route decorator Flask ko batata hai:
# "Jab koi browser '/' URL pe aaye, toh yeh function chalao."
#
# methods=["GET", "POST"] ka matlab:
#   GET  = jab page pehli baar khula ho (sirf form dikhao)
#   POST = jab user ne form submit kiya ho (password check karo)
@app.route("/", methods=["GET", "POST"])
def index():
    # Shuru mein result kuch nahi hoga
    result = None

    # request.method se pata chalta hai ki browser ne GET bheja ya POST
    if request.method == "POST":
        # request.form["password"] se form ka password field padhte hain
        password = request.form["password"]

        # Apna existing function use karo — bilkul wahi jo terminal mein tha!
        score, strength, feedback = check_password_strength(password)

        # Sab kuch ek dictionary mein pack karo taaki HTML tak bhej sakein
        result = {
            "score"    : score,
            "strength" : strength,
            "feedback" : feedback,
        }

    # render_template HTML file load karta hai (templates/index.html)
    # aur result variable bhi saath mein bhejta hai
    return render_template("index.html", result=result)


# ============================================================
# SERVER START KARO
# ============================================================
# debug=True ka fayda: code badalne par server apne aap restart hoga.
# Production (live website) mein debug=False karna chahiye!
if __name__ == "__main__":
    app.run(debug=True)
