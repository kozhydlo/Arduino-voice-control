# Голосове керування за допомогою Python та Arduino

Цей проект дозволяє керувати світлодіодом на платі Arduino, використовуючи голосові команди, які розпізнаються за допомогою бібліотеки Vosk в Python. Голосові команди "Включити" та "Виключити" активують та вимикають світлодіод відповідно.

## Потрібні бібліотеки

Для запуску цього проекту, вам знадобляться наступні бібліотеки:

- Vosk: Для розпізнавання голосових команд
- PyAudio: Для роботи з аудіопотоками
- PyFirmata: Для керування Arduino через USB

Ви можете встановити ці бібліотеки за допомогою pip:

```
pip install vosk pyaudio pyfirmata

```


## Встановлення та налаштування

1. Завантажте модель Vosk для російської мови [звідси](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.tar.gz) та розпакуйте її в корінь вашого проекту.

2. Підключіть Arduino до комп'ютера та визначте правильний COM-порт в коді Arduino.

3. Запустіть Python-скрипт, що містить код для розпізнавання голосових команд. Переконайтеся, що ви вказали правильний COM-порт для Arduino.

4. Готово! Тепер ваша Arduino повинна реагувати на голосові команди "Включити" та "Виключити" для керування світлодіодом на піні 9.

## Використання

Після запуску скрипту Python та завантаження коду на Arduino, ваша система буде готова до прийому голосових команд. Прошу звернути увагу, що команда "Вийти" припиняє виконання програми.


## Автор

Автор цього проекту: [Mark Kozhydlo]

Якщо у вас є будь-які питання або пропозиції щодо цього проекту, будь ласка, зв'яжіться зі мною [markkozhydlo@gmail.com].

Всі права захищені.

# Правильне підлючення світлодіоду
## правильне підключення світлодіоду можете подивитися [тут](https://prnt.sc/-ZcCIseTFU03)

