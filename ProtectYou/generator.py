"""

GENERATOR Function for Protect You
(https://t.me/ProtectYouMainBot (@ProtectYouMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)



<<< DESCRIPTION FOR DEVELOPERS >>>

"""


""" IMPORTS """
from random import choice;
from languages import Languages;



""" MAIN CLASS """
class Generator:
    def __init__ (self) -> None:
        pass;


    @staticmethod
    def password (password_language: str, level: int, length: int) -> str:
        chars = Languages[password_language][level];    # take chars
        password = "";    # init variable

        # create password
        for _ in range(length):
            password += choice(chars);
        return password;    # give password to user
