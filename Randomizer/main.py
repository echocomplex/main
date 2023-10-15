"""

Randomizer - Рандомайзер (Telegram Bot)
https://t.me/RandomizerMainBot (@RandomizerMainBot)
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
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton;
from privacy import *;
from messages import *;
from buttons import *;
from database import Database;
from randomizer import Randomizer;
from work_with_wiki import Wikipedia, Wikipedia_Error;


""" SIGN IN """
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



""" CALLBACK HANDLER AND CALLBACK FUNC """
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

    ### SECOND MENU ###
    elif (call.data in second_menu_buttons[language].keys()):
        markup = InlineKeyboardMarkup();   # create markup
        btn = InlineKeyboardButton(text=second_menu_buttons[language][call.data][0],
                                   callback_data=second_menu_buttons[language][call.data][1]);
        markup.add(btn);
        back = InlineKeyboardButton(text=backbtn[language], callback_data="mainmenu");   # create button
        markup.add(back)    # add button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=second_menu_message[language][call.data],
                              parse_mode="html", reply_markup=markup)    # send message

    ### RANDOMIZER ###
    elif (call.data in randomizer_messages[language].keys()):
        # COUNTRY RANDOMIZER
        if (call.data == "take_country"):
            randomizer = Randomizer(language);    # init randomizer class
            country: str = randomizer.country();    # get random country
            del randomizer;
            wiki = Wikipedia(language);    # init wiki class
            try:
                wiki.set_article(country);    # set article
                link: str = wiki.get_link();    # get link
            except Wikipedia_Error:
                link: str = f"https://{language.lower()}.wikipedia.org/";
            del wiki;

            # send message
            bot.send_message(chat_id=chat_id,
                             text=randomizer_messages[language][call.data][0].format(link, country),
                             parse_mode="html");    # send message

            markup = InlineKeyboardMarkup();    # create markup
            again = InlineKeyboardButton(text=randomizer_buttons[language][call.data],
                                         callback_data="take_country");     # create button
            back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");  # create button
            markup.add(again);    # add btn to markup
            markup.add(back);    # add btn to markup
            bot.send_message(chat_id=chat_id, text=randomizer_messages[language][call.data][1],
                             parse_mode="html", reply_markup=markup);    # send message

        # PROFESSION RANDOMIZER
        elif (call.data == "take_work"):
            randomizer = Randomizer(language);  # init randomizer class
            profession: str = randomizer.profession();  # get random profession
            del randomizer;

            # send message
            bot.send_message(chat_id=chat_id,
                             text=randomizer_messages[language][call.data][0].format(profession),
                             parse_mode="html");  # send message

            markup = InlineKeyboardMarkup();  # create markup
            again = InlineKeyboardButton(text=randomizer_buttons[language][call.data],
                                         callback_data="take_work");  # create button
            back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");  # create button
            markup.add(again);  # add btn to markup
            markup.add(back);  # add btn to markup
            bot.send_message(chat_id=chat_id, text=randomizer_messages[language][call.data][1],
                             parse_mode="html", reply_markup=markup);  # send message

        # ACTIONS RANDOMIZER
        elif (call.data == "take_action"):
            randomizer = Randomizer(language);  # init randomizer class
            action: str = randomizer.action();  # get random action
            del randomizer;

            # send message
            bot.send_message(chat_id=chat_id,
                             text=randomizer_messages[language][call.data][0].format(action),
                             parse_mode="html");  # send message

            markup = InlineKeyboardMarkup();  # create markup
            again = InlineKeyboardButton(text=randomizer_buttons[language][call.data],
                                         callback_data="take_action");    # create button
            back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");    # create button
            markup.add(again);    # add btn to markup
            markup.add(back);    # add btn to markup
            bot.send_message(chat_id=chat_id, text=randomizer_messages[language][call.data][1],
                             parse_mode="html", reply_markup=markup);    # send message

        # WORD RANDOMIZER
        elif (call.data == "take_word"):
            msg = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                        text=randomizer_messages[language][call.data],
                                        parse_mode="html");    # send message
            bot.register_next_step_handler(msg, take_word);    # register next step func

        # NUMBER RANDOMIZER
        elif (call.data == "take_num"):
            msg = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                        text=randomizer_messages[language][call.data],
                                        parse_mode="html");    # send message
            bot.register_next_step_handler(msg, take_number);    # register next func

        # ARTICLES RANDOMIZER
        elif (call.data == "take_article"):
            wiki = Wikipedia(language);  # init wikipedia
            wiki.random_article();  # set random article
            title: str = wiki.get_title();  # get title
            link: str = wiki.get_link();  # get link
            del wiki;

            # send message
            bot.send_message(chat_id=chat_id,
                             text=randomizer_messages[language][call.data][0].format(link, title),
                             parse_mode="html");  # send message

            markup = InlineKeyboardMarkup();  # create markup
            again = InlineKeyboardButton(text=randomizer_buttons[language][call.data],
                                         callback_data="take_article");  # create button
            back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");  # create button
            markup.add(again);  # add btn to markup
            markup.add(back);  # add btn to markup
            bot.send_message(chat_id=chat_id, text=randomizer_messages[language][call.data][1],
                             parse_mode="html", reply_markup=markup);  # send message



""" UNKNOWN CONTENT HANDLER AND FUNC """
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



""" RANDOM WORD CHOICE """
def take_word (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    randomizer = Randomizer(language);  # init randomizer class
    word: str = randomizer.word(message.text);  # get random word

    # send message
    bot.send_message(message.chat.id,
                     text=take_word_messages[language][0].format(word),
                     parse_mode="html");

    markup = InlineKeyboardMarkup();
    again = InlineKeyboardButton(text=take_word_button[language], callback_data="take_word");
    back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");
    markup.add(again);
    markup.add(back);
    bot.send_message(message.chat.id,
                     text=take_word_messages[language][1],
                     parse_mode="html", reply_markup=markup);



""" RANDOM NUMBER CHOICE """
def take_number (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();
    del database;

    try:
        first, second = message.text.split(" ");    # try to split user text to variables
        try:    # if format is correct trying to convert variables to integer
            first = int(first);
            second = int(second);
            randomizer = Randomizer(language);  # init randomizer
            num: int = randomizer.number(first, second);  # get random number
            msg: str = take_number_messages[language][2].format(num);
        except:    # if user info can't be converted to integer
            msg: str = take_number_messages[language][1];
    except:    # if user entered info not in correct format
        msg: str = take_number_messages[language][0];

    # send message
    bot.send_message(message.chat.id, text=msg, parse_mode="html");

    markup = InlineKeyboardMarkup();  # create markup
    again = InlineKeyboardButton(text=take_number_button[language], callback_data="take_num");
    back = InlineKeyboardButton(text=to_the_start_menu[language], callback_data="mainmenu");
    markup.add(again);
    markup.add(back);
    bot.send_message(message.chat.id,
                     text=take_number_messages[language][3],
                     parse_mode="html", reply_markup=markup)  # send message



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
            except:
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
    # functions to call in 132 line
    admin_menu_functions: dict = {
        "add_channel": add_channel,
        "remove_channel": remove_channel,
        "make_a_promotional_mailing": make_promotional_mailing
    };

    print("Bot Randomizer is running and ready to work...");

    bot.polling(none_stop=True, interval=0);
