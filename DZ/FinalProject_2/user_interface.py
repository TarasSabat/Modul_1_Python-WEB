from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display_menu(self, commands):
        pass

    @abstractmethod
    def get_user_input(self, prompt):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass


class ConsoleInterface(UserInterface):
    def display_menu(self, commands):
        print("Available commands:")
        for command in commands:
            print(f"  - {command}")

    def get_user_input(self, prompt):
        return input(prompt)

    def display_message(self, message):
        print(message)

    def display_contacts(self, contacts):
        for contact in contacts:
            print(contact)
