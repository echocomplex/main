"""

BUTTONS FOR Protect You - Генератор паролей (Telegram Bot)
https://t.me/ProtectYouMainBot (@ProtectYouMainBot)
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

mainmenubut: dict = {
    "RU": {
        "Китайский 🇨🇳": "Chinese",
        "Белорусский 🇧🇾": "Belarusian",
        "Английский 🇺🇸": "English",
        "Бенгальский 🇧🇩": "Bengali",
        "Арабский 🇸🇦": "Arabic",
        "Хинди 🇮🇳": "Hindi",
        "Турецкий 🇹🇷": "Turkish",
        "Русский 🇷🇺": "Russian",
        "Японский 🇯🇵": "Japanese",
        "Немецкий 🇩🇪": "Deutsche",
        "Мультиязычный 🌐": "Multilingual"
    },
    "EN": {
        "Chinese 🇨🇳": "Chinese",
        "Belarusian 🇧🇾": "Belarusian",
        "English 🇺🇸": "English",
        "Bengali 🇧🇩": "Bengali",
        "Arabic 🇸🇦": "Arabic",
        "Hindi 🇮🇳": "Hindi",
        "Turkish 🇹🇷": "Turkish",
        "Russian 🇷🇺": "Russian",
        "Japanese 🇯🇵": "Japanese",
        "Deutsche 🇩🇪": "Deutsche",
        "Multilingual 🌐": "Multilingual"
    }
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

take_level_password_buttons: dict = {
    "RU": {
        "Простой (строчные буквы)": "1",
        "Средний (строчные и заглавные буквы)": "2",
        "Сложный (все буквы и цифры)": "3",
        "Сложнейший (все буквы, цифры и символы)": "4"
    },
    "EN": {
        "Easy (lowercase letters)": "1",
        "Medium (lowercase and uppercase letters)": "2",
        "Hard (all letters and numbers)": "3",
        "Incredible (all letters, numbers and symbols)": "4",
    }
};

Go_To_Menu: dict = {
    "RU": "Перейти к меню ➡️",
    "EN": "Go to menu ➡️"
};
