"""

MESSAGES FOR Conveditor - Видео и Аудио Редактор (Telegram Bot) - https://t.me/ConveditorMainBot (@ConveditorMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

<< DESCRIPTION FOR TRANSLATORS >>

--- To add new language you need add it to «languages» dictionary (buttons.py)

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

start_msg: str = "<b>Выберите язык/Choose language:</b>";

"""
struct for all the following dictionaries:
    language_key (str): any_info
"""

lang_ch: dict = {
    "RU": ("<b>Язык выбран!</b>", "Продолжить ➡️"),
    "EN": ("<b>The language is set!</b>", "Continue ➡️")
};

information: dict = {
    "RU": "<b>Conveditor - Видео и Аудио Редактор (Telegram Bot) - @ConveditorMainBot</b>\n\n"
          "<b>Создатель:</b> @echoscomplex\n\n"
          "<b>Бот относится к проекту main</b>: @tg_main_project\n\n"
          "<b>Правообладатель:</b> @echoscode\n\n"
          "<b>Лицензия:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n"
          "<b><i>Все права сохранены.</i></b>",
    "EN": "<b>Conveditor - Видео и Аудио Редактор (Telegram Bot) - @ConveditorMainBot</b>\n\n"
          "<b>Creator:</b> @echoscomplex\n\n"
          "<b>The bot belongs to the main project</b>: @tg_main_project\n\n"
          "<b>Copyright holder:</b> @echoscode\n\n"
          "<b>License:</b> GNU GPL v2 ECHO'S DEVELOPMENT © 2023\n<b>"
          "<i>All rights reserved.</i></b>"
};

mainmenu: dict = {
    "RU": ("<b>Рад вас видеть, ", "!\n\nЭто Conveditor. Здесь вы можете отредактировать аудио или видео файлы. "
                                  "Выберите то, что вам нужно:</b>"),
    "EN": ("<b>Glad to see you, ", "!\n\nThis is a Conveditor. Here you can edit audio or video files. "
                                   "Choose what you need:</b>")
};

subscribe: dict = {
    "RU": ['<b>Для использования бота необходимо подписаться на каналы ниже. '
           'Если вы сделали это, нажмите на кнопку "Я подписался ✅"</b>', 'Я подписался ✅'],
    "EN": ['<b>To use the bot, you need to subscribe to the channels listed below. '
           'If you have done this, click on the "I subscribed ✅" button.</b>', 'I subscribed ✅']
};

Second_Menu: dict = {
    "videored": {"RU": "<b>Вы в видеоредакторе. Выберите функцию, которая вам нужна.</b>",
                 "EN": "<b>You're in a video editor. Select the function you need.</b>"},
    "audiored": {"RU": "<b>Вы в аудиоредакторе. Выберите функцию, которая вам нужна.</b>",
                 "EN": "<b>You're in a audio editor. Select the function you need.</b>"}
};

Redactor_Message: dict = {
    "concatenate": {"RU": "<b>Отправьте два видеофайла (mp4, avi), которые надо склеить. "
                          "Файлы должны быть одного разрешения во избежание появления артефактов.\n\nP.S. На данный момент боты могут работать с файлами, весом не более 20Мб\n\nДля начала, отправьте первый файл.</b>",
                    "EN": "<b>Send two video files (mp4, avi) that need to be concatenated together. "
                          "The files must be of the same resolution in order to avoid the appearance of artifacts.\n\nP.S. At the moment, bots can work with files weighing no more than 20Mb\n\nTo start send first file.</b>"},
    "cut": {"RU": "<b>Отправьте видеофайл (mp4, avi), который вам надо обрезать.</b>",
            "EN": "<b>Send the video file (mp4, avi) that you need to cut.</b>"},
    "rmaudio": {"RU": "<b>Отправьте видеофайл (mp4, avi), в котором надо удалить аудио.</b>",
                "EN": "<b>Send a video file (mp4, avi) in which you want to delete the audio.</b>"},
    "getaudio": {"RU": "<b>Отправьте видеофайл (mp4, avi), из которого надо извлечь аудио.</b>",
                 "EN": "<b>Send the video file (mp4, avi) from which you want to extract the audio.</b>"},
    "changevolume": {"RU": "<b>Отправьте видеофайл (mp4, avi), в котором надо изменить громкость.</b>",
                     "EN": "<b>Send a video file (mp4, avi) in which you need to change the volume.</b>"},
    "addaudio": {"RU": "<b>Отправьте видеофайл (mp4, avi), к которому надо добавить аудиодоржку.</b>",
                 "EN": "<b>Send a video file (mp4, avi) to which you want to add an audio track.</b>"},
    "getframes": {"RU": "<b>Отправьте видеофайл (mp4, avi), из которого надо извлечь все кадры.</b>\n\n"
                        "<i>Кадры (jpg) будут отправлены в zip-архиве.</i>",
                  "EN": "<b>Send a video file (mp4, avi) from which you need to extract all the frames.</b>\n\n"
                        "<i>The frames (jpg) will be sent in a zip archive.</i>"},
    "concatenate_audio": {"RU": "<b>Отправьте два аудиофайла (mp3), которые надо склеить.\n\n"
                                "Для начала, отправьте первый файл.</b>",
                          "EN": "<b>Send two audio files (mp3) that need to be glued together.\n\n"
                                "To start, send the first file.</b>"},
    "cut_audio": {"RU": "<b>Отправьте аудиофайл (mp3), который надо обрезать.</b>",
                  "EN": "<b>Send the audio file (mp3) to be cut.</b>"},
    "changevolume_audio": {"RU": "<b>Отправьте аудиофайл (mp3), в котором надо изменить громкость.</b>",
                           "EN": "<b>Send an audio file (mp3) in which you need to change the volume.</b>"}
};

Processing_Video: dict = {
    "RU": "<b>Обрабатываем ваше видео, подождите немного...</b>",
    "EN": "<b>Processing your video, wait a bit...</b>"
};

concatenate_messages: dict = {
    "RU": "<b>Отлично, теперь отправьте второй файл.</b>",
    "EN": "<b>Great, now send the second file</b>"
};

concatenate2_messages: dict = {
    "RU": "<b>Файлы успешно склеены и сохранены на сервере. Начало отправки...</b>",
    "EN": "<b>The files have been successfully concatenated and saved on the server. Start of sending...</b>"
};

Unknown: dict = {
    "RU": "<b>Я вас не понимаю...\nМожет, мне открыть вам меню?</b>",
    "EN": "<b>I don't understand you...\n\nMaybe I should open a menu for you?</b>"
};

unknown_error: dict = {
    "RU": "<b>Произошла неизвестная ошибка!</b>",
    "EN": "<b>An unknown error has occurred!</b>"
};

Format_Error: dict = {
    "RU": "<b>Не удалось получить файл. Он верного формата?\n\n"
          "Эта же ошибка могла возникнуть, если вы отправили файл больше 20Мб.</b>",
    "EN": "<b>The file could not be retrieved. Is it the right format?\n\n"
          "The same error could occur if you sent a file larger than 20MB.</b>"
};

Back_To_Menu: dict = {
    "RU": "<b>Вернуться к начальному меню?</b>",
    "EN": "<b>Go back to the start menu?</b>"
};

Wrong_Format_Video: dict = {
    "RU": "<b>Файл не формата mp4 или avi!</b>",
    "EN": "<b>The file is not in mp4 or avi format!</b>"
};

Wrong_Format_Audio: dict = {
    "RU": "<b>Файл не формата mp3!</b>",
    "EN": "<b>File is not in mp3 format!</b>"
};

Processing_Video: dict = {
    "RU": "<b>Обрабатываем ваше видео, подождите немного...</b>",
    "EN": "<b>Processing your video, wait a bit...</b>"
};

Processing_Audio: dict = {
    "RU": "<b>Обрабатываем ваше аудио, подождите немного...</b>",
    "EN": "<b>Processing your audio, wait a bit....</b>"
};

cut1: dict = {
    "RU": "<b>Отлично, теперь отправьте промежуток, который надо вырезать. "
          "Это должно быть два числа через пробел</b>\n\n<i>Пример: 0 10</i>",
    "EN": "<b>Great, now send the gap that needs to be cut. "
          "It should be two numbers separated by a space</b>\n\n<i>Example: 0 10</i>"
};

cut2_error: dict = {
    "RU": "<b>Вы некорректно ввели промежуток, а конкретно - вы ввели не число.</b>\n\n<i>Пример: 0 10</i>",
    "EN": "<b>You entered the interval incorrectly, and specifically - you did not enter a number.</b>\n\n"
          "<i>Example: 0 10</i>"
};

Files_Successfully_Saved: dict = {
    "RU": "<b>Файлы успешно сохранены, начало редактирования...</b>",
    "EN": "<b>The files has been saved successfully, the start of editing...</b>"
};

File_Successfully_Saved: dict = {
    "RU": "<b>Файл успешно сохранен, начало редактирования...</b>",
    "EN": "<b>The file has been saved successfully, the start of editing...</b>"
};

cut2_Start_Sending: dict = {
    "RU": "<b>Видео успешно обрезано и сохранено на сервере. Начало отправки...</b>",
    "EN": "<b>The video has been successfully cropped and saved on the server. Start of sending...</b>"
};

Send_Error: dict = {
    "RU": "<b>Бот не смог отправить итоговый файл. Возможная на то причина - вес больше 20Мб.</b>",
    "EN": "<b>The bot could not send the final file. A possible reason for this is the weight is more than 20Mb.</b>"
};

change_volume2_errors: dict = {
    0: {"RU": "<b>Вы некорректно ввели значение, а конкретно - вы ввели не число.</b>\n\n<i>Пример: 0.5</i>",
        "EN": "<b>You entered the value incorrectly, and specifically - you did not enter a number.</b>\n\n"
              "<i>Example: 0.5</i>"
        },
    1: {"RU": "<b>Вы некорректно ввели значение, а конкретно - вы ввели отрицательное число.</b>\n\n<i>Пример: 0.5</i>",
        "EN": "<b>You entered the value incorrectly, specifically, you entered a negative number.</b>\n\n"
              "<i>Example: 0.5</i>"
        }
};

change_volume2_messages: dict = {
    "RU": "<b>Громкость видео успешно изменена до {} и итоговый файл сохранен на сервере. Начало отправки...</b>",
    "EN": "<b>The video volume has been successfully changed to {} and the final file is saved on the server. "
          "Start of sending...</b>"
};

cut_audio2_errors: dict = {
    "RU": "<b>Вы некорректно ввели промежуток, а конкретно - вы ввели не число.</b>\n\n<i>Пример: 0 10</i>",
    "EN": "<b>You entered the interval incorrectly, "
          "and specifically - you did not enter a number.</b>\n\n<i>Example: 0 10</i>"
};

cut_audio2_messages: dict = {
    "RU": "<b>Аудио успешно обрезано и сохранено на сервере. Начало отправки...</b>",
    "EN": "<b>The audio has been successfully cropped and saved on the server. Start of sending...</b>"
};

change_volume2_audio_messages: dict = {
    "RU": "<b>Громкость аудио успешно изменена до {} и итоговый файл сохранен на сервере. Начало отправки...</b>",
    "EN": "<b>The video volume has been successfully changed to {} and the final file is saved on the server. "
          "Start of sending...</b>"
};

del_au_messages: dict = {
    "RU": "<b>Аудио успешно удалено и итоговый файл сохранен на сервере. Начало отправки...</b>",
    "EN": "<b>The audio was successfully deleted and video has saved on the server. Start of sending...</b>"
};

get_au_messages: dict = {
    "RU": "<b>Аудио успешно извлечено и сохранено на сервере. Начало отправки...</b>",
    "EN": "<b>The audio has been successfully extracted and saved on the server. Start of sending...</b>"
};

change_volume_messages: dict = {
    "RU": "<b>Отлично, теперь отправьте значение, на которое надо изменить громкость. "
          "Изначально выставляется громкость звука 1, соответственно, вам надо написать коэффициент "
          "на который будет произведено уменьшение или увеличение звука "
          "(Если вы напишете 0.1, то громкость будет уменьшена в 10 раз).</b>\n\n<i>Пример: 0.5</i>",
    "EN": "<b>Great, now send the value to which you want to change the volume. "
          "Initially, the sound volume is set to 1, respectively, "
          "you need to write the coefficient by which the sound will be reduced or increased "
          "(If you write 0.1, the volume will be reduced 10 times).</b>\n\n<i>Example: 0.5</i>",
};

add_audio_messages: dict = {
    "RU": "<b>Отлично, теперь отправьте аудиофайл, который нужно прикрепить к видео (mp3).</b>",
    "EN": "<b>Great, now send the audio file you want to attach to the video (mp3).</b>"
};

img_get_messages: dict = {
    "RU": "<b>Кадры успешно извлечены и сохранены в архив на сервере. Начало отправки...</b>",
    "EN": "<b>The frames have been successfully extracted and archived on the server. Start of sending...</b>"
};

add_audio2_messages: dict = {
    "RU": "<b>Видео и аудио успешно склеены и сохранены на сервере. Начало отправки...</b>",
    "EN": "<b>Video and audio have been successfully concatenated and saved on the server. Start of sending...</b>"
};

concatenate_audio_messages: dict = {
    "RU": "<b>Отлично, теперь отправьте второй аудиофайл, который будет учавствовать в склейке (mp3).</b>",
    "EN": "<b>Great, now send the audio file that will participate in the concatenate (mp3).</b>"
};

concatenate_audio2_messages: dict = {
    "RU": "<b>Аудио успешно склеены и сохранены на сервере. Начало отправки...</b>",
    "EN": "<b>Audio have been successfully concatenated and saved on the server. Start of sending...</b>"
};

cut_audio_messages: dict = {
    "RU": "<b>Отлично, отправьте промежуток, который надо вырезать, через пробел.</b>\n\n<i>Пример: 0 15</i>",
    "EN": "<b>Great, send the gap that needs to be cut, separated by a space.</b>\n\n<i>Example: 0 15</i>"
};

change_volume_audio_messages: dict = {
    "RU": "<b>Отлично, теперь отправьте значение, на которое надо изменить громкость. "
          "Изначально выставляется громкость звука 1, соответственно, вам надо написать коэффициент "
          "на который будет произведено уменьшение или увеличение звука "
          "(Если вы напишете 0.1, то громкость будет уменьшена в 10 раз).</b>\n\n<i>Пример: 0.5</i>",
    "EN": "<b>Great, now send the value to which you want to change the volume. "
          "Initially, the sound volume is set to 1, respectively, "
          "you need to write the coefficient by which the sound will be reduced or increased "
          "(If you write 0.1, the volume will be reduced 10 times).</b>\n\n<i>Example: 0.5</i>"
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
