"""

messages
Searcher - Поиск по IP/Номеру телефона (Telegram Bot)
https://t.me/SearcherMainBot (@SearcherMainBot)
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
    "RU": "<b>Searcher - Поиск по IP/Номеру телефона (Telegram Bot): @SearcherMainBot</b>\n\n"
          "<code>Вся информация, используемая ботом, взята из открытых источников.</code>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>Searcher - Поиск по IP/Номеру телефона (Telegram Bot): @SearcherMainBot</b>\n\n"
          "<code>All information used by the bot is taken from public sources.</code>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nЭто Searcher. Здесь вы можете получить всю доступную информацию по IP-адресу и номеру телефона. "
                                  "Выберите то, что вам нужно:</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nThis is a Searcher. Here you can get all the available information by IP address and phone number. "
                                   "Choose what you need:</b>")
};

take_info_step: dict = {
    "take_ip": {"RU": "<b>Отправьте IP-адрес, по которому надо выполнить поиск.</b>\n<i>Пример: 192.168.0.1</i>",
                "EN": "<b>Send the IP address to search for.</b>\n<i>For example: 192.168.0.1</i>"},
    "take_tel": {"RU": "<b>Отправьте телефон, по которому надо выполнить поиск.</b>\n<i>Пример: +71234567890</i>",
                 "EN": "<b>Send the phone number you want to search on.</b>\n<i>For example: +71234567890</i>"}
};

ip_info_messages: dict = {
    "RU": "<b>IP-адрес: </b><code>{}</code>\n"
          "<b>Город: </b><code>{}</code>\n"
          "<b>Регион: </b><code>{}</code>\n"
          "<b>Страна: </b><code>{}</code>\n"
          "<b>Провайдер: </b><code>{}</code>\n"
          "<b>Организация: </b><code>{}</code>\n"
          "<b>Почтовый индекс: </b><code>{}</code>\n"
          "<b>Часовой пояс: </b><code>{}</code>\n"
          "<b>Широта: </b><code>{}</code>\n"
          "<b>Долгота: </b><code>{}</code>",
    "EN": "<b>IP-adress: </b><code>{}</code>\n"
          "<b>City: </b><code>{}</code>\n"
          "<b>Region: </b><code>{}</code>\n"
          "<b>Country: </b><code>{}</code>\n"
          "<b>Provider: </b><code>{}</code>\n"
          "<b>Organization: </b><code>{}</code>\n"
          "<b>Postal code: </b><code>{}</code>\n"
          "<b>Timezone: </b><code>{}</code>\n"
          "<b>Latitude: </b><code>{}</code>\n"
          "<b>Longitude: </b><code>{}</code>"
};

unknown_phone: dict = {
    "RU": "Неизвестно",
    "EN": "Unknown"
};

Phone_Info_Messages: dict = {
    "RU": "<b>Номер телефона: </b><code>{}</code>\n"
          "<b>Провайдер: </b><code>{}</code>\n"
          "<b>Регион: </b><code>{}</code>\n"
          "<b>Часовой пояс: </b><code>{}</code>",
    "EN": "<b>Phone number: </b><code>{}</code>\n"
          "<b>Carrier: </b><code>{}</code>\n"
          "<b>Region: </b><code>{}</code>\n"
          "<b>Timezone: </b><code>{}</code>"
};

ip_not_found: dict = {
    "RU": "<b>IP не найден 😔</b>",
    "EN": "<b>IP not found 😔</b>"
};

phone_not_found: dict = {
    "RU": "<b>Номер телефона не найден 😔</b>",
    "EN": "<b>Phone not found 😔</b>"
};

Back_To_Menu: dict = {
    "RU": "<b>Вернуться к начальному меню?</b>",
    "EN": "<b>Go back to the start menu?</b>"
};

Go_To_Menu: dict = {
    "RU": "Перейти к меню ➡️",
    "EN": "Go to menu ➡️"
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
