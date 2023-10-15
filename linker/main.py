"""

linker - Telegram Bot (https://t.me/maineyeechobot)

This bot just send links to other bots :)

"""


print("Starting...")


""" IMPORTS """
from telebot import TeleBot;
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup;
from privacy import TOKEN;
from buttonsmessages import buttons, start_message, glad_to_see;


bot = TeleBot(TOKEN);


@bot.callback_query_handler(func=lambda call: True)
def inline (call) -> None:
    language: str = call.data;
    markup = InlineKeyboardMarkup();
    for text, callback in buttons[language].items():
        if (callback in ("RU", "EN")):
            btn = InlineKeyboardButton(text=text, callback_data=callback);
        else:
            btn = InlineKeyboardButton(text=text, url=callback);
        markup.add(btn);
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id, text=f"{glad_to_see[language].format(call.message.chat.first_name)}\n\n{start_message[language]}",
                          parse_mode="html", reply_markup=markup);



@bot.message_handler()
def anycontent (message) -> None:
    language: str = "RU";
    markup = InlineKeyboardMarkup();
    for text, callback in buttons[language].items():
        if (callback in ("RU", "EN")):
            btn = InlineKeyboardButton(text=text, callback_data=callback);
        else:
            btn = InlineKeyboardButton(text=text, url=callback);
        markup.add(btn);
    bot.send_message(message.chat.id, text=f"{glad_to_see[language].format(message.chat.first_name)}\n\n{start_message[language]}",
                     parse_mode="html", reply_markup=markup);


if (__name__ == "__main__"):
    print("Bot main is running and ready to work...");
    bot.polling(none_stop=True, interval=0);
