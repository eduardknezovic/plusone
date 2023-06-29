
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

## The dev workflow

### 1. The task 

First step is to determine the task/feature that will be worked on.

The list of tasks is available here: https://trello.com/b/pL5FfrOi/plusone

If there's something interesting that you'd like to do, feel free to create 
your own ticket!

When you're ready to start working on a task, assign it to yourself (if it's not assigned already) 
and move it to the "In Progress" column.

**The most important step in software development**: *Before starting coding, make sure you fully understand the requirements*

If there is something off or unclear, do not hesitate to reach out and start a discussion.

It is possible that the author of the task has missed something, or that the task is just isn't well defined.

To re-iterate: this is the most important step in the whole dev process. 

If something goes wrong here, all of the work that follows will be in vain. Not only in vain, but it might even be harmful to
the project.

### 2. Make sure your local repository is up to date

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

After you've ensured that you have the latest version of the repository, you can create a new branch.

### 3. Creating a new feature branch

It's a common practice in the industry to 
create a new git branch for each feature.

It allows for easier version control and code review. 

Very useful, even for small teams.

Creating a new branch:
```
git branch <branch_name> # Creates a new branch
git checkout <branch_name> # Switches to the new branch
```

Or, you can do it in one step:
```
git checkout -b <branch_name> # Same as the above, two commands in one!
```

(Branch name can be a short description of the feature ie. "add-pushup-command")

### 3. Making changes

Once you're on the new branch, you can make changes to the code.

To save changes, you need to "commit" them.

To commit the changes, run:
```
git add . # Adds all the changes to the commit
git commit -m "Your commit message" 
```

If you want to check whether you've successfully committed the changes, run:
```
git log
```

It will show the list of commits, with the most recent (hopefully, yours) commit on top.

### 4. Pushing the changes to the repository

After the feature is completed, it's pushed to the remote repository,
using the command:
```
git push
```

When pushing for the first time, you will be asked to set the upstream branch, like so:
```
git push --set-upstream origin <branch_name>
```

Now, your changes are available on the remote repository.

### 5. Create a GitHub pull request (code review)

By creating a pull request, you’re requesting a review and approving of your changes before they become final.

Steps:
- Go to the repository page on GitHub (https://github.com/eduardknezovic/plusone)
- Click on the "Pull requests" tab
- Click on the "New pull request" button
- Select the branch that you want to merge to the main branch (compare: <branch_name>)

Add "eduardknezovic" as a reviewer.

After the pull request is approved, the changes will get merged to the main branch, and shortly after that,
the changes will be deployed to the production server.
