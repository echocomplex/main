"""

DATABASE EDITOR FOR OnlyVox - Озвучка текста (Telegram Bot)
https://t.me/OnlyVoxMainBot (@OnlyVoxMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

Database class works with two files: users.db and channels.db

users.db has 2 columns (chat_id: int, language: char(10))

channels.db has 3 columns (channel_id: int, channel_name: varchar(100), channel_link: varchar(100))

"""

""" IMPORTS """
import sqlite3;


class Database:
    chat_id: int;

    """ PRIVATE VARIABLES """
    def __init__ (self, chat_id: int) -> None:
        self.__chat_id: int = chat_id;
        self.__filename: str = "users.db";
        self.__channels_filename: str = "channels.db";
        self.__connection = sqlite3.Connection(self.__filename);
        self.__cursor = self.__connection.cursor();

    """ CLOSE CONNECTION """
    def __del__ (self):
        self.__connection.close();

    """ ADD USER TO DATABASE """
    def add_user (self) -> None:
        self.__cursor.execute(
            """
            INSERT OR IGNORE INTO users (chat_id, language) 
            VALUES (?, ?)
            """,
            (self.__chat_id, "RU"));
        self.__connection.commit();

    """ TAKE A TUPLE WITH USERS """
    def take_users (self) -> tuple:
        self.__cursor.execute(
            """
            SELECT chat_id
            FROM users
            """);
        users: list = [];
        data: list = self.__cursor.fetchall();
        for row in data:
            users.append(row[0]);
        return tuple(users);

    """ TAKE language FROM TARGET USER """
    def take_language (self) -> str:
        self.__cursor.execute(
            """
            SELECT language 
            FROM users 
            WHERE chat_id = ?
            """,
            (self.__chat_id,));
        record: list = self.__cursor.fetchall();
        language: str = record[0][0];
        return language;

    """ UPDATE TARGET USER language"""
    def update_language (self, language: str) -> None:
        self.__cursor.execute(
            """
            UPDATE users 
            SET language = ?
            WHERE chat_id = ?
            """,
            (language, self.__chat_id));
        self.__connection.commit();

    """ TAKE CHANNELS """
    def take_channels (self) -> tuple:
        connection = sqlite3.Connection(self.__channels_filename);
        cursor = connection.cursor();
        cursor.execute(
            """
            SELECT *
            FROM channels
            """
        );
        channel_info: tuple = tuple(cursor.fetchall());
        connection.close();
        return channel_info;

    """ ADD CHANNEL """
    def add_channel (self, channel_info: str) -> None:
        channel_id, channel_name, channel_link = channel_info.split("----");
        channel_id = int(channel_id);
        connection = sqlite3.Connection(self.__channels_filename);
        cursor = connection.cursor();
        cursor.execute(
            """
            INSERT INTO channels (channel_id, channel_name, channel_link)
            VALUES (?, ?, ?)
            """,
            (channel_id, channel_name, channel_link)
        );
        connection.commit();
        connection.close();

    """ DELETE CHANNEL """
    def delete_channel (self, channel_link: str) -> None:
        connection = sqlite3.Connection(self.__channels_filename);
        cursor = connection.cursor();
        cursor.execute(
            """
            DELETE FROM channels
            WHERE channel_link = ?
            """,
            (channel_link,)
        );
        connection.commit();
        connection.close();


if (__name__ == "__main__"):
    connection = sqlite3.Connection("users.db");
    connection2 = sqlite3.Connection("channels.db");
    cursor = connection.cursor();
    cursor2 = connection2.cursor();
    cursor.execute(""" SELECT * FROM users """);
    print(cursor.fetchall());
    cursor2.execute(""" SELECT * FROM channels """);
    print(cursor2.fetchall());
