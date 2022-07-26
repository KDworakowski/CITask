#! /usr/bin/env python
import string
import random

letters = string.ascii_letters
numbers = string.digits
punctation = string.punctuation


class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length

    def password_generator(self):
        printable = f"{letters}{numbers}{punctation}"

        printable = list(printable)
        random.shuffle(printable)

        random_password = random.choices(printable, k=self.length)
        random_password = "".join(random_password)
        return random_password
