"""

MESSAGES FOR WikiNavigator - Википедия в Телеграм (Telegram Bot)
https://t.me/WikiNavigatorMainBot (@WikiNavigatorMainBot)
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
    "RU": "<b>WikiNavigator - Википедия в Телеграм (Telegram Bot): @WikiNavigatorMainBot</b>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>WikiNavigator - Википедия в Телеграм (Telegram Bot): @WikiNavigatorMainBot</b>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nЭто WikiNavigator. "
                                  "Здесь вы можете выполнить поиск по Википедии, спарсить статью и выбрать случайную. "
                                  "Для поиска просто отправьте запрос, а для генерации случайной статьи /random</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nThis is WikiNavigator. "
                                   "Here you can search Wikipedia, sparse an article and choose a random one. "
                                   "To search just send a query, and to generate a random article /random</b>")
};

here_is_your_search_result: dict = {
    "RU": "<b>Вот что нам удалось найти по вашему запросу:</b>",
    "EN": "<b>Here's what we were able to find on your request:</b>"
};

no_result: dict = {
    "RU": "<b>По вашему запросу ничего не найдено 😔</b>",
    "EN": "<b>Nothing was found for your request 😔</b>"
};

select_article_message: dict = {
    "RU": "<b>Ваша статья: </b><code>{}</code>",
    "EN": "<b>Your article: </b><code>{}</code>"
};

random_article_message: dict = {
    "RU": "<b>Ваша случайная статья: </b><code>{}</code>",
    "EN": "<b>Your random article: </b><code>{}</code>"
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
    "RU": ['<b>Для использования бота необходимо подписаться на каналы ниже. '
           'Если вы сделали это, нажмите на кнопку "Я подписался ✅"</b>', 'Я подписался ✅'],
    "EN": ['<b>To use the bot, you need to subscribe to the channels listed below. '
           'If you have done this, click on the "I subscribed ✅" button.</b>', 'I subscribed ✅']
};