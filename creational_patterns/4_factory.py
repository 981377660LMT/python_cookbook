""""
A Factory is an object for creating other objects.

*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django
For example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.
"""


from abc import ABCMeta, abstractmethod


class Localizer(metaclass=ABCMeta):
    @abstractmethod
    def localize(self, msg: str) -> str:
        pass


class GreekLocalizer(Localizer):
    """A simple localizer a la gettext"""

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> Localizer:

    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }

    return localizers[language]()


if __name__ == '__main__':
    print(get_localizer("Greek").localize("aas"))

