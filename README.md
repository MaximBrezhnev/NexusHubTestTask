Для запуска задач необходимо, чтобы на устройстве был установлен Python

Перед запуском задач необходимо:
1. Клонировать репозиторий
```
git clone git@github.com:MaximBrezhnev/NexusHubTestTask.git
```
или следующий вариант, если не настроены/нет желания настраивать ключи SSH
```
git clone https://github.com/MaximBrezhnev/NexusHubTestTask.git
```
2. Перейти в основную директорию проекта:
```
cd NexusHubTestTask
```

3. Создать и активировать виртуальное окружение virutalenv (приведен пример для Linux/MacOS):
```
python3 -m venv .venv
source .venv/bin/activate
```
4. Установить зависимости из файла `requirements.txt` командой 
```
pip install -r requirements.txt
```

Задача 1:

Примечание: ввиду отсутствия платной подписки использовал Groq вместо OpenAI, т.к. 
посчитал это более наглядным, чем мокать доступ к недоступному API

1. По аналогии с `task1/.env.example` создайте файл `task1/.env`, добавив туда свой ключ от API Groq (https://console.groq.com/keys)
2. Запустите задачу, находясь в основной директории проекта:
```
uvicorn task1.main:app --reload,
```

Задача 2:
1. По аналогии с `task2/.env.example` создайте файл `task2/.env`, добавив туда данные своего аккаунта в Telegram и
чат для отслеживания (можно добавить через username без @ или предав непосредственно числовой id чата)
2. Запустите задачу с помощью команды 
```
python -m task2.main
```
