from Bot import AddBot, ExitBot, SearchBot

choice = {
    'add': AddBot(),
    'search': SearchBot(),
    'exit': ExitBot(),
}


class BotFactory:
    @staticmethod
    def create(action):
        if action in choice:
            return choice[action]
        else:
            return None


if __name__ == "__main__":
    bot = BotFactory.create('search')
    bot.handle()

