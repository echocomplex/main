"""

Using g4f from gpt4free by xtekky (https://github.com/xtekky/gpt4free/)

"""

""" IMPORTS """
from g4f.client import Client
from g4f.Provider import DeepInfra
class ChatGPT:
    def __init__ (self) -> None:
        self.__messages: list = [];

    def add_bot_message (self, message: str) -> None:
        self.__messages.append({"role": "assistant", "content": message});

    def generate_response(self, question: str) -> str:
        self.__messages.append({"role": "user", "content": question});
        client = Client();
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            provider=DeepInfra,
            messages=self.__messages
        )
        return response.choices[0].message.content;



if (__name__ == "__main__"):
    chat = ChatGPT();
    chat.add_bot_message("");
    print(chat.generate_response("Hello! How are you?"));

