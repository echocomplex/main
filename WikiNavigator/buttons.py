"""

BUTTONS FOR WikiNavigator - Википедия в Телеграм (Telegram Bot)
https://t.me/WikiNavigatorMainBot (@WikiNavigatorMainBot)
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

nextbtn: dict = {
    "RU": "Вперед ➡️",
    "EN": "Next ➡️"
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

select_article_buttons: dict = {
    "RU": {
        0: "Перейти к статье ➡️",
        1: ("Отправить текст статьи в сообщении ✍", "send_page_text${}"),
        2: ("⬅️ Вернуться назад", "back_to_menu${}")
    },
    "EN": {
        0: "Go to the article ➡️",
        1: ("Send page text via message ✍", "send_page_text${}"),
        2: ("⬅️ Go back", "back_to_menu${}")
    }
};
