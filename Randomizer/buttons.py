"""

BUTTONS FOR Randomizer - Рандомайзер (Telegram Bot)
https://t.me/RandomizerMainBot (@RandomizerMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<< DESCRIPTION FOR TRANSLATORS >>

--- To add new language you need add it to «languages» dictionary

WARNING: IF AT LEAST ONE OF THE DICTIONARIES (files messages.py, buttons.py)
DOES NOT CONTAIN THE LANGUAGE YOU ADDED,
AN ERROR WILL OCCUR THERE.

--- How does it work?
The program takes the language code from the «languages» dictionary and accesses each of the
other dictionaries using this code. It is important to use a single code that is specified
in «languages» dictionary.

THE LANGUAGE CODE MUST CONSIST OF ONLY 2 CHARACTERS

callback_data must be the same for all languages and must not have any changes.

You can see the filling format below.

"""


""" 
struct:
    language_name (str): language_key (str)
"""
languages: dict = {
    "🇷🇺 Russian": "RU",
    "🇺🇸 English": "EN"
};

"""
struct for all the following dictionaries:
    language_key (str): any_info
"""

mainmenubut = {
    "RU": {
        "Рандомайзер стран 🌏": "country_rand",
        "Рандомайзер профессий 💼": "work_rand",
        "Рандомайзер действий 🕺🏻": "actions_rand",
        "Рандомайзер слов 🔤": "word_rand",
        "Рандомайзер чисел 🔢": "num_rand",
        "Рандомайзер статей на Википедии 🌐": "wiki_rand"
    },
    "EN": {
        "Country randomizer 🌏": "country_rand",
        "Professions randomizer 💼": "work_rand",
        "Actions randomizer 🕺🏻": "actions_rand",
        "Word randomizer 🔤": "word_rand",
        "Numbers randomizer 🔢": "num_rand",
        "Wikipedia article randomizer 🌐": "wiki_rand"
    }
};

second_menu_buttons: dict = {
    "RU": {
        "country_rand": ("Случайная страна 🌏", "take_country"),
        "work_rand": ("Случайная профессия 💼", "take_work"),
        "actions_rand": ("Случайное действие 🕺🏻", "take_action"),
        "word_rand": ("Случайное слово 🔤", "take_word"),
        "num_rand": ("Случайное число 🔢", "take_num"),
        "wiki_rand": ("Случайная статья 🌐", "take_article")
    },
    "EN": {
        "country_rand": ("Random Country 🌏", "take_country"),
        "work_rand": ("Random Professions 💼", "take_work"),
        "actions_rand": ("Random Action 🕺🏻", "take_action"),
        "word_rand": ("Random Word 🔤", "take_word"),
        "num_rand": ("Random Number 🔢", "take_num"),
        "wiki_rand": ("Random article 🌐", "take_article")
    }
};

randomizer_buttons: dict = {
    "RU": {
        "take_country": "Еще одна страна 🌏",
        "take_work": "Еще одна профессия 💼",
        "take_action": "Еще одно действие 🕺🏻",
        "take_word": "Еще одно слово 🔤",
        "take_number": "Еще одно число 🔢",
        "take_article": "Еще одна статья 🌐"
    },
    "EN": {
        "take_country": "Another country 🌏",
        "take_work": "Another profession 💼",
        "take_action": "Another action 🕺🏻",
        "take_word": "Another word 🔤",
        "take_number": "Another number 🔢",
        "take_article": "Another article 🌐"
    }
};

to_the_start_menu: dict = {
    "RU": "⬅️ К начальному меню",
    "EN": "⬅️ To the start menu"
};

take_number_button: dict = {
    "RU": "Еще одно число 🔢",
    "EN": "Another number 🔢"
};

take_word_button: dict = {
    "RU": "Еще одно слово 🔤",
    "EN": "Another word 🔤"
};

backbtn: dict = {
    "RU": "⬅️ Назад",
    "EN": "⬅️ Back"
};

admin_menu_buttons: dict = {
    "RU": {"Добавить канал": "add_channel",
           "Удалить канал": "remove_channel",
           "Провести рассылку": "make_a_promotional_mailing"},
    "EN": {"Add channel": "add_channel",
           "Remove channel": "remove_channel",
           "Make a promotional mailing": "make_a_promotional_mailing"}
};

Continue: dict = {
    "RU": "Продолжить",
    "EN": "Continue"
};

Go_To_Menu: dict = {
    "RU": "Перейти к меню ➡️",
    "EN": "Go to menu ➡️"
};
