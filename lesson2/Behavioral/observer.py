import datetime
import json


class Event:
    observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self.observers:
            observer(event, data)

        date = data + 20
        print(date)


def logger (event, data):
    print(event, data)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'a') as f:
            f.write(json.dumps({
                'event': event,
                'data': data,
                'time': datetime.datetime.now().isoformat()
            }) + '\n')


if __name__ == "__main__":
    event = Event()
    event.register_observer(logger)
    event.register_observer(FileLogger('log'))
    event.notify('ping', 20)
    event.notify('ping', 3)
    event.notify('ping', 10)
    event.notify('pong', 20)
    event.unregister_observer(logger)
    event.notify('ping', 1000)

