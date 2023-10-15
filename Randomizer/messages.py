"""

MESSAGES FOR Randomizer - Рандомайзер (Telegram Bot)
https://t.me/RandomizerMainBot (@RandomizerMainBot)
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
    "RU": "<b>Randomizer - Рандомайзер (Telegram Bot): @RandomizerMainBot</b>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>Randomizer - Рандомайзер (Telegram Bot): @RandomizerMainBot</b>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nЭто Randomizer. "
                                  "Здесь вы можете выбрать случайную страну, профессию, действие, "
                                  "слово, число и статью на Википедии! "
                                  "Выберите то, что вам нужно:</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nThis is a Randomizer. "
                                   "Here you can choose a random country, profession, action, "
                                   "word, number and Wikipedia article! "
                                   "Choose what you need:</b>")
};

second_menu_message:  dict = {
    "RU": {
        "country_rand": "<b>Рандомайзер стран.</b>\n\n"
                        "<i>Здесь вы можете получить абсолютно случайно выбранную страну.</i>\n\n"
                        "<b>Для чего это нужно?</b>\n\n"
                        "<i>Например, если вы не знаете, в какой стране вы хотите побывать, "
                        "наш бот вам подскажет и пришлет ссылку на страницу Википедии!</i>",
        "work_rand": "<b>Рандомайзер профессий.</b>\n\n"
                     "<i>Здесь вы можете получить абсолютно случайно выбранную профессию.</i>\n\n"
                     "<b>Для чего это нужно?</b>\n\n"
                     "<i>Например, если вы не знаете, в какой сфере себя еще можно попробовать, "
                     "наш рандомайзер с таблицей, содержащей более 1400 профессий, обязательно вам подскажет.</i>",
        "actions_rand": "<b>Рандомайзер действий.</b>\n\n"
                        "<i>Здесь вы можете получить абсолютно случайно выбранное действие из списка, "
                        "в котором их больше 100.</i>\n\n"
                        "<b>Для чего это нужно?</b>\n\n"
                        "<i>Например, вам скучно и вы не знаете, чем можно заняться. "
                        "Наш бот подскажет вам это занятие!</i>",
        "word_rand": "<b>Рандомайзер слов.</b>\n\n"
                     "<i>Бот выбирает случайное слово из тех, что вы ему отправите.</i>\n\n"
                     "<b>Для чего это нужно?</b>\n\n"
                     "<i>Например, если вы не можете выбрать марку или вкус чипсов в магазине.</i>",
        "num_rand": "<b>Рандомайзер чисел.</b>\n\n"
                    "<i>Бот выбирает случайное число из диапазона, который вы зададите.</i>\n\n"
                    "<b>Для чего это нужно?</b>\n\n"
                    "<i>Например, если вам нужно сгенерировать случайный PIN-код.</i>",
        "wiki_rand": "<b>Рандомайзер статей на Википедии.</b>\n\n"
                     "<i>Бот выбирает случайную статью на крупнейшей интернет-энциклопедии</i>\n\n"
                     "<b>Для чего это нужно?</b>\n\n"
                     "<i>Это позволяет узнать интересные и познавательные факты, "
                     "о которых вы могли и не задумываться.</i>"
    },
    "EN": {
        "country_rand": "<b>Country randomizer</b>\n\n"
                        "<i>Here you can get a completely randomly selected country.</i>\n\n"
                        "<b>What is it for?</b>\n\n"
                        "<i>For example, if you don't know which country you want to visit, "
                        "then our bot will tell you about it and send you a link to the Wikipedia page!</i>",
        "work_rand": "<b>Professions randomizer.</b>\n\n"
                     "<i>Here you can get a completely randomly selected profession.</i>\n\n"
                     "<b>What is it for?</b>\n\n"
                     "<i>For example, if you do not know in which field you can still try yourself, "
                     "then our randomizer with a table containing more than 1400 professions "
                     "will definitely tell you.</i>",
        "actions_rand": "<b>Actions randomizer.</b>\n\n"
                        "<i>Here you can get an absolutely randomly selected action from a list "
                        "with more than 100 of them.</i>\n\n"
                        "<b>What is it for?</b>\n\n"
                        "<i>For example, you are bored and don't know what to do. "
                        "Our bot will tell you this action!</i>",
        "word_rand": "<b>Words randomizer.</b>\n\n"
                     "<i>The bot selects a random word from those that you send to it.</i>\n\n"
                     "<b>What is it for?</b>\n\n"
                     "<i>For example, if you can't choose the brand or taste of chips in the store.</i>",
        "num_rand": "<b>Number randomizer.</b>\n\n"
                    "<i>The bot selects a random number from the range that you specify.</i>\n\n"
                    "<b>What is it for?</b>\n\n"
                    "<i>For example, if you need to generate a random PIN.</i>",
        "wiki_rand": "<b>Wikipedia article randomizer.</b>\n\n"
                     "<i>The bot selects a random article on the largest internet encyclopedia.</i>\n\n"
                     "<b>What is it for?</b>\n\n"
                     "<i>This allows you to learn interesting and enlightening facts "
                     "that you may not have thought about</i>"
    }
};

randomizer_messages: dict = {
    "RU": {
        "take_country": ("<b>Ваша случайная страна: </b><a href='{}'>{}</a>.",
                         "<b>Выбрать еще одну страну или вернуться к начальному меню?</b>"),
        "take_work": ("<b>Ваша случайная профессия: </b><code>{}</code>.",
                      "<b>Выбрать еще одну профессию или вернуться к начальному меню?</b>"),
        "take_action": ("<b>Ваше случайное действие: </b><code>{}</code>.",
                        "<b>Выбрать еще одно действие или вернуться к начальному меню?</b>"),
        "take_word": "<b>Отправьте слова, из которых надо выбирать, через пробел.</b>\n\n"
                     "<i>Пример: «овощи фрукты ягоды»</i>",
        "take_num": "<b>Отправьте диапазон чисел, из которого надо выбирать, через пробел.</b>\n\n"
                    "<i>Пример: «-100000 100000»</i>",
        "take_article": ("<b>Ваша случайная статья: </b><a href='{}'>{}</a>.",
                         "<b>Выбрать еще одну статью или вернуться к начальному меню?</b>")
    },
    "EN": {
        "take_country": ("<b>Your random country: </b><a href='{}'>{}</a>.",
                         "<b>Choose another country or go back to the start menu?</b>"),
        "take_work": ("<b>Your random profession: </b>{}.",
                      "<b>Choose another profession or go back to the start menu?</b>"),
        "take_action": ("<b>Your random action: </b>{}.",
                        "<b>Choose another action or go back to the start menu?</b>"),
        "take_word": "<b>Send the words from which to choose, separated by a space.</b>\n\n"
                     "<i>For example: «berries fruits vegetables»</i>",
        "take_num": "<b>Send the range of numbers separated by a space.</b>\n\n"
                    "<i>For example: «-100000 100000»</i>",
        "take_article": ("<b>Your random article: </b><a href='{}'>{}</a>.",
                         "<b>Choose another article or go back to the start menu?</b>")
    }
};

take_number_messages: dict = {
    "RU": {
        0: "<b>Вы ввели информацию в неправильном формате!</b>\n\n<i>Пример: «-100000 100000»</i>",
        1: "<b>Вы ввели информацию в правильном формате, но не число!</b>\n\n<i>Пример: «-100000 100000»</i>",
        2: "<b>Ваше случайное число: </b><code>{}</code>.",
        3: "<b>Выбрать число из нового диапазона или вернуться к начальному меню?</b>"
    },
    "EN": {
        0: "<b>You entered the information in the wrong format!</b>\n\n<i>For example: «-100000 100000»</i>",
        1: "<b>You entered the information in the correct format, but not the number!</b>\n\n"
           "<i>For example: «-100000 100000»</i>",
        2: "<b>Your random number: </b><code>{}</code>.",
        3: "<b>Choose a number from a new range or go back to the start menu?</b>"
    }
};

take_word_messages: dict = {
    "RU": {
        0: "<b>Ваше случайное слово: </b><code>{}</code>.",
        1: "<b>Выбрать еще одно слово или вернуться к начальному меню?</b>"
    },
    "EN": {
        0: "<b>Your random word: </b><code>{}</code>.",
        1: "<b>Select another word or return to the start menu?</b>"
    }
};

Unknown: dict = {
    "RU": "<b>Я вас не понимаю...\nМожет, мне открыть вам меню?</b>",
    "EN": "<b>I don't understand you...\n\nMaybe I should open a menu for you?</b>"
};

admin_complete: dict = {
    "RU": "<b>Проверка на администратора пройдена! Нажмите «продолжить».</b>",
    "EN": "<b>Admin check passed! Click «continue».</b>"
};

admin_menu_messages: dict = {
    "RU": "<b>Вы в меню администратора.</b>\n\n<i>Выберите то, что вам нужно:</i>",
    "EN": "<b>You're in the admin menu.</b>\n\n<i>Select what you want:</i>"
};

chosen_func_adminmode: dict = {
    "add_channel": {"RU": "<b>Введите информацию в таком формате:</b>\n\n"
                          "chat_id----Название----Ссылка\n\nДля отмены напишите <b>«отмена»</b>",
                    "EN": "<b>Enter the information in this format:</b>\n\n"
                          "chat_id----Channel_name----Link\n\nTo cancel, write <b>«cancel»</b>."},
    "remove_channel": {"RU": "<b>Отправьте ссылку на канал, который нужно удалить.</b> "
                             "Для отмены напишите <b>«отмена»</b>",
                       "EN": "<b>Send a link to the channel you want to delete.</b> "
                             "To cancel, write <b>«cancel»</b>."},
    "make_a_promotional_mailing": {"RU": "<b>Отправьте текст рассылки.</b> Для отмены напишите <b>«отмена»</b>",
                                   "EN": "<b>Send the text of a promotional mailing.</b> "
                                         "To cancel, write <b>«cancel»</b>."}
};

Success: dict = {
    "RU": "<b>Успешно!</b>",
    "EN": "<b>Success!</b>"
};

admin_mode_error: dict = {
    "RU": "Произошла ошибка! Проверьте введенные данные!\n\nТекст ошибки: {}",
    "EN": "There has been an error! Please, check the entered data.\n\nError text: {}"
};

admin_mode_stopped: dict = {
    "RU": "<b>Отменено!</b>",
    "EN": "<b>It's cancelled!</b>"
};

Cancel_Word: dict = {
    "RU": "отмена",
    "EN": "cancel"
};

Success_promotional_mailing: dict = {
    "RU": "<b>Рассылка успешно проведена!</b>\n\n"
          "<i>Кол-во пользователей, получивших рассылку: <b>{}</b>.</i>",
    "EN": "<b>The mailing has been successfully carried out!</b>\n\n"
          "<i>Number of users who received the promotional mail: <b>{}</b>.</i>"
};

subscribe: dict = {
    "RU": ('<b>Для использования бота необходимо подписаться на каналы ниже. '
           'Если вы сделали это, нажмите на кнопку "Я подписался ✅"</b>', 'Я подписался ✅'),
    "EN": ('<b>To use the bot, you need to subscribe to the channels listed below. '
           'If you have done this, click on the "I subscribed ✅" button.</b>', 'I subscribed ✅')
};