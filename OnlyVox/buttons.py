"""

BUTTONS FOR OnlyVox - Озвучка текста (Telegram Bot)
https://t.me/OnlyVoxMainBot (@OnlyVoxMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<< DESCRIPTION FOR TRANSLATORS >>

--- To add new language you need add it to «languages» dictionary

WARNING: IF AT LEAST ONE OF THE DICTIONARIES (files messages.py, buttons.py)
DOES NOT CONTAIN THE LANGUAGE YOU ADDED,
AN ERROR WILL OCCUR THERE.

--- How does it work?
The program takes the language code from the «languages» dictionary and accesses each of the
other dictionaries using this code. It is important to use a single code that is specified
in «languages» dictionary.

THE LANGUAGE CODE MUST CONSIST OF ONLY 2 CHARACTERS

callback_data must be the same for all languages and must not have any changes.

You can see the filling format below.

"""


""" 
struct:
    language_name (str): language_key (str)
"""
languages: dict = {
    "🇷🇺 Russian": "RU",
    "🇺🇸 English": "EN"
};

"""
struct for all the following dictionaries:
    language_key (str): any_info
"""

to_the_start_menu: dict = {
    "RU": "⬅️ К начальному меню",
    "EN": "⬅️ To the start menu"
};

languages_buttons: dict = {
    "RU": (
        ('Русский 🇷🇺', 'ru'),
        ('Английский 🇺🇸', 'en'),
        ('Китайский 🇨🇳', 'zh'),
        ('Испанский 🇪🇸', 'es'),
        ('Французский 🇫🇷', 'fr'),
        ('Немецкий 🇩🇪', 'de'),
        ('Турецкий 🇹🇷', 'tr'),
        ('Арабский 🇸🇦', 'ar'),
        ('Итальянский 🇮🇹', 'it'),
        ('Хинди 🇮🇳', 'hi'),
        ('Китайский (упрощенный) 🇨🇳', 'zh-CN'),
        ('Японский 🇯🇵', 'ja'),
        ('Украинский 🇺🇦', 'uk'),
        ('Африканский 🇿🇦', 'af'),
        ('Болгарский 🇧🇬', 'bg'),
        ('Бенгальский 🇧🇩', 'bn'),
        ('Боснийский 🇧🇦', 'bs'),
        ('Каталонский 🇪🇸', 'ca'),
        ('Чешский 🇨🇿', 'cs'),
        ('Датский 🇩🇰', 'da'),
        ('Греческий 🇬🇷', 'el'),
        ('Эстонский 🇪🇪', 'et'),
        ('Финский 🇫🇮', 'fi'),
        ('Гуджарати 🇮🇳', 'gu'),
        ('Хорватский 🇭🇷', 'hr'),
        ('Венгерский 🇭🇺', 'hu'),
        ('Индонезийский 🇮🇩', 'id'),
        ('Исландский 🇮🇸', 'is'),
        ('Иврит 🇮🇱', 'iw'),
        ('Яванский 🇮🇱', 'jw'),
        ('Кхмерский 🇰🇭', 'km'),
        ('Каннада 🇮🇳', 'kn'),
        ('Корейский 🇰🇷', 'ko'),
        ('Латинский 🇲🇽', 'la'),
        ('Латышский 🇱🇻', 'lv'),
        ('Малаялам 🇮🇳', 'ml'),
        ('Маратхи 🇮🇳', 'mr'),
        ('Малайский 🇮🇱', 'ms'),
        ('Мьянма 🇲🇲', 'my'),
        ('Непальский 🇮🇳', 'ne'),
        ('Голландский 🇳🇱', 'nl'),
        ('Норвежский 🇳🇴', 'no'),
        ('Польский 🇵🇱', 'pl'),
        ('Португальский 🇵🇹', 'pt'),
        ('Румынский 🇷🇴', 'ro'),
        ('Сингальский 🇱🇰', 'si'),
        ('Словацкий 🇸🇰', 'sk'),
        ('Албанский 🇦🇱', 'sq'),
        ('Сербский 🇷🇸', 'sr'),
        ('Сунданский 🇸🇩', 'su'),
        ('Шведский 🇸🇪', 'sv'),
        ('Суахили 🇰🇪', 'sw'),
        ('Тамильский 🇮🇳', 'ta'),
        ('Телугу 🇮🇳', 'te'),
        ('Тайский 🇹🇭', 'th'),
        ('Филиппинский 🇵🇭', 'tl'),
        ('Урду 🇮🇳', 'ur'),
        ('Вьетнамский 🇻🇳', 'vi'),
        ('Китайский (Мандарин/Тайвань) 🇨🇳', 'zh-TW')
    ),
    "EN": (
        ('Russian 🇷🇺 ', 'ru'),
        ('English 🇺🇸 ', 'en'),
        ('Chinese 🇨🇳 ', 'zh'),
        ('Spanish 🇪🇸 ', 'es'),
        ('French 🇫🇷 ', 'fr'),
        ('German 🇩🇪 ', 'de'),
        ('Turkish 🇹🇷 ', 'tr'),
        ('Arabic 🇸🇦 ', 'ar'),
        ('Italian 🇮🇹 ', 'it'),
        ('Hindi 🇮🇳 ', 'hi'),
        ('Chinese (Simplified) 🇨🇳 ', 'zh-CN'),
        ('Japanese 🇯🇵 ', 'ja'),
        ('Ukrainian 🇺🇦 ', 'uk'),
        ('African 🇿🇦 ', 'af'),
        ('Bulgarian 🇧🇬 ', 'bg'),
        ('Bengali 🇧🇩 ', 'bn'),
        ('Bosnian 🇧🇦 ', 'bs'),
        ('Catalan 🇪🇸 ', 'ca'),
        ('Czech 🇨🇿 ', 'cs'),
        ('Danish 🇩🇰 ', 'da'),
        ('Greek 🇬🇷 ', 'el'),
        ('Estonian 🇪🇪 ', 'et'),
        ('Finnish 🇫🇮 ', 'fi'),
        ('Gujarati 🇮🇳 ', 'gu'),
        ('Croatian 🇭🇷 ', 'hr'),
        ('Hungarian 🇭🇺 ', 'hu'),
        ('Indonesian 🇮🇩 ', 'id'),
        ('Icelandic 🇮🇸 ', 'is'),
        ('Hebrew 🇮🇱 ', 'iw'),
        ('Javanese 🇮🇱 ', 'jw'),
        ('Khmer 🇰🇭 ', 'km'),
        ('Kannada 🇮🇳 ', 'kn'),
        ('Korean 🇰🇷 ', 'ko'),
        ('Latin 🇲🇽 ', 'la'),
        ('Latvian 🇱🇻 ', 'lv'),
        ('Malayalam 🇮🇳 ', 'ml'),
        ('Marathi 🇮🇳 ', 'mr'),
        ('Malay 🇮🇱 ', 'ms'),
        ('Myanmar 🇲🇲 ', 'my'),
        ('Nepali 🇮🇳 ', 'ne'),
        ('Dutch 🇳🇱 ', 'nl'),
        ('Norwegian 🇳🇴 ', 'no'),
        ('Polish 🇵🇱 ', 'pl'),
        ('Portuguese 🇵🇹 ', 'pt'),
        ('Romanian 🇷🇴 ', 'ro'),
        ('Sinhala 🇱🇰 ', 'si'),
        ('Slovak 🇸🇰 ', 'sk'),
        ('Albanian 🇦🇱 ', 'sq'),
        ('Serbian 🇷🇸 ', 'sr'),
        ('Sundanese 🇸🇩 ', 'su'),
        ('Swedish 🇸🇪 ', 'sv'),
        ('Swahili 🇰🇪 ', 'sw'),
        ('Tamil 🇮🇳 ', 'ta'),
        ('Telugu 🇮🇳 ', 'te'),
        ('Thai 🇹🇭 ', 'th'),
        ('Filipino 🇵🇭 ', 'tl'),
        ('Urdu 🇮🇳 ', 'ur'),
        ('Vietnamese 🇻🇳 ', 'vi'),
        ('Chinese (Mandarin/Taiwan) 🇨🇳 ', 'zh-TW')
    )
};

callback_data_btns: tuple = (
    'ru', 'en', 'zh', 'es', 'fr', 'de', 'tr', 'ar', 'it', 'hi', 'zh-CN', 'ja', 'uk', 'af', 'bg',
    'bn', 'bs', 'ca', 'cs', 'da', 'el', 'et', 'fi', 'gu', 'hr', 'hu', 'id', 'is', 'iw', 'jw', 'km',
    'kn', 'ko', 'la', 'lv', 'ml', 'mr', 'ms', 'my', 'ne', 'nl', 'no', 'pl', 'pt', 'ro', 'si', 'sk',
    'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'ur', 'vi', 'zh-TW'
);

backbtn: dict = {
    "RU": "⬅️ Назад",
    "EN": "⬅️ Back"
};

nextbtn: dict = {
    "RU": "Вперед ➡️",
    "EN": "Next ➡️"
};

admin_menu_buttons: dict = {
    "RU": {"Добавить канал": "add_channel",
           "Удалить канал": "remove_channel",
           "Провести рассылку": "make_a_promotional_mailing"},
    "EN": {"Add channel": "add_channel",
           "Remove channel": "remove_channel",
           "Make a promotional mailing": "make_a_promotional_mailing"}
};

Continue: dict = {
    "RU": "Продолжить",
    "EN": "Continue"
};

Go_To_Menu: dict = {
    "RU": "Перейти к меню ➡️",
    "EN": "Go to menu ➡️"
};

select_article_buttons: dict = {
    "RU": {
        0: "Перейти к статье ➡️",
        1: ("Отправить текст статьи в сообщении ✍", "send_page_text${}"),
        2: ("⬅️ Вернуться назад", "back_to_menu${}")
    },
    "EN": {
        0: "Go to the article ➡️",
        1: ("Send page text via message ✍", "send_page_text"),
        2: ("⬅️ Go back", "back_to_menu${}")
    }
};
