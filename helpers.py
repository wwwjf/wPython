from colorama import init,Fore


def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message + " this is a warning ")
    else:
        print(Fore.BLUE + message)
