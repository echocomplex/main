"""

SEARCH_TELEPHONE_INFO Function for Searcher bot
(https://t.me/SearcherMainBot (@SearcherMainBot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<< DESCRIPTION FOR DEVELOPERS >>

You can see an example in «if (__name__=="__main__")»

"""


""" IMPORTS """
import csv;
import json;
from phonenumbers.phonenumberutil import NumberParseException;
from phonenumbers import parse;
from phonenumbers import geocoder;
from phonenumbers import timezone;
from phonenumbers import carrier;
from messages import unknown_phone;



class Phone_Get_Info:

    def __init__ (self, phone: str, language: str) -> None:
        self.__phone: str = phone;
        self.__language: str = language;
        self.carrier: str = unknown_phone[language];
        self.region: str = unknown_phone[language];
        self.timezone: str = unknown_phone[language];

        # start parse
        if self.__phone[0:1] == "+":
            if self.__phone[1:2] == "7":
                self.__russia_num();
            else:
                self.__phnum_parse();
        elif self.__phone[0:1] == "8":
            self.__russia_num();
        else:
            self.__phnum_parse();

    def __russia_num (self) -> None:
        if ((self.__phone[0:1] == "+") and (self.__phone[2:3] == "9")):
            num_one = self.__phone[2:5];
            two_num = self.__phone[5:];
            self.__csv_read(num_one, two_num);
        elif ((self.__phone[0:1] == "8") and (self.__phone[1:2] == "9")):
            num_one = self.__phone[1:4];
            two_num = self.__phone[4:];
            self.__csv_read(num_one, two_num);
        else:
            self.__phnum_parse();


    def __csv_read (self, zone: str, number: str) -> None:
        with open('zone.json', 'r', encoding='utf-8') as f:
            zone_t = json.load(f);
        with open("DEF-9xx.csv", "r", encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="\t");
            for i, line in enumerate(reader):
                if (i != 0):
                    if ((line[0].split(";")[0] == zone) and (\
                            [k for k in range(int(line[0].split(";")[1]), int(line[0].split(";")[2])) if int(number) == k])):
                        prov = line[0].split(";")[4];
                        region = line[0].split(";")[5].strip();
                        try:
                            for z in zone_t:
                                if region in z:
                                    time_zone = z[region];
                            self.carrier = prov;
                            self.region = region;
                            self.timezone = time_zone;
                        except KeyError:
                            self.carrier = prov;
                            self.region = region;
                            self.timezone = unknown_phone[self.__language];

    def __phnum_parse (self) -> None:
        try:
            ph_parse = parse(self.__phone);
        except NumberParseException:
            return;
        ph_timezone = timezone.time_zones_for_number(ph_parse);
        ph_region = geocoder.description_for_number(ph_parse, self.__language.lower());
        ph_prov = carrier.name_for_number(ph_parse, self.__language.lower());
        if ph_prov == "":
            ph_prov = unknown_phone[self.__language];
        elif ph_region == "":
            ph_region = unknown_phone[self.__language];
        elif ph_timezone[0] == "":
            ph_timezone = unknown_phone[self.__language];

        # insert into variables
        self.carrier = ph_prov;
        self.region = ph_region;
        self.timezone = timezone;


if (__name__=="__main__"):
    phone: str = "<<Any Phone Number>>";
    language: str = "EN";
    info = Phone_Get_Info(phone, language);
    print(info.region, info.carrier, info.timezone);
