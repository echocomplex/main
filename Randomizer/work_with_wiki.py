"""

WORK WITH WIKI FOR Randomizer bot (https://t.me/RandomizerMainBot (@RandomizerMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

"""



""" IMPORTS """
import wikipedia;
import requests;
from bs4 import BeautifulSoup;



""" EXCEPTION CLASS """
class Wikipedia_Error (Exception):
    def __init__ (self, text) -> None:
        self.txt = text;



""" CLASS WIKIPEDIA """
class Wikipedia:

    def __init__ (self, language: str) -> None:
        self.__language: str = language.lower();
        wikipedia.set_lang(self.__language);    # set language
        self.__article = None;
        self.__link: str = "";
        self.__title: str = "";

    """ SET ARTICLE """
    def set_article (self, request: str) -> None:
        try:
            self.__article = wikipedia.page(request);    # make request
            self.__link = self.__article.url;
            self.__title = self.__article.title;
        except:
            raise Wikipedia_Error("Article not found.");

    """ GET ARTICLE TITLE """
    def get_title (self) -> str:
        if (self.__title != ""):
            return self.__title;
        else:
            raise Wikipedia_Error("Article not selected. You need to set the article first.");

    """ GET ARTICLE LINK """
    def get_link (self) -> str:
        if (self.__link != ""):
            return self.__link;
        else:
            raise Wikipedia_Error("Article not selected. You need to set the article first.");

    """ SET RANDOM ARTICLE """
    def random_article (self) -> None:
        url = requests.get(f"https://{self.__language}.wikipedia.org/wiki/Special:Random");
        soup = BeautifulSoup(url.content, "html.parser");
        title = soup.find(class_="firstHeading").text;
        try:
            self.set_article(title);
        except Wikipedia_Error:
            self.__title = title;
            self.__link = f"https://{self.__language}.wikipedia.org/wiki/{title}";
