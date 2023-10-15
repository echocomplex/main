"""

MESSAGES FOR StealthMail - Анонимные письма
(Telegram Bot) (@StealthMailMainBot)
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
    "RU": "<b>StealthMail - Анонимные письма (Telegram Bot): @StealthMailMainBot</b>\n\n"
          "<code>Бот, его владелец и создатель не несут отвественности за отправленные письма с его адреса.</code>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>StealthMail - Анонимные письма (Telegram Bot): @StealthMailMainBot</b>\n\n"
          "<code>The bot, owner and creator are not responsible for emails sent from bot's address.</code>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nЭто StealthMail. Здесь вы можете отправить анонимное почтовое письмо. "
                                  "Выберите то, что вам нужно:</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nThis is StealthMail. Here you can send an anonymous email. "
                                   "Choose what you need:</b>")
};

Back_To_Menu: dict = {
    "RU": "<b>Вернуться к начальному меню или отправить еще одно письмо?</b>",
    "EN": "<b>Go back to the start menu or send another email?</b>"
};

get_address_message: dict = {
    "RU": "<b>Отправьте адрес почтового ящика получателя.</b>",
    "EN": "<b>Send the recipient's mailbox address.</b>"
};

what_is_this_message: dict = {
    "RU": "<b>Как это работает?</b>\n\nЭтот бот отправляет анонимные письма на почтовые ящики. "
          "Вам просто нужно ввести адрес почтового ящика, заголовок письма и текст письма. "
          "Получатель не узнает, кто именно отправил письмо.\n\n"
          "<b>Но почему получатель не сможет узнать, кто его отправил?</b>\n\n"
          "Этому способствуют несколько факторов:\n"
          "1. Письмо отправляется с домена maineyebot@yandex.com.\n"
          "2. На почтовом сервисе не сохраняются отправленные письма.\n"
          "3. На стороне бота не сохраняется информация об отправленных письмах.",
    "EN": "<b>How it works?</b>\n\nThis bot sends anonymous emails to mailboxes. "
          "You just need to enter the address of the mailbox, the title of the letter and the text. "
          "The recipient will not know who exactly sent the email.\n\n"
          "<b>But why can't the recipient find out who sent it?</b>\n\n"
          "Several factors contribute to this:\n"
          "1. The email is sent from the domain maineyebot@yandex.com.\n"
          "2. Sent emails are not saved on the mail service.\n"
          "3. No information about sent emails is saved on the bot side."
};


send_mail_message: dict = {
    "RU": "<b>Отправьте заголовок письма.</b>",
    "EN": "<b>Send the email title.</b>"
};

email_error: dict = {
    "RU": "<b>Адрес электронной почты указан неверно!</b>",
    "EN": "<b>The email address is incorrect!</b>"
};

send_mail2_message: dict = {
    "RU": "<b>Отправьте текст письма.</b>",
    "EN": "<b>Send the email text.</b>"
};

send_mail3_messages: dict = {
    0: {"RU": "<b>Начало отправки сообщения...</b>",
        "EN": "<b>Starting to send a message...</b>"},
    1: {0: {"RU": "<b>Сообщение успешно отправлено!</b>\n\n"
                  "<b>Заголовок:</b> <code>{}</code>\n\n"
                  "<b>Почта получателя:</b> <code>{}</code>",
            "EN": "<b>The message has been sent successfully!</b>\n\n"
                  "<b>Subject:</b> <code>{}</code>\n\n"
                  "<b>Recipient's email:</b> <code>{}</code>"
            },
        1: {"RU": "<b>Произошла ошибка! Причина ее возникновения - Сообщение похоже на спам. "
                  "Эта ошибка связана не с ботом, а с почтовым сервисом.\n\n"
                  "Попробуйте иначе составить сообщение "
                  "(обычно ошибка возникает, если все не содержит в себе существующих слов).</b>",
            "EN": "<b>An error has occurred! The reason for its occurrence is that the message looks like spam. "
                  "This error is not related to the bot, but to the mail service. "
                  "Try to compose a message differently, usually Spam Defense recognizes as "
                  "spam if the text or subject in them do not include readable words.</b>"
            },
        2: {"RU": "<b>Произошла ошибка! Возможные причины ее возникновения:\n\n"
                  "1. Неправильно указан email (формат: maineyebot@yandex.com)\n"
                  "2. Заголовок или письмо слишком длинные.</b>",
            "EN": "<b>An error has occurred! Possible causes of its occurrence:\n\n"
                  "1. The email address is specified incorrectly (format: maineyebot@yandex.com)\n"
                  "2. The title or letter is too long.</b>"
            }
        },
    2: {"RU": "<b>Вернуться к начальному меню или отправить еще одно письмо?</b>",
        "EN": "<b>Go back to the start menu or send another email?</b>"}
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
