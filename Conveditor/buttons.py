"""

BUTTONS FOR Conveditor - Видео и Аудио Редактор (Telegram Bot) - https://t.me/ConveditorMainBot (@ConveditorMainBot)
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
    "RU": {"Видеоредактор 🎬": "videored", "Аудиоредактор 🎧": "audiored"},
    "EN": {"Video editor 🎬": "videored", "Audio editor 🎧": "audiored"}
};

backbtn: dict = {
    "RU": "⬅️ Назад",
    "EN": "⬅️ Back"
};

Second_Step_Buttons: dict = {
    "videored": {"RU": {"Объединение видеофайлов (Склейка)": "concatenate",
                        "Обрезать видео": "cut",
                        "Удалить аудио из видео": "rmaudio",
                        "Извлечь аудио из видео (mp3)": "getaudio",
                        "Изменить громкость видео": "changevolume",
                        "Добавить аудиодорожку к видео": "addaudio",
                        "Извлечение кадров из видео": "getframes"},
                "EN": {"Concatenate videos": "concatenate",
                        "Cut video": "cut",
                        "Delete audio in video": "rmaudio",
                        "Get audio from video (mp3)": "getaudio",
                        "Change video volume": "changevolume",
                        "Add audio to video": "addaudio",
                        "Extracting frames from a video": "getframes"}
    },
    "audiored": {"RU": {"Объединение аудиофайлов (Склейка)": "concatenate_audio",
                        "Обрезать аудио": "cut_audio",
                        "Изменить громкость аудио": "changevolume_audio"},
                "EN": {"Concatenate audiofiles": "concatenate_audio",
                        "Cut audio": "cut_audio",
                        "Change audio volume": "changevolume_audio"}
    }
};

Go_To_Menu: dict = {
    "RU": "Перейти к меню ➡️",
    "EN": "Go to menu ➡️"
};

Continue: dict = {
    "RU": "Продолжить",
    "EN": "Continue"
};

admin_menu_buttons: dict = {
    "RU": {"Добавить канал": "add_channel",
           "Удалить канал": "remove_channel",
           "Провести рассылку": "make_a_promotional_mailing"},
    "EN": {"Add channel": "add_channel",
           "Remove channel": "remove_channel",
           "Make a promotional mailing": "make_a_promotional_mailing"}
};
