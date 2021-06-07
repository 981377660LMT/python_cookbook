"""
Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.


Encapsulates how a set of objects interact.
"""


class User:
    """A class whose instances want to interact with each other"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_room = ChatRoom()

    def say(self, message: str) -> None:
        self.chat_room.display_message(self, message)

    def __str__(self) -> str:
        return self.name


class ChatRoom:
    """Mediator class"""

    def display_message(self, user: User, message: str) -> None:
        print(f"[{user} says]: {message}")


if __name__ == '__main__':

    molly = User('Molly')
    molly.say("Hi Team! Meeting at 3 PM today.")

