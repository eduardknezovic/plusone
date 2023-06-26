
from app.telegram_bot import run_telegram_bot

def main():
    print("Starting telegram bot, press Ctrl+C to stop.")
    run_telegram_bot()
    print("Ending telegram bot.")

if __name__ == '__main__':
    main()
