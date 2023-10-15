"""

MAIN FILE
Conveditor - Видео и Аудио Редактор (Telegram Bot) - https://t.me/ConveditorMainBot (@ConveditorMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<<< DESCRIPTION FOR DEVELOPERS >>>

Each text of the bot message is taken from the file messages.py,
the text of buttons and callback_data - from the file buttons.py
(they also contain instructions for translators).

Working with the database is done through database.py

Video and audio are edited using Video and Audio classes,
which are located in redactor.py

privacy.py should contain token and channel information
(detailed information in the file)

"""


print("Starting...");


""" IMPORTS """
import os;
from telebot import TeleBot;
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton;
from privacy import TOKEN, administrators;
from buttons import *;
from redactor import Video, Audio;
from messages import *;
from database import Database;



""" BOT SIGN IN """
bot = TeleBot(TOKEN);



""" start AND language COMMAND HANDLER AND FUNC """
@bot.message_handler(commands=["start", "language"])
def start (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    del database;
    # send message to user
    markup = InlineKeyboardMarkup();
    for text, callback in languages.items():
        btn = InlineKeyboardButton(text=text, callback_data=callback);
        markup.add(btn);
    bot.send_message(chat_id=chat_id, text=start_msg, parse_mode="html", reply_markup=markup);



""" adminmode COMMAND HANDLER AND FUNC """
@bot.message_handler(commands=["adminmode"])
def admin_mode (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    if (chat_id in administrators):
        markup = InlineKeyboardMarkup();
        cont = InlineKeyboardButton(text=Continue[language],
                                    callback_data="admin_menu");
        markup.add(cont);
        bot.send_message(chat_id=chat_id, text=admin_complete[language],
                         parse_mode="html", reply_markup=markup);
    else:
        # Hiding like we don't know this command exists.
        markup = InlineKeyboardMarkup();  # create markup
        menu = InlineKeyboardButton(text=Go_To_Menu[language],
                                          callback_data="mainmenu");  # create back to menu button
        markup.add(menu);  # add button to markup
        bot.send_message(chat_id=chat_id, text=Unknown[language],
                         parse_mode="html", reply_markup=markup);  # send message to user



""" INFO COMMAND HANDLER AND FUNC """
@bot.message_handler(commands=["info"])
def info (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;
    bot.send_message(chat_id=chat_id, text=information[language],
                     parse_mode="html");



""" CALLBACK HANDLER AND CALLBACK FUNC """
@bot.callback_query_handler(func=lambda call: True)
def inline (call) -> None:
    """"""
    ### USED VARIABLES ###
    # search user in database
    chat_id: int = call.message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();    # language, selected by user in /start or /language

    ### ADMIN MENU ###
    if ((call.data == "admin_menu") and (chat_id in administrators)):
        # send menu
        markup = InlineKeyboardMarkup();
        for text, callback in admin_menu_buttons[language].items():
            btn = InlineKeyboardButton(text=text, callback_data=callback);
            markup.add(btn);
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=admin_menu_messages[language], parse_mode="html", reply_markup=markup);

    ### CATCH ANY admin_menu CALLBACK ###
    elif ((call.data in admin_menu_buttons[language].values()) and (chat_id in administrators)):
        # to understand this, take a look to «if (__name__=="__main__")», dict «admin_mode_functions»
        # send message
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=chosen_func_adminmode[call.data][language],
                                    parse_mode="html");
        # and register next func
        bot.register_next_step_handler(msg, admin_menu_functions[call.data]);

    ### SET LANGUAGE ###
    elif (call.data in languages.values()):
        language = call.data;
        database.update_language(language);
        markup = InlineKeyboardMarkup();
        next = InlineKeyboardButton(text=lang_ch[language][1], callback_data="mainmenu");
        markup.add(next);
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=lang_ch[language][0], parse_mode="html", reply_markup=markup);

    ### CHECK USER SUBSCRIBE TO CHANNELS ###
    sub_status = True;  # subscribe status
    # check subscribe to channels in cycle
    channels: tuple = database.take_channels();
    # clear memory for bug avoidance and speed up
    del database;
    for channel_info in channels:
        stat = bot.get_chat_member(chat_id=channel_info[0],
                                   user_id=call.from_user.id).status;  # get user status in channel
        if (stat in ("member", "creator", "administrator")):  # if user subscribed
            continue;  # start next cycle
        else:  # if user not in one or more channels
            sub_status = False;  # change status to False
    if (sub_status):  # if user subscribed
        pass;
    else:
        markup = InlineKeyboardMarkup();  # create markup
        for channel_id, channel_name, channel_link in channels:  # create buttons with links
            btn = InlineKeyboardButton(text=channel_name, url=channel_link);
            markup.add(btn);
        sub = InlineKeyboardButton(text=subscribe[language][1],
                                   callback_data="mainmenu");  # create check button
        markup.add(sub);  # add button to markup
        bot.send_message(chat_id=chat_id,
                         text=subscribe[language][0],
                         parse_mode="html", reply_markup=markup);
        return;  # terminate function

    ### START MENU ###
    if (call.data == "mainmenu"):
        markup = InlineKeyboardMarkup();
        buttons = mainmenubut[language];
        for text, callback in buttons.items():
            btn = InlineKeyboardButton(text=text, callback_data=callback);
            markup.add(btn);
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=f"{mainmenu[language][0]}{call.message.chat.first_name}{mainmenu[language][1]}",
                              parse_mode="html", reply_markup=markup);

    ### EDITOR MENU ###
    elif (call.data in Second_Menu.keys()):
        markup = InlineKeyboardMarkup();
        buttons = Second_Step_Buttons[call.data][language];
        for text, callback in buttons.items():
            button = InlineKeyboardButton(text=text, callback_data=callback);
            markup.add(button);
        back = InlineKeyboardButton(text=backbtn[language], callback_data="mainmenu");
        markup.add(back);
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=Second_Menu[call.data][language],
                              parse_mode="html", reply_markup=markup);

    ### DROP NEXT STEP MENU ###
    elif (call.data in functions.keys()):
        # to understand this, take a look to «if (__name__=="__main__")», dict «functions»
        message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text=Redactor_Message[call.data][language],
                                        parse_mode="html");
        bot.register_next_step_handler(message, functions[call.data]);



""" UNKNOWN CONTENT HANDLER AND FUNCTION """
@bot.message_handler()
def unknown (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    markup = InlineKeyboardMarkup();  # create markup
    menu = InlineKeyboardButton(text=Go_To_Menu[language], callback_data="mainmenu");  # create back to menu button
    markup.add(menu);  # add button to markup
    bot.send_message(chat_id=chat_id, text=Unknown[language],
                     parse_mode="html", reply_markup=markup);  # send message to user



""" CUT FUNCTIONS """
def cut (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Format_Error[language], parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;    # stop function

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language], parse_mode="html");
    name = file_info.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name) or (".avi" in name)):
        pass;
    else:
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;    # stop function

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    # send message
    msg = bot.send_message(chat_id=chat_id,
                           text=cut1[language],
                           parse_mode='html');
    # and register next step function (name, file are args)
    bot.register_next_step_handler(msg, cut2, name, file);

def cut2 (message, name, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    time = message.text;

    # check information, which user entered
    try:
        start_time, end_time = time.split(" ");
    except Exception:
        # user has entered incorrect information
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=cut2_error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;   # stop function

    # check, is time interval int and >= 0
    isit1 = start_time.isdigit();
    isit2 = end_time.isdigit();
    if (isit1 and isit2):
        start_time: int = int(start_time);
        end_time: int = int(end_time);
    else:
        # user has entered incorrect information
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=cut2_error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;    # stop function

    # write videofile
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(chat_id=chat_id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    redactor = Video();
    # start editing video (perhaps too long)
    src2: str = redactor.cut(src1, start_time, end_time);   # returns path to file or "BAD"
    if (src2 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the video
        bot.send_message(chat_id=chat_id,
                         text=cut2_Start_Sending[language],
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document, visible_file_name=src2.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" CONCATENATE FUNCTIONS """
def concatenate (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info1 = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info1 = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Format_Error[language],
                             parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(message.chat.id, text=Processing_Video[language], parse_mode="html");
    name1 = file_info1.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name1) or (".avi" in name1)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;
    # at this point file has been verified, start downloading
    file1 = bot.download_file(file_info1.file_path);
    # send message
    bot.send_message(message.chat.id, text=concatenate_messages[language], parse_mode='html');
    # and register next step function (name1, file1 are args)
    bot.register_next_step_handler(message, concatenate2, name1, file1);

def concatenate2 (message, name1, file1) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info2 = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info2 = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id, text=Format_Error[language], parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language],
                     parse_mode="html");
    name2 = file_info2.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name2) or (".avi" in name2)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file2 = bot.download_file(file_info2.file_path);
    src1 = name1;
    src2 = name2;
    with open(src1, "wb") as movie1:
        movie1.write(file1);
    with open(src2, "wb") as movie2:
        movie2.write(file2);

    bot.send_message(chat_id=chat_id, text=Files_Successfully_Saved[language],
                     parse_mode="html");

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src3: str = red.concatenate(src1, src2);    # returns path to file or "BAD"
    if (src3 == "BAD"):
        bot.send_message(chat_id=chat_id,
                         text=unknown_error[language],
                         parse_mode="html");
    else:
        # try to send the video
        bot.send_message(chat_id=chat_id,
                         text=concatenate2_messages[language],
                         parse_mode="html");
        with open(src3, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document,
                              visible_file_name=src3.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");
    # removing spent files
    try:
        os.remove(src1)
        os.remove(src2)
        os.remove(src3)
    except Exception:
        pass;
    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" DELETE AUDIO FROM VIDEO FUNCTION """
def del_au (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id, text=Format_Error[language], parse_mode="html")
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(message.chat.id, text=Processing_Video[language], parse_mode="html");
    name = file_info.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name) or (".avi" in name)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data="videored");
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(message.chat.id, text=File_Successfully_Saved[language], parse_mode="html")

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src2: str = red.rmaudio(src1);    # returns path to file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(message.chat.id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the video
        bot.send_message(message.chat.id,
                         text=del_au_messages[language],
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(message.chat.id, document=document, visible_file_name=src2.replace("videos", ""))
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(message.chat.id,
                             text=Send_Error[language],
                             parse_mode="html");
    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;
    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" GET AUDIO FROM VIDEO FUNCTION """
def get_au (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database

    # try to get the file
    try:
        file_info = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id, text=Format_Error[language], parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language], parse_mode="html")
    name = file_info.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name) or (".avi" in name)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);
    bot.send_message(chat_id=chat_id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src2 = red.get_au(src1);    # returns path to file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the audio
        bot.send_message(chat_id=chat_id,
                         text=get_au_messages[language],
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document,
                              visible_file_name=src2.replace("music/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
    markup.add(back)
    bot.send_message(message.chat.id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" CHANGE VIDEO VOLUME FUNCTIONS """
def changevolume (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Format_Error[language],
                             parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language], parse_mode="html")
    name = file_info.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name) or (".avi" in name)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    msg = bot.send_message(chat_id=chat_id,
                           text=change_volume_messages[language],
                           parse_mode='html');
    # and register next step function (name, file are args)
    bot.register_next_step_handler(msg, changevolume2, name, file);

def changevolume2 (message, name, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # check information, which user entered
    try:
        volume: float = float(message.text);
    except Exception:
        # information is incorrect
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_errors[0][language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;
    if (volume >= 0):
        pass;
    else:
        # volume is < 0
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_errors[1][language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point info has been verified, start writing
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(chat_id=chat_id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src2 = red.change_volume(src1, volume);    # returns path to file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the video
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_messages[language].format(volume),
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document, visible_file_name=src2.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" ADD AUDIO TO VIDEO FUNCTIONS """
def addaudio (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info1 = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info1 = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Format_Error[language],
                             parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language], parse_mode="html");
    name1 = file_info1.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name1) or (".avi" in name1)):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info1.file_path);
    # send message
    msg = bot.send_message(chat_id=chat_id,
                           text=add_audio_messages[language],
                           parse_mode='html');
    # and register next step function (name1, file are args)
    bot.register_next_step_handler(msg, addaudio2, name1, file);

def addaudio2 (message, name1, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info2 = bot.get_file(message.audio.file_id);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Audio[language], parse_mode="html");
    name2 = file_info2.file_path;

    # check file format (supported only mp3)
    if (".mp3" in name2):
        pass;
    else:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Audio[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file2 = bot.download_file(file_info2.file_path);
    src1 = name1;
    src2 = name2;
    try:
        with open(src1, "wb") as movie1:
            movie1.write(file);
        with open(src2, "wb") as movie2:
            movie2.write(file2);
    except Exception:
        # one of these files isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    bot.send_message(chat_id=chat_id, text=Files_Successfully_Saved[language],
                     parse_mode="html");

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src3 = red.addaudio(src1, src2);    # returns path to file or "BAD"

    if (src3 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the video
        bot.send_message(chat_id=chat_id,
                         text=add_audio2_messages[language],
                         parse_mode="html");
        with open(src3, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document,
                              visible_file_name=src3.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
        os.remove(src3);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored')
    markup.add(back)
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" GET FRAMES FROM VIDEO FUNCTION """
def img_get (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.document.file_id);
    except Exception:
        try:
            file_info = bot.get_file(message.video.file_id);
        except Exception:
            # file isn't in the correct format or doesn't exist
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Format_Error[language],
                             parse_mode="html");
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                             reply_markup=markup);
            return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Video[language], parse_mode="html");
    name = file_info.file_path;

    # check file format (supported only mp4 or avi)
    if ((".mp4" in name) or (".avi" in name)):
        pass;
    else:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Video[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    src1 = name;
    # start writing
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(chat_id=chat_id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    red = Video();
    # start editing video (perhaps too long)
    src2 = red.extract_frames(src1);    # returns path to file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the archive
        bot.send_message(chat_id=chat_id,
                         text=img_get_messages[language],
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document, visible_file_name=src2);
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        dir = 'photos/';
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f));
        os.remove(src2);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='videored');
    markup.add(back);
    bot.send_message(message.chat.id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" CONCATENATE AUDIO FUNCTIONS """
def concatenate_audio (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.audio.file_id);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Audio[language], parse_mode="html");
    name1 = file_info.file_path;

    # check file format (supported only mp3)
    if (".mp3" in name1):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Audio[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    # send message
    msg = bot.send_message(chat_id=chat_id,
                           text=concatenate_audio_messages[language],
                           parse_mode='html');
    # and register next step func (name1, file are args)
    bot.register_next_step_handler(msg, concatenate_audio2, name1, file);

def concatenate_audio2 (message, name1, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info2 = bot.get_file(message.audio.file_id);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Audio[language], parse_mode="html");
    name2 = file_info2.file_path;

    # check file format (supported only mp3)
    if (".mp3" in name2):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Audio[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file2 = bot.download_file(file_info2.file_path);
    src1 = name1;
    src2 = name2;
    # start writing
    try:
        with open(src1, "wb") as movie1:
            movie1.write(file);
        with open(src2, "wb") as movie2:
            movie2.write(file2);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='checksub');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;


    bot.send_message(chat_id=chat_id, text=Files_Successfully_Saved[language],
                     parse_mode="html");

    # init redactor
    red = Audio();
    # start editing video (perhaps too long)
    src3 = red.concatenate(src1, src2);   # returns path to file or "BAD"

    if (src3 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the audio
        bot.send_message(chat_id=chat_id,
                         text=concatenate_audio2_messages[language],
                         parse_mode="html");
        with open(src3, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document, visible_file_name=src3.replace("audios/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");

    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
        os.remove(src3);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" CUT AUDIO FUNCTIONS """
def cut_audio (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.audio.file_id);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Audio[language], parse_mode="html");
    name1 = file_info.file_path;

    # check file format (supported only mp3)
    if (".mp3" in name1):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Audio[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    # send message
    msg = bot.send_message(chat_id=chat_id,
                     text=cut_audio_messages[language],
                     parse_mode='html');
    # and register next step function (name1, file are args)
    bot.register_next_step_handler(msg, cut_audio2, name1, file);

def cut_audio2 (message, name, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    time = message.text;

    # check information, which user entered
    try:
        start_time, end_time = time.split();
    except Exception:
        # user has entered incorrect information
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=cut_audio2_errors[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;
    isit1 = start_time.isdigit();
    isit2 = end_time.isdigit();
    if (isit1 and isit2):
        start_time = int(start_time);
        end_time = int(end_time);
    else:
        # user has entered incorrect information
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=cut_audio2_errors[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point information has been verified, start writing
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(message.chat.id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    red = Audio();
    # start editing video (perhaps too long)
    src2 = red.cut(src1, start_time, end_time);    # returns path to the file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(message.chat.id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the audio
        bot.send_message(message.chat.id,
                         text=cut_audio2_messages[language],
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(message.chat.id, document=document, visible_file_name=src2.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(message.chat.id,
                             text=Send_Error[language],
                             parse_mode="html");
    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;

    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
    markup.add(back);
    bot.send_message(message.chat.id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" CHANGE AUDIO VOLUME FUNCTIONS """
def changevolumeaudio (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # try to get the file
    try:
        file_info = bot.get_file(message.audio.file_id);
    except Exception:
        # file isn't in the correct format or doesn't exist
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=Format_Error[language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been received, start processing
    bot.send_message(chat_id=chat_id, text=Processing_Audio[language], parse_mode="html");
    name1 = file_info.file_path;

    # check file format (supported only mp3)
    if (".mp3" in name1):
        pass;
    else:
        # file isn't in the correct format
        # hence, send error message
        bot.send_message(chat_id=chat_id, text=Wrong_Format_Audio[language], parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point file has been verified, start downloading
    file = bot.download_file(file_info.file_path);
    # send message
    msg = bot.send_message(chat_id=chat_id,
                           text=change_volume_audio_messages[language],
                           parse_mode='html');
    # and register next step function (name1, file are args)
    bot.register_next_step_handler(msg, changevolumeaudio2, name1, file);

def changevolumeaudio2 (message, name, file) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    # check information, which user entered
    try:
        volume = float(message.text);
    except Exception:
        # user has entered incorrect information
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_errors[0][language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;
    if (volume >= 0):
        pass;
    else:
        # volume is < 0
        # hence, send error message
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_errors[1][language],
                         parse_mode="html");
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                         reply_markup=markup);
        return;

    # at this point information has been verified, start writing
    src1 = name;
    with open(src1, "wb") as movie1:
        movie1.write(file);

    bot.send_message(chat_id=chat_id, text=File_Successfully_Saved[language], parse_mode="html");

    # init redactor
    red = Audio();
    # start editing video (perhaps too long)
    src2 = red.change_volume(src1, volume);    # returns path to the file or "BAD"

    if (src2 == "BAD"):
        bot.send_message(chat_id=chat_id, text=unknown_error[language], parse_mode="html");
    else:
        # try to send the audio
        bot.send_message(chat_id=chat_id,
                         text=change_volume2_audio_messages[language].format(volume),
                         parse_mode="html");
        with open(src2, "rb") as file:
            document = file.read();
        try:
            bot.send_document(chat_id=chat_id, document=document, visible_file_name=src2.replace("videos/", ""));
        except Exception:
            # file wasn't sent
            # hence, send error message
            bot.send_message(chat_id=chat_id,
                             text=Send_Error[language],
                             parse_mode="html");
    # removing spent files
    try:
        os.remove(src1);
        os.remove(src2);
    except Exception:
        pass;
    # and send suggestion to go to menu
    markup = InlineKeyboardMarkup();
    back = InlineKeyboardButton(text=backbtn[language], callback_data='audiored');
    markup.add(back);
    bot.send_message(chat_id=chat_id, text=Back_To_Menu[language], parse_mode="html",
                     reply_markup=markup);



""" ADMIN MENU COMMANDS """
def add_channel (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

    # check admin rights
    if (chat_id in administrators):
        # check for a stop word
        if (message.text.lower() == Cancel_Word[language]):
            del database;
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=admin_mode_stopped[language],
                             parse_mode="html", reply_markup=markup);
            return;
        else:
            pass

        # try to add channel in database
        try:
            database.add_channel(message.text);
            del database;
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Success[language],
                             parse_mode="html", reply_markup=markup);
        except Exception as ex:
            del database;
            # send error message
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=admin_mode_error[language].format(ex),
                             parse_mode="html", reply_markup=markup);
    else:
        markup = InlineKeyboardMarkup();  # create markup
        menu = InlineKeyboardButton(text=Go_To_Menu[language], callback_data="mainmenu");  # create back to menu button
        markup.add(menu);  # add button to markup
        bot.send_message(chat_id=chat_id, text=Unknown[language],
                         parse_mode="html", reply_markup=markup);  # send message to user

def remove_channel (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

    # check admin rights
    if (chat_id in administrators):
        # check for a stop word
        if (message.text.lower() == Cancel_Word[language]):
            del database;
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=admin_mode_stopped[language],
                             parse_mode="html", reply_markup=markup);
            return;
        else:
            pass

        # try to remove channel in database
        try:
            database.delete_channel(message.text);
            del database;
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=Success[language],
                             parse_mode="html", reply_markup=markup);
        except Exception as ex:
            del database;
            # send error message
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=admin_mode_error[language].format(ex),
                             parse_mode="html", reply_markup=markup);
    else:
        markup = InlineKeyboardMarkup();  # create markup
        menu = InlineKeyboardButton(text=Go_To_Menu[language], callback_data="mainmenu");  # create back to menu button
        markup.add(menu);  # add button to markup
        bot.send_message(chat_id=chat_id, text=Unknown[language],
                         parse_mode="html", reply_markup=markup);  # send message to user

def make_promotional_mailing (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

    # check admin rights
    if (chat_id in administrators):
        # check for a stop word
        if (message.text.lower() == Cancel_Word[language]):
            del database;
            markup = InlineKeyboardMarkup();
            back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
            markup.add(back);
            bot.send_message(chat_id=chat_id, text=admin_mode_stopped[language],
                             parse_mode="html", reply_markup=markup);
            return;
        else:
            pass

        # take all users chat_id
        users: tuple = database.take_users();
        del database;
        count: int = 0;
        for user in users:
            try:
                bot.send_message(chat_id=user, text=message.text,
                                 parse_mode="html");
                count += 1
            except Exception:
                pass;
        markup = InlineKeyboardMarkup();
        back = InlineKeyboardButton(text=backbtn[language], callback_data="admin_menu");
        markup.add(back);
        bot.send_message(chat_id=chat_id, text=Success_promotional_mailing[language].format(count),
                         parse_mode="html", reply_markup=markup);
    else:
        markup = InlineKeyboardMarkup();  # create markup
        menu = InlineKeyboardButton(text=Go_To_Menu[language], callback_data="mainmenu");  # create back to menu button
        markup.add(menu);  # add button to markup
        bot.send_message(chat_id=chat_id, text=Unknown[language],
                         parse_mode="html", reply_markup=markup);  # send message to user



if (__name__ == "__main__"):
    # functions to call in 161 line
    functions: dict = {
        "concatenate": concatenate,
        "cut": cut,
        "rmaudio": del_au,
        "getaudio": get_au,
        "changevolume": changevolume,
        "addaudio": addaudio,
        "getframes": img_get,
        "concatenate_audio": concatenate_audio,
        "cut_audio": cut_audio,
        "changevolume_audio": changevolumeaudio,
    };

    # functions to call in 147 line
    admin_menu_functions: dict = {
        "add_channel": add_channel,
        "remove_channel": remove_channel,
        "make_a_promotional_mailing": make_promotional_mailing
    };

    print("Bot Conveditor is running and ready to work.");

    bot.polling(none_stop=True, interval=0);
