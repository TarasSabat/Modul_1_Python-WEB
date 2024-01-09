from Bot import AddBot, ExitBot, SearchBot


if __name__ == "__main__":
    choice = {
        'add': AddBot(),
        'search': SearchBot(),
        'exit': ExitBot(),
    }

    action = input("Choose an action: ")

    while True:
        if action in choice:
            choice[action].handle()
        else:
            print("Incorrect action!")
