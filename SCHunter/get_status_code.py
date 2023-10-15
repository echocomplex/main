"""

GET_STATUS_CODE Function for SCHunter (Telegram Bot) (@SCHunterMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

"""

""" IMPORTS """
import requests;
from status_codes import Codes;


class StatusCodeException (Exception):
    def __init__(self, text) -> None:
        self.text: str = text;



class StatusCode:

    def __init__ (self, language: str) -> None:
        self.__status_code = None;
        self.__request = None;
        self.__language: str = language.lower();

    """ SET STATUS CODE VIA URL """
    def set_status_code_via_url (self, url: str) -> None:
        try:
            self.__request = requests.get(url);
            self.__status_code = self.__request.status_code;
        except Exception:
            raise StatusCodeException("Unable to connect to the host.");

    """ SET STATUS CODE """
    def set_status_code (self, status_code: int) -> None:
        try:
            self.__status_code = int(status_code);
        except ValueError:
            raise StatusCodeException("Status code is not a number.");

    """ GET STATUS CODE """
    def get_status_code (self) -> int:
        if (self.__status_code is not None):
            return self.__status_code;
        else:
            raise StatusCodeException("No status code has been set.");

    """ GET INFO ABOUT STATUS CODE"""
    def info (self) -> str:
        if (self.__status_code is not None):
            try:
                info = Codes[self.__status_code][self.__language];
                return info;
            except KeyError:
                raise StatusCodeException("Status code does not exist.");
        else:
            raise StatusCodeException("No status code has been set.");
