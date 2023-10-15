"""

ChatGPT Telegram bot (https://t.me/ChatGPTTGMainBot (@ChatGPTTGMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)



<<< DESCRIPTION FOR DEVELOPERS >>>

Each text of the bot message is taken from the file messages.py,
the text of buttons and callback_data - from the file buttons.py
(they also contain instructions for translators).

Working with the database is done through database.py

All randomization is done through a class Randomizer that is in the file randomizer.py

Information from Wikipedia is taken through the Wikipedia class, which is located in the file work_with_wiki.py

privacy.py should contain token, tuple with administrators, email and password for mail client
(detailed information in the file)

"""



print("Starting...");



""" IMPORTS """
from telebot import TeleBot;
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup;
from privacy import TOKEN, administrators;
from messages import *;
from buttons import *;
from dataedit import Database;
from ai import ChatGPT;
from asyncio import set_event_loop, new_event_loop;


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

    if (chat_id in administrators):
        markup = InlineKeyboardMarkup();
        cont = InlineKeyboardButton(text=Continue[language],
                                    callback_data="admin_menu");
        markup.add(cont);
        bot.send_message(chat_id=chat_id, text=admin_complete[language],
                         parse_mode="html", reply_markup=markup);
    else:
        ### dude, i hate xtekky ###
        chat = ChatGPT();
        chat.add_bot_message("");
        try:
            response: str = chat.generate_response(question="/adminmode");  # get response
            bot.send_message(message.chat.id, text=response);
            bot.register_next_step_handler(message, generate_response, bot_message=response);
        except Exception as ex:
            print(ex);
            bot.send_message(message.chat.id, text=error[language], parse_mode="html");



""" info COMMAND HANDLER AND FUNC """
@bot.message_handler(commands=["info"])
def info (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;
    bot.send_message(chat_id=chat_id, text=information[language], parse_mode="html");



""" CALLBACK HANDLER AND FUNC """
@bot.callback_query_handler(func=lambda call: True)
def inline (call) -> None:
    # search user in database
    chat_id: int = call.message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

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
    if (call.data in languages.values()):
        language = call.data;
        database.update_language(language);
        markup = InlineKeyboardMarkup();
        nxt = InlineKeyboardButton(text=lang_ch[language][1], callback_data="mainmenu");
        markup.add(nxt);
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=lang_ch[language][0], parse_mode="html", reply_markup=markup);

    ### CHECK USER SUBSCRIBE TO CHANNELS ###
    sub_status = True;  # subscribe status
    # check subscribe to channels in cycle
    channels: tuple = database.take_channels();

    for channel_info in channels:
        stat = bot.get_chat_member(chat_id=channel_info[0],
                                   user_id=chat_id).status;  # get user status in channel
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
    del sub_status;
    del database;

    ### START MENU ###
    if (call.data == "mainmenu"):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"{mainmenu[language][0]}{call.message.chat.first_name}{mainmenu[language][1]}", parse_mode="html");



@bot.message_handler(content_types=["text"])
def generate_response (message, bot_message: str = "") -> None:
    question: str = message.text;
    if (question in bot_commands.keys()):
        bot_commands[question](message);
        return;

    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

    ### CHECK USER SUBSCRIBE TO CHANNELS ###
    sub_status = True;  # subscribe status
    # check subscribe to channels in cycle
    channels: tuple = database.take_channels();
    for channel_info in channels:
        stat = bot.get_chat_member(chat_id=channel_info[0],
                                   user_id=chat_id).status;  # get user status in channel
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
    del sub_status;
    del database;

    bot.send_message(message.chat.id, text=generate[language], parse_mode="html")    # send start message

    try:
        set_event_loop(new_event_loop());   # fucking g4f is async!!!!
        chat = ChatGPT();
        chat.add_bot_message(bot_message);
        response: str = chat.generate_response(question=question);    # get response

        ### PARSE RESPONSE ###
        for i in range(len(response) // 4084 + 1):  # one telegram message can contain <= 4084 chars
            if (len(response) <= 4084):
                bot.send_message(message.chat.id, text=response);
            else:
                bot.send_message(message.chat.id, text=response[:4084]);
                response = response[4084::];
        bot.register_next_step_handler(message, generate_response, bot_message=response);
    except Exception as ex:
        print(ex);
        bot.send_message(message.chat.id, text=error[language], parse_mode="html");



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
        ### dude, i hate xtekky ###
        chat = ChatGPT();
        chat.add_bot_message("");
        try:
            response: str = chat.generate_response(question=message.text);  # get response
            bot.send_message(message.chat.id, text=response);
            bot.register_next_step_handler(message, generate_response, bot_message=response);
        except Exception as ex:
            print(ex);
            bot.send_message(message.chat.id, text=error[language], parse_mode="html");

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
        ### dude, i hate xtekky ###
        chat = ChatGPT();
        chat.add_bot_message("");
        try:
            response: str = chat.generate_response(question=message.text);  # get response
            bot.send_message(message.chat.id, text=response);
            bot.register_next_step_handler(message, generate_response, bot_message=response);
        except Exception as ex:
            print(ex);
            bot.send_message(message.chat.id, text=error[language], parse_mode="html");

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
        ### dude, i hate xtekky ###
        chat = ChatGPT();
        chat.add_bot_message("");
        try:
            response: str = chat.generate_response(question=message.text);  # get response
            bot.send_message(message.chat.id, text=response);
            bot.register_next_step_handler(message, generate_response, bot_message=response);
        except Exception as ex:
            print(ex);
            bot.send_message(message.chat.id, text=error[language], parse_mode="html");



if (__name__ == "__main__"):
    # functions to call in 128 line
    admin_menu_functions: dict = {
        "add_channel": add_channel,
        "remove_channel": remove_channel,
        "make_a_promotional_mailing": make_promotional_mailing
    };

    bot_commands: dict = {
        "/start": start,
        "/language": start,
        "/info": info,
        "/adminmode": admin_mode
    };

    print("Bot ChatGPT Telegram is started and ready to work");

    bot.polling(none_stop=True, interval=0);
