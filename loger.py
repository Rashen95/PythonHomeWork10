from datetime import datetime


def loger(message):
    with open("log_file.txt", "a", encoding='UTF-8') as lf:
        lf.write(f"{datetime.now().day}.{datetime.now().month} "
                 f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} "
                 f"{message}\n")
