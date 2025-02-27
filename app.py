from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Пример ASCII-арта
ascii_art = """
▓▓▓▓▓▓▓▓▓▓▓▓████████████
▓▓▓▓▓▓▓▓███████▒▒▒▒▒▒▒▒▒███
▓▓▓▓▓█████████▒▒▒▒▒▒▒▒▒▒▒▒████
▓▓▓▓██▒███▒▒▒▒██▒▒▒▒▒▒▒▒▒█▒▒▒██
▓▓▓█▒▒▒█▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒██
▓▓█▒▒▒█▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
▓█▒▒▒██▒▒▒▒▒▒▒▒▒█████████▒▒▒▒▒▒▒▒█
██▒▒▒█▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒█
█▒▒▒██▒▒▒▒▒▒▒▒████████████▒▒▒▒▒▒▒▒█
█▒▒█████▒▒▒███▒▒▒███████▒▒████▒▒▒██
███████████▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒█████
█▒███████▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒████
█▒███████▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒████
▓█▒██████▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒███
▓▓█▒██▒▒██▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒██▒██
▓▓▓██▒▒▒▒▒███▒▒▒▒█████▒▒▒▒███▒▒▒█
▓▓▓▓██▒▒▒▒▒▒███████████████▒▒▒██
▓▓▓▓▓███▒▒▒▒▒▒██████████▒▒▒▒██
▓▓▓▓▓▓▓████▒▒▒█████████▒▒███
▓▓▓▓▓▓▓▓▓▓█████▒▒▒▒▒▒████

"""

# Главная страница с эффектом печати
@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ASCII-арт с эффектом печати</title>
        <style>
            body {
                background-color: black;
                color: green;
                font-family: monospace;
                white-space: pre;
            }
        </style>
    </head>
    <body>
        <pre id="ascii">{{ ascii_art }}</pre>
        <script>
            const asciiElement = document.getElementById("ascii");
            const asciiArt = `{{ ascii_art }}`;
            let index = 0;

            function typeEffect() {
                if (index < asciiArt.length) {
                    asciiElement.innerHTML += asciiArt[index];
                    index++;
                    setTimeout(typeEffect, 50); // Скорость печати (мс)
                }
            }

            typeEffect();
        </script>
    </body>
    </html>
    ''', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)
