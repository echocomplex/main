"""

MESSAGES FOR ChatGPT Telegram bot
(https://t.me/ChatGPTTGMainBot (@ChatGPTTGMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)



<< DESCRIPTION FOR TRANSLATORS >>

--- To add new language you need add it to «languages» dictionary (buttons.py)

WARNING: IF AT LEAST ONE OF THE DICTIONARIES (files: messages.py, buttons.py)
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


start_msg: str = "<b>Choose language/Выберите язык</b>";


"""
struct for all the following dictionaries:
    language_key (str): any_info
"""
lang_ch: dict = {
    "RU": ("<b>Язык выбран!</b>", "Продолжить ➡️"),
    "EN": ("<b>The language is set!</b>", "Continue ➡️")
};

information: dict = {
    "RU": "<b>ChatGPT Telegram (Telegram Bot): @ChatGPTTGMainBot</b>\n\n"
          "<code>Данный бот использует технологию ChatGPT</code>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>ChatGPT Telegram (Telegram Bot): @ChatGPTTGMainBot</b>\n\n"
          "<code>This bot uses ChatGPT technology</code>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nПросто отправьте ваш запрос в сообщении и ChatGPT вам на него ответит. "
                                  "Если требуется обработка медиа, то прилагайте ссылку к файлу в запросе.</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nJust send your request in a message and ChatGPT will answer it to you. "
                                   "If media processing is required, then attach a link to the file in the request.</b>")
};

generate: dict = {
    "RU": "<b>ChatGPT обрабатывает ваш запрос, подождите немного...</b>",
    "ENG": "<b>ChatGPT is processing your request, wait a bit...</b>"
};

error: dict = {
    "RU": "<b>Произошла неизвестная ошибка. Попробуйте еще раз.</b>",
    "ENG": "<b>An unknown error has occurred. Please try again.</b>"
};
