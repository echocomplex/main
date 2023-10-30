"""

Using g4f from gpt4free by xtekky (https://github.com/xtekky/gpt4free/)

"""

""" IMPORTS """
import g4f;
from g4f.Provider import *;

providers = (AItianhu, AItianhuSpace,
             Acytoo, AiAsk,
             Aibn, Aichat,
             Ails, Bing,
             ChatForAi, Chatgpt4Online,
             ChatgptAi, ChatgptDemo,
             ChatgptDuo, ChatgptFree,
             ChatgptLogin, ChatgptX,
             Cromicle, DeepInfra,
             FakeGpt, FreeGpt,
             GPTalk, GeekGpt,
             GptChatly, GptForLove,
             GptGo, GptGod,
             Hashnode, Liaobots,
             Llama2, MyShell,
             NoowAi, Opchatgpts,
             Phind, Vercel,
             Ylokh, You, Yqcloud);

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
            for prov in providers:
                try:
                    response = g4f.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=self.__messages,
                        stream=False,
                        provider=prov
                    );
                    break;
                except Exception:
                    continue;
            if (('<!DOCTYPE html>' in response) or ("流量异常" in response)):
                stat += 1;
                continue;
            else:
                break;
        return response;

