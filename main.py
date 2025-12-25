from flask import Flask, render_template, request

app = Flask(__name__)

projects = {
    'python': {
        'github_link': 'https://github.com/snakyou/tech-addiction-facts',
        'description': 'Консольное приложение на Python с использованием фреймворка Flask',
    },
    'telegram': {
        'github_link': 'https://github.com/snakyou/bot',
        'description': 'Телеграм бот с использованием библиотеки telebot',
    },
    'html': {
        'github_link': 'https://github.com/snakyou/calculator-main',
        'description': 'Калькулятор для расчета энергоэффективности домов',
    },
    'db': {
        'github_link': 'https://github.com/snakyou/diary-main',
        'description': 'Проект с использованием базы данных',
    }
}

# Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html', active_project=None)

# Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    # Определяем, какая кнопка была нажата
    button_clicked = None
    for key in ['python', 'telegram', 'html', 'db']:
        if request.form.get(f'button_{key}'):
            button_clicked = key
            break
    
    # Получаем данные проекта или None если кнопка не нажата
    active_project = projects.get(button_clicked) if button_clicked else None
    
    return render_template('index.html', active_project=active_project)

if __name__ == "__main__":
    app.run(debug=True)
