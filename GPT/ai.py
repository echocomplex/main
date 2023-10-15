"""

Using g4f from gpt4free by xtekky (https://github.com/xtekky/gpt4free/)

"""



""" IMPORTS """
import g4f;



class ChatGPT:
    def __init__ (self) -> None:
        self.__messages: list = [];

    def add_bot_message (self, message: str) -> None:
        self.__messages.append({"role": "assistant", "content": message});

    def generate_response (self, question: str) -> str:
        self.__messages.append({"role": "user", "content": question})
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.__messages,
            stream=False
        );
        return response;
