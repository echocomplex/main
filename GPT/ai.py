"""

Using g4f from gpt4free by xtekky (https://github.com/xtekky/gpt4free/)

"""

""" IMPORTS """
import g4f;
from g4f.Provider import *;

class ChatGPT:
    def __init__ (self) -> None:
        self.__messages: list = [];

    def add_bot_message (self, message: str) -> None:
        self.__messages.append({"role": "assistant", "content": message});

    def generate_response(self, question: str) -> str:
        self.__messages.append({"role": "user", "content": question})
        stat: int = 0;
        while (True):
            if (stat > 5):
                raise Exception("Something went wrong... Try again later.");
            try:
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_35_turbo,
                    messages=self.__messages
                );
            except Exception as e:
                print(e);
                stat: int = 0;
                continue;
            if (('<!DOCTYPE html>' in response) or ("流量异常" in response) or (response == "") or ("chatbase" in response)):
                stat += 1;
                continue;
            else:
                break;
        return response;



if (__name__ == "__main__"):
    chat = ChatGPT();
    chat.add_bot_message("");
    print(chat.generate_response("Hello!"));

