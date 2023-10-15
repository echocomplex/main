"""

WikiNavigator - Википедия в Телеграм (Telegram Bot)
https://t.me/WikiNavigatorMainBot (@WikiNavigatorMainBot)
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
from work_with_wiki import Wikipedia, WikipediaError;


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
        bot.send_message(chat_id=chat_id, text=no_result[language],
                         parse_mode="html");  # send message to user



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



""" random COMMAND HANDLER AND FUNC """
@bot.message_handler(commands=["random"])
def random (message) -> None:
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

    # take random article
    wiki = Wikipedia(language);
    wiki.random_article();
    article_name: str = wiki.get_title();
    database.set_article(article_name);
    del database;
    article_link: str = wiki.get_link();
    del wiki;

    # add buttons
    markup = InlineKeyboardMarkup();
    btn_to_page = InlineKeyboardButton(text=select_article_buttons[language][0], url=article_link);
    markup.add(btn_to_page);
    send_page_text = InlineKeyboardButton(text=select_article_buttons[language][1][0],
                                          callback_data=select_article_buttons[language][1][1].format(0));
    markup.add(send_page_text);

    # send message
    bot.send_message(chat_id=chat_id, text=random_article_message[language].format(article_name),
                     parse_mode="html", reply_markup=markup);



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

    ### START MENU ###
    if (call.data == "mainmenu"):
        del database;
        markup = InlineKeyboardMarkup();
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=f"{mainmenu[language][0]}{call.message.chat.first_name}{mainmenu[language][1]}",
                              parse_mode="html", reply_markup=markup);

    ### MENU NAVIGATION ###
    # SELECT ARTICLE #
    elif ("select_article" in call.data):
        index, backkey = int(call.data.split("$")[1]), int(call.data.split("$")[2]);
        articles: tuple = tuple(database.take_article().split("-@-&"));
        del database;
        page_name: str = articles[index];

        # init wikipedia
        wiki = Wikipedia(language);
        try:
            wiki.set_article(page_name);
        except WikipediaError:
            return;
        url = wiki.get_link();
        del wiki;

        markup = InlineKeyboardMarkup();
        btn_to_page = InlineKeyboardButton(text=select_article_buttons[language][0], url=url);
        markup.add(btn_to_page);
        send_page_text = InlineKeyboardButton(text=select_article_buttons[language][1][0],
                                              callback_data=select_article_buttons[language][1][1].format(index));
        markup.add(send_page_text);
        back = InlineKeyboardButton(text=select_article_buttons[language][2][0],
                                    callback_data=select_article_buttons[language][2][1].format(backkey));
        markup.add(back);

        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=select_article_message[language].format(page_name),
                              parse_mode="html", reply_markup=markup);

    # SEND TEXT IN MESSAGE #
    elif ("send_page_text" in call.data):
        index: int = int(call.data.split("$")[1]);
        articles: tuple = tuple(database.take_article().split("-@-&"));
        del database;
        page_name: str = articles[index];

        try:
            wiki = Wikipedia(language);
            text: str = wiki.get_text(page_name);
            ### PARSE RESPONSE ###
            for i in range(len(text) // 4084 + 1):  # one telegram message can contain <= 4084 chars
                if (len(text) <= 4084):
                    bot.send_message(call.message.chat.id, text=text);
                else:
                    bot.send_message(call.message.chat.id, text=text[:4084]);
                    text = text[4084::];
        except Exception:
            pass;

    # SHOW THE NEXT MENU #
    elif ("next" in call.data):
        index: int = int(call.data.split("$")[1]);
        articles: tuple = tuple(database.take_article().split("-@-&"));
        del database;

        markup = InlineKeyboardMarkup();

        try:
            if (index+9 < len(articles)):
                for i in range(index, index+8):
                    btn = InlineKeyboardButton(text=articles[i], callback_data=f"select_article${i}${index}");
                    markup.add(btn);
                nxt = InlineKeyboardButton(text=nextbtn[language], callback_data=f"next${index+8}");
                markup.add(nxt);  # add button to markup
                back = InlineKeyboardButton(text=backbtn[language], callback_data=f"back${index-8}");
                markup.add(back);
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                      text=here_is_your_search_result[language],
                                      parse_mode="html", reply_markup=markup);
            else:
                for i in range(index, len(articles)):
                    btn = InlineKeyboardButton(text=articles[i], callback_data=f"select_article${i}${index}");
                    markup.add(btn);
                back = InlineKeyboardButton(text=backbtn[language], callback_data=f"back${index-8}");
                markup.add(back);
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                      text=here_is_your_search_result[language],
                                      parse_mode="html", reply_markup=markup);
        except Exception:
            pass;

    # SHOW THE PAST MENU #
    elif ("back" in call.data):
        index: int = int(call.data.split("$")[1]);
        articles: tuple = tuple(database.take_article().split("-@-&"));
        del database;

        markup = InlineKeyboardMarkup();

        try:
            if (index > 1):
                for i in range(index, index+8):
                    btn = InlineKeyboardButton(text=articles[i], callback_data=f"select_article${i}${index}");
                    markup.add(btn);
                nxt = InlineKeyboardButton(text=nextbtn[language], callback_data=f"next${index+8}");
                markup.add(nxt);  # add button to markup
                back = InlineKeyboardButton(text=backbtn[language], callback_data=f"back${index-8}");
                markup.add(back);
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                      text=here_is_your_search_result[language],
                                      parse_mode="html", reply_markup=markup);
            else:
                for i in range(9):
                    btn = InlineKeyboardButton(text=articles[i], callback_data=f"select_article${i}${index}");
                    markup.add(btn);
                nxt = InlineKeyboardButton(text=nextbtn[language], callback_data=f"next${index+8}");
                markup.add(nxt);
                bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                                      text=here_is_your_search_result[language],
                                      parse_mode="html", reply_markup=markup);
        except Exception:
            pass;




""" SEARCH ARTICLE """
@bot.message_handler(content_types=["text"])
def search (message) -> None:
    # search user in database
    chat_id: int = message.chat.id;
    database = Database(chat_id);
    database.add_user();
    language: str = database.take_language();

    wiki = Wikipedia(language);
    result: tuple = wiki.search(message.text);
    del wiki;

    to_write_in_database: str = "";
    if (len(result) > 0):
        for i in range(len(result)):
            if (i+1 == len(result)):
                to_write_in_database += result[i];
            else:
                to_write_in_database += f"{result[i]}-@-&";
        database.set_article(to_write_in_database);
        del database;

        markup = InlineKeyboardMarkup();  # create markup

        if (len(result) > 10):
            for y in range(9):
                btn = InlineKeyboardButton(text=result[y], callback_data=f"select_article${y}${0}");
                markup.add(btn);
            nxt = InlineKeyboardButton(text=nextbtn[language], callback_data=f"next${9}");
            markup.add(nxt);  # add button to markup
            bot.send_message(chat_id=chat_id, text=here_is_your_search_result[language],
                             parse_mode="html", reply_markup=markup);  # send message to user
        else:
            for i in range(len(result)):
                btn = InlineKeyboardButton(text=result[i], callback_data=f"select_article${i}${0}");
                markup.add(btn);
            bot.send_message(chat_id=chat_id, text=here_is_your_search_result[language],
                             parse_mode="html", reply_markup=markup);  # send message to user
    else:
        bot.send_message(chat_id=chat_id, text=no_result[language],
                         parse_mode="html");



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
        bot.send_message(chat_id=chat_id, text=no_result[language],
                         parse_mode="html");  # send message to user

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
        bot.send_message(chat_id=chat_id, text=no_result[language],
                         parse_mode="html");  # send message to user

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
        bot.send_message(chat_id=chat_id, text=no_result[language],
                         parse_mode="html");  # send message to user



if (__name__ == "__main__"):
    # functions to call in 132 line
    admin_menu_functions: dict = {
        "add_channel": add_channel,
        "remove_channel": remove_channel,
        "make_a_promotional_mailing": make_promotional_mailing
    };

    print("Bot WikiNavigator is running and ready to work.");

    bot.polling(none_stop=True, interval=0);
