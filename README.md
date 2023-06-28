
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

## The workflow

It's a common practice in the industry to 
create a new git branch for each feature.

### 0. Making sure you're on a right git branch

To check the current branch, run:
```
git branch
```

It should show the "main" branch.

If it's on some other branch, you can switch to the main branch by running:
```
git checkout main
```

Also, you need to make sure the main branch is up to date with the remote repository.

To do that, run:
```
git pull
```

It will pull the latest changes from the remote repository.

Once that's all covered, you can create a new branch.

### 1. Creating a new branch

Creating a new branch:
```
git checkout -b <branch_name>
```

(Branch name can be a short description of the feature ie. "add-pushup-command")

### 2. Making changes

Once you're on the new branch, you can make changes to the code.

To save changes, you need to "commit" them.

To commit the changes, run:
```
git add . # Adds all the changes to the commit
git commit -m "Your commit message" 
```

### 3. Pushing the changes to the repository

After the feature is completed, it's pushed to the remote repository,
using the command:
```
git push
```

When pushing for the first time, you will be asked to set the upstream branch, like so:
```
git push --set-upstream origin <branch_name>
```

### 4. Create a GitHub pull request

By creating a pull request, you’re requesting a review and approving of your changes before they become final.

Add "eduardknezovic" as a reviewer.

After the pull request is approved, the changes will get merged to the main branch, and shortly after that,
the changes will be deployed to the production server.
