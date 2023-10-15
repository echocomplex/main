"""

TEXT TO SPEECH Function for OnlyVox (Telegram Bot) (@OnlyVoxMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<< DESCRIPTION FOR DEVELOPERS >>

Class Speech takes 1 argument (language (2 chars)) and has two functions (get() and mp3()).

You need to set speech first via «get()» function, after this you can run «mp3()» function,
which returns the path to the mp3 file.


"""


""" IMPORTS """
import random;
from gtts import gTTS;


""" EXCEPTION CLASS """
class SpeechException (Exception):
    def __init__ (self, txt: str) -> None:
        self.text: str = txt;


""" MAIN CLASS """
class Speech:

    def __init__(self, language: str) -> None:
        self.__language: str = language.lower();
        self.__speech = None;

    """ GET SPEECH """
    def get (self, text: str) -> None:
        self.__speech = gTTS(text=text, lang=self.__language);

    """ GET MP3 """
    def mp3 (self) -> str:
        if (self.__speech is None):
            raise SpeechException("Speech was not set. You need to run «get()» function first.");
        else:
            filename = f"OnlyVox_render{random.randint(1000, 9999)}.mp3";
            self.__speech.save(filename);
            return filename;
