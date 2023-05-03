# from sys import exit as sysexit
from sys import exit as sysexit
from bot import Bot
from utils import clearScreen


def main():
    clearScreen()
    bot = Bot()
    bot.main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sysexit()
