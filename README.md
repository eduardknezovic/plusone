
# Plus One


At the time, the purpose of this project is to track 
the number of pushup user has done using Telegram Bot.

The bot is available @PlusOneRobot

It uses Telegram Bot to communicate the user and it
uses Sqlite (SQL) database. 

## Setup

It's recommended to create a virtual environment for projects, but 
it is not the necessary step.

### 0. Virtual Environment (Optional)

From this current folder, you may run these commands in terminal

```bash
python3 -m venv ./venv # Creates a virtual environment
source ./venv/bin/activate # Activates the virtual environment
```

### 1. Set up dependencies

#### Install the required libraries

```bash
pip install -r requirements.txt
```

#### Add the environment variables

In config.py file, there is the TELEGRAM_TOKEN variable.

There's the one that we're using for production, but you can
create your own telegram bot and use its token for local testing!,

Instructions available here: https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot
So, you'd just get the token and paste it in the config.py file.

In short:
- Go to telegram
- Send a message to @BotFather
- Create a new bot with /newbot command
- Copy the token and paste it in the config.py file

### 2. Running the program

From this current folder:

```bash
python main.py
```

If set up correctly, you will be able to send a 
"/pushups 10" message to bot, and it will respond accordingly.

## Unit testing

pytest is used for unit testing. It's already included in the requirements.txt file.

To run the unit tests, run this command from the current folder:

```bash
pytest test.py
```

## Database

The data is stored in the activities.db file. It's a sqlite database.

It can be opened and evaluated using DB Browser for SQLite (https://sqlitebrowser.org/)

Or, you can use the command line to open it:

```bash
sqlite3 activities.db
```

Then, you can run SQL commands to query the data.


