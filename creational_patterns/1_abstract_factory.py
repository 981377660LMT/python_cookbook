# The idea is to abstract the creation of objects depending on business
# logic, platform choice, etc.
import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


class PetShop:
    def __init__(self, animal_factory):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f"your {pet}")
        return pet


def random_animal_factory(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)


if __name__ == '__main__':
    shop = PetShop(random_animal_factory)
    shop.buy_pet('abc')

