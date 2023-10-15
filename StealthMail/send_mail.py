"""

SEND MAIL Function for StealthMail - Анонимные письма
(Telegram Bot) (@StealthMailMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)



<< DESCRIPTION FOR DEVELOPERS >>

When initializing the «Email_Client» class, two arguments must be passed:
the sender's email and his password.

To send a message, call the «send_mail» function from this class,
passing it the following arguments: recipient's email, subject, email text.

The server is created in the __init__ function,
so you can add other functions to this class
(for example, a function that will read e-mails received on this server).

"""


""" IMPORTS """
import smtplib as smtp;
from smtplib import *;


""" MAIN CLASS """
class Email_Client:
    """"""

    def __init__(self, email: str, password: str) -> None:
        self.__email: str = email;
        self.__password: str = password;
        self.__server = smtp.SMTP_SSL('smtp.yandex.ru', 465);
        self.__server.set_debuglevel(1);
        self.__server.ehlo(self.__email);
        self.__server.login(self.__email, self.__password);
        self.__server.auth_plain();

    def __del__ (self) -> None:
        self.__server.quit();

    """ SEND MAIL FUNC """
    def send_mail(self, target_email: str, subject: str, email_text: str) -> int:
        try:
            message_mail = f'From: {self.__email}\nTo: {target_email}\nSubject: {subject}\n\n{email_text}'.encode('utf-8');
            self.__server.sendmail(self.__email, target_email, message_mail);
            return 0;
        except SMTPDataError:
            return 1;
        except Exception as e:
            print(e);
            return 2;
