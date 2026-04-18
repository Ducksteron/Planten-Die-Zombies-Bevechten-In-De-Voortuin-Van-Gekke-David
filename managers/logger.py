from datetime import datetime



def log_action(name: str, username: str) -> None:
    writen_line = "User ("+ username + ") did: " + name + " at: " + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + "\n" + "\n"
    append_to_log(writen_line)



def read(file_name = "log.txt") -> list:
    lines = []
    with open(file_name, mode="r") as file_acc:
        lines = file_acc.readlines()
    return lines

def append_to_log(message: str, file_name = "log.txt"):
    with open(file_name, mode="a") as file_acc:
        file_acc.write(message)