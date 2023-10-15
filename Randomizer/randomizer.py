"""

RANDOMIZER FOR Randomizer bot (https://t.me/RandomizerMainBot (@RandomizerMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

"""


""" IMPORTS """
from random import choice, randint;
import csv;
from actions import Actions_Solo, language_index;


""" CLASS RANDOMIZER """
class Randomizer:

    def __init__(self, language: str):
        self.__language: str = language.lower();

    """ RANDOM COUNTRY """
    def country (self) -> str:
        results: list = [];
        reader = csv.DictReader(open("_countries.csv", encoding="utf-8"), delimiter=",");
        for row in reader:
            results.append(row[f"title_{self.__language}"]);
        country: str = choice(results);
        return country;

    """ RANDOM PROFESSION """
    def profession (self) -> str:
        results: list = [];
        reader = csv.DictReader(open(f"occupations_{self.__language}.csv", encoding="utf-8"), delimiter=",");
        for row in reader:
            results.append((row["occupation"]));
        profession: str = choice(results);
        return profession;

    """ RANDOM ACTION """
    def action (self) -> str:
        actions = [];
        for act in Actions_Solo.items():
            actions.append(act[language_index[self.__language]]);
        action = choice(actions);
        return action;

    """ RANDOM WORD """
    @staticmethod
    def word (text: str) -> str:
        table = text.split(" ");
        element = choice(table);
        return element;

    """ RANDOM NUMBER """
    @staticmethod
    def number (start_num: int, end_num: int) -> int:
        number: int = randint(start_num, end_num);
        return number;